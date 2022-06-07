from django import forms
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


class CreateRoomForm(forms.Form):
    # room number can be 1 or 2
    building_nr = forms.CharField(max_length=10, choices=building_number_choices, default=1)
    # basement, ground floor, 1 floor, 2 floor
    floor_nr = forms.CharField(max_length=10, choices=floor, default="basement")
    room_name = forms.CharField(max_length=10)


class DeviceList(forms.Form):
    # devices
    pass
"""