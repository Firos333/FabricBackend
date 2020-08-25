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
    def __str__(self):
        return self.fault

faults = ['YSV_count_Yawn','CV_count_Yawn','CWft_count_Yawn','ThTh_count_Yawn',
'CM_count_Yawn','SY_count_Yawn','Ctn_count_Yawn','CWp_count_Yawn',

'SOS_count_Sizing','SPB_count_Sizing','SV_count_Sizing','SS_count_Sizing',

'COV_count_DyedYarn','STB_count_DyedYarn',

'DOP_count_Weavers','HS_count_Weavers','WDR_count_Weavers','WWft_count_Weavers','WDT_count_Weavers','SW_count_Weavers',

'EH_count_Machine','H_count_Machine','LM_count_Machine','LWP_count_Machine',
'MB_count_Machine','OWP_count_Machine', 'RM_count_Machine','SM_count_Machine','TM_count_Machine',

'BP_count_Machine','CR_count_Machine','DE_count_Machine','FL_count_Machine','LO_count_Machine',
'ME_count_Machine','SEF_count_Machine','TER_count_Machine','TL_count_Machine',

'BS_count_Machine','BTN_count_Machine','DM_count_Machine','DP_count_Machine','OWft_count_Machine'
,'TC_count_Machine','TP_count_Machine']

class ThirdTable(models.Model):
    
    Unique_id = models.CharField(max_length =50,default=0)
    meter = models.IntegerField(default=0)
    date_modified = models.DateField(auto_now=True)
    time_modified = models.TimeField(auto_now=True)
    time_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.Unique_id)
for fault in faults:
    ThirdTable.add_to_class(fault, models.CharField(max_length=150))