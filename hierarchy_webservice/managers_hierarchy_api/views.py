from django.shortcuts import render
from serializers import HierarchySerializers
from django.http import Request
from rest_framework.views import APIView
from django import JsonResponse

class HierarchyController(APIView):

    def get(self, request):
        try:
            if request.GET.get('sortby'):
                sortby= request.GET['sortby']
            else:
                sortby=None
            # read file and sort it by given keys
            
            if sortby is None:
                ## r=  write code to sort data in reuested format and return response
            else:
                ## read csv and sort data by request field
                pass
            return JsonResponse(r)
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error': str(e)})