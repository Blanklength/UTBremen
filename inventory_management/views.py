from django.shortcuts import render
from .models import Room
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import HttpResponse
from django.db.models import Q


# from .forms import FilterForm

# Create your views here.


class RoomListView(ListView):
    model = Room

    # f1 = FilterForm()
    # context = {"filter_field": f1}

    def get_queryset(self):
        query_search = self.request.GET.get("search")
        if query_search is None:
            return Room.objects.all()
        else:
            return Room.objects.filter(Q(room_name__contains=query_search) | Q(building_nr__contains=query_search) | Q(
                floor_nr__contains=query_search))


class RoomDetailView(DetailView):
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = str(self.request)[-3]
        context['room_num']=pk
        print(self.request)

        return context



def TestDetail(request, id):
    return HttpResponse(id)
