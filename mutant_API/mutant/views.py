

from itertools import count
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.response import Response
from .serializers import MutantSerializer
from .models import Mutant, isMutant
from rest_framework.views import APIView
import json
from .models import Mutant, isMutant





# Create your views here.

class MutantApiView(APIView):
 
    def get(self, request):
        teaMuntan = Mutant.objects.all()
        mutant_serializer = MutantSerializer(teaMuntan, many = True)
        return Response(mutant_serializer.data)

 

    def post (self, request):
        
        jd = json.loads((request.body).decode('utf-8')) 

        datos = isMutant(jd)
            #datos = json.dumps(datos)

            #datos = {'message':'Success'}
        #Mutant.adn= jd
        
        if datos:
            res = status.HTTP_200_OK
            Mutant.objects.create(adnMutant=jd)
            #Mutan.adn = 
        
        else:
            res = status.HTTP_403_FORBIDDEN
            Mutant.objects.create(Human=jd)


        return Response(res)

class StatsApiView(APIView):

    def get(self, request):
        
        teamMutan = Mutant.objects.exclude(adnMutant__isnull = True).count()
        allAdn = len(Mutant.objects.all()) # ¿?
        teamHuman = Mutant.objects.exclude(Human__isnull = True).count()
        if teamHuman == 0:
            ratio = teamMutan
        else:
            ratio = teamMutan / teamHuman

        res = {"count_mutant_dna":teamMutan, "count_human_dna":teamHuman, "ratio":ratio} 

        return JsonResponse(res)

 
