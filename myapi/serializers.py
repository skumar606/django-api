from rest_framework import serializers

from .models import User
from .models import UserLoginHistory

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserLoginHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: UserLoginHistory
        fields: ('userid', 'login_time', 'ip_address')