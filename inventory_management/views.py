from django.shortcuts import render
from .models import Room
from django.views.generic import ListView

# Create your views here.



class RoomListView(ListView):
    model = Room
    def get_queryset(self):
        query_search = self.request.GET.get("search")
        if query_search is None:
            return Room.objects.all()
        else:
            return Room.objects.filter(room_name__startswith=query_search)
