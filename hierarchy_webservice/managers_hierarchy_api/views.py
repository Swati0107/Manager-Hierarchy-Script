from django.shortcuts import render
from rest_framework.views import APIView
from .utils.generate_hierarchy import GenerateCSVController
import csv, os
import traceback
from django.http import JsonResponse
import operator
class HierarchyController(APIView):

    # read file and sort it by given keys
    input_folder_path ='/home/swastav/Desktop/Manager-Hierarchy-Script/hierarchy_webservice/managers_hierarchy_api/sample_input/sample_input.json'
    output_folder_path="/home/swati/Desktop/Manager-Hierarchy-Script/hierarchy_webservice/managers_hierarchy_api/sample_output/sample_output.csv"

    def get(self, request):
        try:
            result=None
            sortby=None

            if request.GET.get('sortby'):
                sortby= request.GET.get('sortby')
            print(sortby)
            
            # Run and calculate hierarchy for the input file
            if os.path.exists(self.input_folder_path):
                # Call the function which calculates the hierarchy
                result= GenerateCSVController().start_process(self.input_folder_path, self.output_folder_path, sortby)
            else:
                raise Exception("The input file doesn't exists! please provide input file in the sample input folder.")
            return JsonResponse({})
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error': str(e)})
        finally:
            return JsonResponse({'result': result})