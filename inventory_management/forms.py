from django import forms
from .models import building_number_choices
from .models import floor

""""
device_choices = (
    ("Pj", "Projector"),
    ("CV", "Canvas"),
    ("", "Projector"),
    ("Pj", "Projector"),
    ("Pj", "Projector"),
    ("Pj", "Projector"),
)


class FilterForm(forms.Form):
    room_field = forms.CharField(label="Raumnummer", max_length=10)
    building_field = forms.CharField(label="Bauabschnitt", max_length=10)
    floor_field = forms.CharField(label="Etage", max_length=10)
    device_field = forms.CharField(choices=device_choices)


class DeviceList(forms.Form):
    # devices
    pass
"""


class CreateRoomForm(forms.Form):
    # room number can be 1 or 2
    building_nr = forms.ChoiceField(choices=building_number_choices)
    # basement, ground floor, 1 floor, 2 floor
    floor_nr = forms.ChoiceField(choices=floor)
    room_name = forms.CharField(max_length=10)
