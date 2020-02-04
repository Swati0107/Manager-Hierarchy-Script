from django.shortcuts import render
from rest_framework.views import APIView
from .generate_hierarchy import GenerateCSVController
import csv, os
import traceback
from django.http import JsonResponse

def index(request, sortby=None):
    if sortby is not None:
        data={'users': [], 'levels':[]}

        with open('/home/swastav/Desktop/Manager-Hierarchy-Script/hierarchy_webservice/managers_hierarchy_api/sample_output/sample_output.csv', 'w+') as csvfile:
            readCSV=csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                data['users'].append(row[0])
                data['levels'].append(row[-1])

                for i in range(1,9):
                    data['managers'+str(i).append(row[i])]
    # else:
        ## write code to fetch sorted data for html

    return render(request, 'index.html', {'data': data, 'numbers': range(len(data['users']))})

class HierarchyController(APIView):

    def get(self, request):
        try:
            if request.GET.get('sortby'):
                sortby= request.GET['sortby']
            else:
                sortby=None
            # read file and sort it by given keys
            # input_folder_path = 'managers_hierarchy_api/sample_input/sample_input.json'
            input_folder_path ='/home/swastav/Desktop/Manager-Hierarchy-Script/hierarchy_webservice/managers_hierarchy_api/sample_input/sample_input.json'
            
            # Run and calculate hierarchy for the input file
            if os.path.exists(input_folder_path):
                # Call the function which calculates the hierarchy
                GenerateCSVController().start_process()
            else:
                raise Exception("The input file doesn't exists! please provide input file in the sample input folder.")
            ## read csv and sort data by request field
            index(sortby, input_folder_path)
            
            return JsonResponse(r)
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error': str(e)})