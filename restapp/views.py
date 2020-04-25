from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import PrimaryTable,SecondTable,ThirdTable,FourthTable
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
            primary=PrimaryTable()
            primary.save()
            pk_store=primary.pk
            Unique_id = str(primary.pk)+loom_no+str(piece_no)+str(set_no)
            primary=PrimaryTable(loom_no=loom_no,piece_no=piece_no,set_no=set_no,beam_no=beam_no,Unique_id=Unique_id )
            primary.pk = pk_store
            primary.save()
            # first = PrimaryTable.objects.all().only('Unique_id')
            # serializer= PrimaryTableSerializer(first)
            return Response({"Unique_id":Unique_id},status=status.HTTP_201_CREATED)

        elif "fault" in request.data:
            Unique_id = request.data.get('Unique_id')
            meter1 = request.data.get('meter1')
            fault = request.data.get('fault')
            second=SecondTable(fault=fault,meter=meter1,Unique_id =Unique_id )
            second.save()
            return Response(status=status.HTTP_201_CREATED)
        elif "Unique_id_current" in request.data:
            Unique_id = request.data.get('Unique_id_current')
            for x in SecondTable.objects.filter(Unique_id=Unique_id).all():
                meter= x.meter
                wdr_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='wdr').count()
                wdt_count = SecondTable.objects.filter(meter=meter, Unique_id=Unique_id,fault='wdt').count()
                cm_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='cm').count()
                cwp_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='cwp').count()
                sos_count = SecondTable.objects.filter(meter=meter,Unique_id=Unique_id, fault='sos').count()
                sv_count = SecondTable.objects.filter(meter=meter, Unique_id=Unique_id,fault='sv').count()
                third=ThirdTable(wdr_count=wdr_count,wdt_count=wdt_count,cm_count=cm_count,cwp_count=cwp_count,sos_count=sos_count,sv_count=sv_count,Unique_id=Unique_id,meter=meter)
                third.save()
            for row in ThirdTable.objects.filter(Unique_id=Unique_id).all().reverse():
                if ThirdTable.objects.filter(meter=row.meter,Unique_id=Unique_id).count() > 1:
                    row.delete()
            meter_dic = ThirdTable.objects.filter(Unique_id=Unique_id).aggregate(Max('meter'))
            meter_total=meter_dic.get("meter__max")
            wdr_count_dic = ThirdTable.objects.filter(Unique_id=Unique_id).aggregate(Sum('wdr_count'))
            wdr_count_total= wdr_count_dic.get("wdr_count__sum")
            wdt_count_dic = ThirdTable.objects.filter(Unique_id=Unique_id).aggregate(Sum('wdt_count'))
            wdt_count_total= wdt_count_dic.get("wdt_count__sum")
            cm_count_dic = ThirdTable.objects.filter(Unique_id=Unique_id).aggregate(Sum('cm_count'))
            cm_count_total= cm_count_dic.get("cm_count__sum")
            cwp_count_dic = ThirdTable.objects.filter(Unique_id=Unique_id).aggregate(Sum('cwp_count'))
            cwp_count_total= cwp_count_dic.get("cwp_count__sum")
            sos_count_dic = ThirdTable.objects.filter(Unique_id=Unique_id).aggregate(Sum('sos_count'))
            sos_count_total= sos_count_dic.get("sos_count__sum")
            sv_count_dic = ThirdTable.objects.filter(Unique_id=Unique_id).aggregate(Sum('sv_count'))
            sv_count_total= sv_count_dic.get("sv_count__sum")
            fourth=FourthTable(wdr_count_total=wdr_count_total,wdt_count_total=wdt_count_total,cm_count_total=cm_count_total,cwp_count_total=cwp_count_total,sos_count_total=sos_count_total,sv_count_total=sv_count_total,Unique_id=Unique_id,meter_total=meter_total)
            fourth.save()
            for row in FourthTable.objects.filter(Unique_id=Unique_id).all().reverse():
                if FourthTable.objects.filter(Unique_id=Unique_id).count() > 1:
                    row.delete()
            return Response(status=status.HTTP_201_CREATED)
        
    


# {
# "Unique_id":"38567567567",
# "meter1":"7",
# "fault":"4"

# }
    
#     {
#     "Unique_id_current": "38567567567"
# }
