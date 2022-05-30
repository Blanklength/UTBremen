from django.urls import path
from . import views
from .views import RoomListView


urlpatterns = [
    path('', RoomListView.as_view(), name="search_results")
]
