from django.shortcuts import render
from .models import Room
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import CreateRoomForm


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
        room = Room.objects.get(pk=int(pk))
        context['room_num'] = room.room_name
        print(self.request)

        return context



class CreateRoomView(CreateView):
    model = Room
    fields = '__all__'

    def get_context_data(self, **kwargs):
        form1 = CreateRoomForm()
        return {'form': form1}

    def get_success_url(self):
        return '/'


def delete(request, id):
    room = Room.objects.get(id=id)
    room.delete()

    return HttpResponseRedirect("/")
