from django.shortcuts import render
from serializers import HierarchySerializers
from django.http import Request
from rest_framework.views import APIView
from django import JsonResponse
from genreate_hierarchy import start_process

class HierarchyController(APIView):

    def get(self, request):
        try:
            if request.GET.get('sortby'):
                sortby= request.GET['sortby']
            else:
                sortby=None
            # read file and sort it by given keys
            inpuy_folder_path = 'managers_hierarchy_api/sample_input/'
            
            # Run and calculate hierarchy for the input file
            if os.path.exists(input_folder_path):
                # Call the function which calculates the hierarchy
                start_process()
            else:
                raise Exception("The input file doesn't exists! please provide input file in the sample input folder.')

            if sortby is None:
                ## r=  write code to sort data in reuested format and return response
            else:
                ## read csv and sort data by request field
                pass
            return JsonResponse(r)
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error': str(e)})