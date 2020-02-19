from django.shortcuts import render
from rest_framework.views import APIView
from .utils.generate_hierarchy import GenerateCSVController
import csv, os
import traceback
from django.http import JsonResponse
import operator

# def sort_table(table, cols):
#     """ sort a table by multiple columns
#         table: a list of lists (or tuple of tuples) where each inner list 
#                represents a row
#         cols:  a list (or tuple) specifying the column numbers to sort by
#                e.g. (1,0) would sort by column 1, then by column 0
#     """
#     for col in reversed(cols):
#         table = sorted(table, key=operator.itemgetter(col))
#     return table


# def index(request, sortby=None):
#     # if sortby is not None:
#     data=[]
#     cols=[]
#     with open('hierarchy_webservice/managers_hierarchy_api/sample_output/sample_output.csv', 'r') as csvfile:
#         readCSV=csv.reader(csvfile, delimiter=',')
#         i = 0
#         for row in readCSV:
#             if i == 0:
#                 cols = list(row)
#             else:
#                 data.append(row)
#             i+=1
#     data = tuple(data)
#     data = sort_table(data, (1,0))
#     return render(request, 'index.html', {'data': data, 'rows': range(len(data)), 'cols': range(len(cols))})

def index(request, sortby=None):
    data={'users': [], 'levels':[]}
    for i in range(1, 9):
        data['managers'+str(i)] = []

    with open('hierarchy_webservice/managers_hierarchy_api/sample_output/sample_output.csv', 'r') as csvfile:
        readCSV=csv.reader(csvfile, delimiter=',')
        c = 0
        cols=[]

        for row in readCSV:
            if(c == 0 ):
                cols = row
                c += 1
            
            data['users'].append(row[0])
            data['levels'].append(row[-1])

            for i in range(1, 9):
                data['managers'+str(i)].append(row[i])
    return render(request, 'index.html', {'data': data, 'numbers': range(len(data['users'])), 'cols': cols})

class HierarchyController(APIView):

    def get(self, request):
        try:
            a=None
            if request.GET.get('sortby'):
                sortby= request.GET['sortby']
            else:
                sortby=None
            # read file and sort it by given keys
            input_folder_path ='/home/swati/Desktop/Manager-Hierarchy-Script/hierarchy_webservice/managers_hierarchy_api/sample_input/sample_input.json'
            
            # Run and calculate hierarchy for the input file
            if os.path.exists(input_folder_path):
                # Call the function which calculates the hierarchy
                a= GenerateCSVController().start_process()
            else:
                raise Exception("The input file doesn't exists! please provide input file in the sample input folder.")
            return JsonResponse({})
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error': str(e)})
        finally:
            return JsonResponse({'result': a})