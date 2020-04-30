import datetime 
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone


class PrimaryTable(models.Model):

    Unique_id = models.CharField(max_length =50,default=0)
    loom_no = models.IntegerField(default=0)
    set_no = models.IntegerField(default=0)
    beam_no = models.IntegerField(default=0)
    piece_no = models.IntegerField(default=0)
    Descrip = models.CharField(max_length =250,default=0)
    Weave = models.IntegerField(default=0)
    Weft_Count = models.IntegerField(default=0)
    Act_Width = models.IntegerField(default=0)
    Warp_Count = models.IntegerField(default=0)
    Sound_MTRSC = models.IntegerField(default=0)
    DOFE_MTRS = models.IntegerField(default=0)
    Act_EPI = models.IntegerField(default=0)
    Act_PPI = models.IntegerField(default=0)
    Doffed_Shift = models.IntegerField(default=0)
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
    class meta():
        fields=('meter')


class ThirdTable(models.Model):
    
    Unique_id = models.CharField(max_length =50,default=0)
    meter = models.IntegerField(default=0)
    YSV_count = models.IntegerField(default=0)
    CV_count = models.IntegerField(default=0)
    CW_count = models.IntegerField(default=0)
    ThTh_count = models.IntegerField(default=0)
    CM_count = models.IntegerField(default=0)
    SY_count = models.IntegerField(default=0)
    Ctn_count = models.IntegerField(default=0)
    CWp_count = models.IntegerField(default=0)
    
    
    # wdr_count = models.IntegerField(default=0)
    # wdt_count = models.IntegerField(default=0)
    # cm_count = models.IntegerField(default=0)
    # cwp_count = models.IntegerField(default=0)
    # sos_count = models.IntegerField(default=0)
    # sv_count = models.IntegerField(default=0)
    # date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)
    time_date = models.DateTimeField(auto_now=True)

class FourthTable(models.Model):
    Unique_id = models.CharField(max_length =50,default=0)
    meter_total = models.IntegerField(default=0)
    wdr_count_total = models.IntegerField(default=0)
    wdt_count_total = models.IntegerField(default=0)
    cm_count_total = models.IntegerField(default=0)
    cwp_count_total = models.IntegerField(default=0)
    sos_count_total = models.IntegerField(default=0)
    sv_count_total = models.IntegerField(default=0)
    time_date = models.DateTimeField(auto_now=True)