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
            
            Unique_id = str(primary.pk)+loom_no+str(piece_no)+str(set_no)
            
            primary=PrimaryTable(loom_no=loom_no,piece_no=piece_no,set_no=set_no,beam_no=beam_no,
            Unique_id=Unique_id,Descrip=Descrip,Weave=Weave,Weft_Count=Weft_Count,Act_Width=Act_Width,
            Warp_Count=Warp_Count,Sound_MTRSC=Sound_MTRSC,DOFE_MTRS=DOFE_MTRS,Act_EPI=Act_EPI,
            Doffed_Shift=Doffed_Shift,Act_PPI=Act_PPI)
            
            primary.pk = pk_store
            primary.save()

            return Response({"Unique_id":Unique_id},status=status.HTTP_201_CREATED)

        elif "fault" in request.data:
            Unique_id = request.data.get('Unique_id')
            meter_read = request.data.get('meter_read')
            fault = request.data.get('fault')
            second=SecondTable(fault=fault,meter=meter_read,Unique_id =Unique_id )
            second.save()
            return Response(status=status.HTTP_201_CREATED)
    
        elif "Unique_id_current" in request.data:
            Unique_id = request.data.get('Unique_id_current')
            for x in SecondTable.objects.filter(Unique_id=Unique_id).all():
                meter= x.meter
                # Yawn fault
                YSV_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='YSVButton').count()
                CV_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='CVButton').count()
                CW_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='CWftButton').count()
                ThTh_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='ThThButton').count()
                CM_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='CMButton').count()
                SY_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='SYButton').count()
                Ctn_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='CtnButton').count()
                CWp_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='CWpButton').count()
                
                
                third=ThirdTable(YSV_count=YSV_count,CV_count=CV_count,CW_count=CW_count,ThTh_count=ThTh_count,
                                CM_count=CM_count,SY_count=SY_count,Ctn_count=Ctn_count,CWp_count=CWp_count,
                                Unique_id=Unique_id,meter=meter)
                third.save()
            for row in ThirdTable.objects.filter(Unique_id=Unique_id).all().reverse():
                if ThirdTable.objects.filter(meter=row.meter,Unique_id=Unique_id).count() > 1:
                    row.delete()
            return Response(status=status.HTTP_201_CREATED)
        
    


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