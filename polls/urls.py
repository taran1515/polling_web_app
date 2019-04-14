from django.urls import path

from . import views

app_name='polls'
urlpatterns = [

    path('user_login' ,views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('<int:question_id>/results/',views.results,name='results')
]