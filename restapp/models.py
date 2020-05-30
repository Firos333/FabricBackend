import datetime 
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone


class PrimaryTable(models.Model):

    Unique_id = models.CharField(max_length =50,default=0)
    loom_no = models.CharField(max_length =50,default=0)
    set_no = models.CharField(max_length =50,default=0)
    beam_no = models.CharField(max_length =50,default=0)
    piece_no = models.CharField(max_length =50,default=0)
    Descrip = models.CharField(max_length =250,default=0)
    Weave = models.CharField(max_length =50,default=0)
    Weft_Count = models.CharField(max_length =50,default=0)
    Act_Width = models.CharField(max_length =50,default=0)
    Warp_Count = models.CharField(max_length =50,default=0)
    Sound_MTRSC = models.CharField(max_length =50,default=0)
    DOFE_MTRS = models.CharField(max_length =50,default=0)
    Act_EPI = models.CharField(max_length =50,default=0)
    Act_PPI = models.CharField(max_length =50,default=0)
    Doffed_Shift = models.CharField(max_length =50,default=0)
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

    # Yawn fault
    YSV_count = models.IntegerField(default=0)
    CV_count = models.IntegerField(default=0)
    CW_count = models.IntegerField(default=0)
    ThTh_count = models.IntegerField(default=0)
    CM_count = models.IntegerField(default=0)
    SY_count = models.IntegerField(default=0)
    Ctn_count = models.IntegerField(default=0)
    CWp_count = models.IntegerField(default=0)
    
    # Sizing fault
    SOS_count = models.IntegerField(default=0)
    SPB_count = models.IntegerField(default=0)
    SV_count = models.IntegerField(default=0)
    SS_count = models.IntegerField(default=0)

    #DyedYarn Faults
    COV_count = models.IntegerField(default=0)
    STB_count = models.IntegerField(default=0)

    #Weavers Fault buttons
    DOP_count = models.IntegerField(default=0)
    HS_count = models.IntegerField(default=0)
    WDR_count = models.IntegerField(default=0)
    WWft_count = models.IntegerField(default=0)
    WDT_count = models.IntegerField(default=0)
    SW_count = models.IntegerField(default=0)

    #Machine Faults
    EH_count = models.IntegerField(default=0)
    H_count = models.IntegerField(default=0)
    LM_count = models.IntegerField(default=0)
    LWP_count = models.IntegerField(default=0)
    MB_count = models.IntegerField(default=0)
    OWP_count = models.IntegerField(default=0)
    RM_count= models.IntegerField(default=0)
    SM_count = models.IntegerField(default=0)
    TM_count = models.IntegerField(default=0)

    BP_count = models.IntegerField(default=0)
    CR_count = models.IntegerField(default=0)
    DE_count = models.IntegerField(default=0)
    FL_count = models.IntegerField(default=0)
    LO_count = models.IntegerField(default=0)
    ME_count = models.IntegerField(default=0)
    SEF_count = models.IntegerField(default=0)
    TER_count = models.IntegerField(default=0)
    TL_count = models.IntegerField(default=0)

    BS_count = models.IntegerField(default=0)
    BTN_count = models.IntegerField(default=0)
    DM_count = models.IntegerField(default=0)
    DP_count = models.IntegerField(default=0)
    OWft_count = models.IntegerField(default=0)
    TC_count = models.IntegerField(default=0)
    TP_count = models.IntegerField(default=0)
    

    date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)
    time_date = models.DateTimeField(auto_now=True)

