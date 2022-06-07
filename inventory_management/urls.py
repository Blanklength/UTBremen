from django.urls import path
from . import views
from .views import RoomListView
from .views import RoomDetailView


urlpatterns = [
    path('', RoomListView.as_view(), name="search_results"),
    path('<int:pk>', RoomDetailView.as_view(), name="room_details")
]
