from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UsersList)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('token/', views.CreateToken.as_view(), name='token_obtain_pair'),
    path('profile/', views.ProfileView.as_view(), name='token_obtain_pair'),
]