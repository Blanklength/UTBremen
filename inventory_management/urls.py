from django.urls import path
from . import views
from .views import RoomListView
from .views import RoomDetailView
from .views import CreateRoomView


urlpatterns = [
    path('', RoomListView.as_view(), name="search_results"),
    path('<int:pk>', RoomDetailView.as_view(), name="room_details"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('create', CreateRoomView.as_view(), name='create')
]
