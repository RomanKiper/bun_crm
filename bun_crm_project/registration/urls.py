# from django.urls import path
# from .import views
#
# urlpatterns = [
#
#     path('registration', views.registration, name='registration'),
#     path('signin', views.signin, name='signin'),
#     path('user_account', views.user_account, name='user_account'),
# ]


from django.urls import path

from .views import RegisterCreateView, SignInView, LogoutView, ProfileView

urlpatterns = [
    path('registration/', RegisterCreateView.as_view(), name='registration'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logaut/', LogoutView.as_view(), name='logaut'),
    path('user_account', ProfileView.as_view(), name='user_account')
]