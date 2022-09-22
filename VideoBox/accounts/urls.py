from django.urls import path
# from knox.views import LogoutView

from .views import user_init


urlpatterns = [
    path('user_init', user_init, name='user_init'),
    # path('logout', LogoutView.as_view(), name='logout'),
]
