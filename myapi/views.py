from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .serializers import UserSerializer
from .models import User

from .serializers import UserLoginHistorySerializer
from .models import UserLoginHistory

import requests
from ipware import get_client_ip

import jwt
import datetime

class IndexPage(APIView):
    def get(self, request):
        return Response({
            '/api/users': 'GET(list of users) and POST(create new user)',
            '/api/token': 'generate JWT token and login',
            '/api/profile': 'get profile view using JWT token'
        })

class UsersList(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class CreateToken(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        # get user details from db
        user = User.objects.filter(username=username).first()

        # verify user
        if user is None:
            raise AuthenticationFailed('user is not found')
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')

        # get ip address of the user
        ip, is_routable = get_client_ip(request)
        if ip is None:
            # Unable to get the client's IP address
            pass
        else:
            # We got the client's IP address 
            if is_routable:
                # The client's IP address is publicly routable on the Internet
                pass
            else:
                # The client's IP address is private
                pass
        
        # sending a webhook to the following URL
        response = requests.post('https://encrusxqoan0b.x.pipedream.net/', data = {'user': user.id, 'ip': ip})

        # save login history to db
        serializer = UserLoginHistory(userid = user.id, ip_address = ip)
        serializer.save()

        # generate jwt token
        payload = {
            'username': user.username
        }
        encoded = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=encoded, httponly=True)
        response.data = {
            'token': encoded
        }
        return response

class ProfileView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('unauthorized')
        
        try:
            payload = jwt.decode(token, "secret", algorithms="HS256")
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthorized')

        user = User.objects.filter(username=payload['username']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
