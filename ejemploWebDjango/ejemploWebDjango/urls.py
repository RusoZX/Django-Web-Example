"""ejemploWebDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.core.views import homePage, signup
from apps.feed.views import feed, search
from apps.feed.api import api_add_post, api_add_like_post
from apps.userprofile.views import userprofile, like_user, unlike_user, likesreceived, likesgiven, edit_profile
from apps.conversaciones.views import conversaciones, conversacion
from apps.conversaciones.api import api_add_mensaje
from apps.notification.views import notifications

from django.contrib.auth import views



urlpatterns = [
    path("", homePage, name="homePage"),
    path("signup/", signup, name="signup"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("login/", views.LoginView.as_view(template_name='core/login.html'), name="login"),

    path("feed/", feed, name="feed"),
    path("search/", search, name="search"),
    path("notifications/", notifications, name="notifications"),
    path("u/<str:username>/", userprofile, name='userprofile'),
    path("edit_profile/", edit_profile, name='edit_profile'),
    path("conversaciones/", conversaciones, name='conversaciones'),
    path("conversaciones/<int:user_id>/", conversacion, name='conversacion'),

    path("u/<str:username>/like/", like_user, name='like_user'),
    path("u/<str:username>/unlike/", unlike_user, name='unlike_user'),
    path("u/<str:username>/likesreceived/", likesreceived, name="likesreceived"),
    path("u/<str:username>/likesgiven/", likesgiven, name="likesgiven"),

    path("feed/api/add_post/", api_add_post, name="api_add_post"),
    path("feed/api/add_like_post/", api_add_like_post, name="api_add_like_post"),
    path("conversacion/api/add_mensaje/", api_add_mensaje, name="api_add_mensaje"),

    path("admin/", admin.site.urls),
    

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
