import datetime 
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone


class PrimaryTable(models.Model):

    Unique_id = models.CharField(max_length =50,default=0,unique=True)
    loom_no = models.CharField(max_length =50,default=0)
    set_no = models.IntegerField(default=0)
    beam_no = models.IntegerField(default=0)
    piece_no = models.IntegerField(default=0)
    date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)
    def __str__(self):
        return self.Unique_id

class SecondTable(models.Model):
    Unique_id = models.CharField(max_length =50,default=0)
    meter = models.IntegerField(default=0)
    fault = models.CharField(max_length =50,default=0)
    date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)
    time_date = models.DateTimeField(auto_now=True)

class ThirdTable(models.Model):
    
    Unique_id = models.CharField(max_length =50,default=0)
    meter = models.IntegerField(default=0)
    wdr_count = models.IntegerField(default=0)
    wdt_count = models.IntegerField(default=0)
    cm_count = models.IntegerField(default=0)
    cwp_count = models.IntegerField(default=0)
    sos_count = models.IntegerField(default=0)
    sv_count = models.IntegerField(default=0)
    date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)
    time_date = models.DateTimeField(auto_now=True)