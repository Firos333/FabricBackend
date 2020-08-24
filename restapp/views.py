from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import PrimaryTable,SecondTable,ThirdTable
from django.shortcuts import get_object_or_404
from .serializers import PrimaryTableSerializer
from django.db.models import Sum,Max



class Tables(APIView):

    
    def post(self,request):
        if "loom_no" in request.data:
            
            loom_no = request.data.get('loom_no')
            piece_no = request.data.get('piece_no')
            set_no = request.data.get('set_no')
            beam_no = request.data.get('beam_no')
            Descrip = request.data.get('Descrip')
            Weave = request.data.get('Weave')
            Weft_Count = request.data.get('Weft_Count')
            Act_Width = request.data.get('Act_Width')
            Warp_Count = request.data.get('Warp_Count')
            Sound_MTRSC = request.data.get('Sound_MTRSC')
            DOFE_MTRS = request.data.get('DOFE_MTRS')
            Act_EPI = request.data.get('Act_EPI')
            Act_PPI= request.data.get('Act_PPI')
            Doffed_Shift = request.data.get('Doffed_Shift')
            
            primary=PrimaryTable()
            primary.save()
            pk_store=primary.pk
            
            Unique_id = str(primary.pk)+loom_no+piece_no+set_no+beam_no
            
            primary=PrimaryTable(loom_no=loom_no,piece_no=piece_no,set_no=set_no,beam_no=beam_no,
            Unique_id=Unique_id,Descrip=Descrip,Weave=Weave,Weft_Count=Weft_Count,Act_Width=Act_Width,
            Warp_Count=Warp_Count,Sound_MTRSC=Sound_MTRSC,DOFE_MTRS=DOFE_MTRS,Act_EPI=Act_EPI,
            Doffed_Shift=Doffed_Shift,Act_PPI=Act_PPI)
            
            primary.pk = pk_store
            primary.save()

            return Response({"Unique_id":Unique_id},status=status.HTTP_201_CREATED)

        elif "fault" in request.data:
            faultss = ['YSV_count_Yawn','CV_count_Yawn','CW_count_Yawn','ThTh_count_Yawn',
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
            Unique_id = request.data.get('Unique_id')
            meter_read = request.data.get('meter_read')
            fault = request.data.get('fault')
            second=SecondTable(fault=fault,meter=meter_read,Unique_id =Unique_id )
            second.save()
            
            faultcount= SecondTable.objects.filter(meter=meter_read,Unique_id=Unique_id, fault=fault).count()
            
            x = ThirdTable.objects.filter(meter=meter_read,Unique_id=Unique_id).count()
            
            
            if x < 1:
                third = ThirdTable(meter=meter_read,Unique_id=Unique_id)
                third.save()
                x=1

            if x > 0:
                get_pk =ThirdTable.objects.filter(meter=meter_read,Unique_id=Unique_id).values('pk')
                y = get_pk[0]['pk']
                listed = fault.split("B", 1)
                letter = listed[0]
                starts_with = [word for word in faultss if word.startswith(letter)]
                name=starts_with[0] 
                print(name)
                if name in faultss:
                    dictionary = {'meter':meter_read,'Unique_id':Unique_id,name:faultcount}
                for field, value in dictionary.items():
                    instance= ThirdTable.objects.get(pk=y)
                    setattr(instance, field, value)
                    instance.save()    
            return Response(status=status.HTTP_201_CREATED)
        
        elif "Unique_id_continue" in request.data:
            Unique_id_check=request.data.get('Unique_id_continue')
            if PrimaryTable.objects.filter(Unique_id=Unique_id_check).count()==1:
                return Response({"Unique_id_continue":'yes'},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Unique_id_continue":'No'},status=status.HTTP_400_BAD_REQUEST)
    


# {
# "Unique_id":"38567567567",
# "meter1":"7",
# "fault":"cm"

# }
    
#     {
#     "Unique_id_current": "38567567567"
# }

#  {
#     "loom_no": "333",
#     "piece_no":"45",
#     "set_no": "333",
#     "beam_no":"45"  
# }
# {
# "row":[
# {
# "Unique_id":"3n",
# "meter1":"4",
# "fault":"sov"

# },

# {
# "Unique_id":"3n",
# "meter1":"7",
# "fault":"wdt"

# }

# ]}


# {
# "Unique_id":"1n",
# "meter_read":"7",
# "fault":"YSVButton"

# }
