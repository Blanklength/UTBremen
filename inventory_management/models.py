from django.db import models
import datetime

# Create your models here.

# choices
building_number_choices = [
    ("BA1", "BA1"),
    ("BA2", "BA2")
]

# amount of plates of a canvas
plate_amount_choices = [
    ("1", "1"),
    ("2", "2"),
    ("4", "4")
]

floor = [
    ("BST", "Basement"),
    ("GF", "Ground Floor"),
    ("1F", "First Floor"),
    ("2F", "Second Floor")
]


class Device_Type(models.Model):
    device_brand = models.CharField(max_length=50, default=None)
    device_serie = models.CharField(max_length=50, default=None)
    device_serie_num = models.IntegerField(max_length=10, default=None)

    def __str__(self):
        return f'{self.device_brand} {self.device_serie} {self.device_serie_num}'


class Device(models.Model):
    device_production_date = models.DateField(default=datetime.date.today())
    device_serial_number = models.CharField(max_length=50, default=None)
    device_warantee_date = models.DateField(default=datetime.date.today())
    device_is_working = models.BooleanField(default=True)
    device_special_notes = models.CharField(max_length=50, default=None, blank=True)
    device_typ = models.ForeignKey(Device_Type, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return f'{self.device_serial_number} {self.device_typ}'


#################################################################
# Beamer
#################################################################

class Projector_Brand_Typ(Device_Type):
    pass


class Projector(Device):
    pass


#################################################################
# Canvas
#################################################################

class Canvas(models.Model):
    plate_amounts = models.CharField(max_length=10, choices=plate_amount_choices, default=1)

    def __str__(self):
        return f'Canva with the amount of {self.plate_amounts} plates'


#################################################################
# Speaker
#################################################################

class Speaker_typ(Device_Type):
    pass


class Speaker(Device):
    pass


#################################################################
# Smart Boards
#################################################################

class SmartBoard_typ(Device_Type):
    pass


class SmartBoard(Device):
    pass


#################################################################
# Cameras
#################################################################


class Camera_typ(Device_Type):
    pass


class Camera(Device):
    pass


#################################################################
# Room
#################################################################

class Room(models.Model):
    # room number can be 1 or 2
    building_nr = models.CharField(max_length=10, choices=building_number_choices, default=1)
    # basement, ground floor, 1 floor, 2 floor
    floor_nr = models.CharField(max_length=10, choices=floor, default="basement")
    room_name = models.CharField(max_length=10)
    projector = models.OneToOneField(Projector, on_delete=models.SET_NULL, blank=True, default=None, null=True)
    smartboard = models.OneToOneField(SmartBoard, on_delete=models.SET_NULL, blank=True, default=None, null=True)
    speaker = models.OneToOneField(Speaker, on_delete=models.SET_NULL, blank=True, default=None, null=True)
    canva = models.OneToOneField(Canvas, on_delete=models.SET_NULL, blank=True, default=None, null=True)

    def __str__(self):
        return f'{self.room_name} {self.building_nr} {self.floor_nr}'
