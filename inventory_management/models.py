from django.db import models
from django.utils.timezone import now


# Create your models here.


# user
class User(models.Model):
    username = models.CharField(max_length=10, default=None)
    user_password = models.CharField(max_length=10, default=None)


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
    device_series = models.CharField(max_length=50, default=None)
    device_series_num = models.IntegerField(max_length=10, default=None)

    def __str__(self):
        return f'{self.device_brand} {self.device_series} {self.device_series_num}'


class Device(models.Model):
    device_production_date = models.DateField(default=now())
    device_serial_number = models.CharField(max_length=50, default=None)
    device_warranty_date = models.DateField(default=now())
    device_is_working = models.BooleanField(default=True)
    device_special_notes = models.CharField(max_length=50, default=None, blank=True)
    device_typ = models.ForeignKey(Device_Type, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return f'{self.device_serial_number} {self.device_typ}'


#################################################################
# Beamer
#################################################################

class Projector_Brand_Typ(Device_Type):
    class Meta:
        verbose_name = "Projektor Typ"
        verbose_name_plural = "Projektor Typen"


class Projector(Device):
    class Meta:
        verbose_name = "Projektor"
        verbose_name_plural = "Projektoren"


#################################################################
# Canvas
#################################################################

class Canvas(models.Model):
    class Meta:
        verbose_name = "Tafel"
        verbose_name_plural = "Tafeln"

    plate_amounts = models.CharField(max_length=10, choices=plate_amount_choices, default=1)

    def __str__(self):
        return f'Canva with the amount of {self.plate_amounts} plates'


#################################################################
# Speaker
#################################################################

class Speaker_typ(Device_Type):
    class Meta:
        verbose_name = "Lautsprecher Typ"
        verbose_name_plural = "Lautsprecher Typen"


class Speaker(Device):
    class Meta:
        verbose_name = "Lautsprecher"
        verbose_name_plural = "Lautsprecher"


#################################################################
# Smart Boards
#################################################################

class SmartBoard_typ(Device_Type):
    class Meta:
        verbose_name = "Smartboard Type"
        verbose_name_plural = "Smartboard Typen"


class SmartBoard(Device):
    class Meta:
        verbose_name = "Smartboard"
        verbose_name_plural = "Smartboards"


#################################################################
# Cameras
#################################################################


class Camera_typ(Device_Type):
    class Meta:
        verbose_name = "Kamera Type"
        verbose_name_plural = "Kamera Typen"


class Camera(Device):
    class Meta:
        verbose_name = "Kamera"
        verbose_name_plural = "Kameras"


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
    smart_board = models.OneToOneField(SmartBoard, on_delete=models.SET_NULL, blank=True, default=None, null=True)
    speaker = models.OneToOneField(Speaker, on_delete=models.SET_NULL, blank=True, default=None, null=True)
    canvas = models.OneToOneField(Canvas, on_delete=models.SET_NULL, blank=True, default=None, null=True)

    def __str__(self):
        return f'{self.room_name} {self.building_nr} {self.floor_nr}'
