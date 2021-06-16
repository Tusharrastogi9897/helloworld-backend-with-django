from django.urls import path
from .serializers import ChatRoomSerializer, UserSerializer
from .models import ChatRoom, User
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('room-list/<int:page>', GetListAPI.as_view(
        model_ = ChatRoom,
        serializer_ = ChatRoomSerializer
    )),
    path('user-list/<int:page>', GetListAPI.as_view(
        model_ = User,
        serializer_ = UserSerializer
    )),
    path('get-token/', TokenAPI.as_view())
]