from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("findmeian/", views.findmeian, name="findmeian"),
    path("about/", views.about, name="about"),
    path("login/",views.login_view,name="login"),
    path("register/",views.register_view,name="register"),
    path('freetotalk/',views.freetotalk_view,name='freetotalk'),
    path('question/',views.question_view,name='question'),
    path('profile/<str:username>/',views.user_profile_view,name='userprofile')
]