from django.urls import path
from .views import tracker_view, register_view, login_view

urlpatterns = [
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path("", tracker_view, name="tracker_view"),
]
