from django.contrib.auth import views as auth_views
from django.urls import path
from graphene_django.views import GraphQLView

from . import views

urlpatterns = [
	path('', views.index, name="index"),
    path("login/",
    	auth_views.LoginView.as_view(template_name="registration/login.html"),
    	name="login"),
    path('api/graphql/', GraphQLView.as_view(graphiql=True)),
]
