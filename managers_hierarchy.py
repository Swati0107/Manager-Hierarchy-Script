import json
from json.decoder import JSONDecodeError
import pandas as pd

# Creating random roles list to defind levels as of now
# def create_sample_level_dict(title_set):

#     level_count=int(len(title_set)/10)+1
#     level_dict = {"l"+str(k): [] for k in range(1,level_count+1)} 

#     for ind, role in enumerate(title_set):
#         val=int(int(ind)/10)+1
#         print(val)
#         level_dict["l"+str(val)].append(role)
#     print(level_dict, "level_dict")
#     return level_dict

# Creating random roles list to defind levels as it's value
# def create_sample_level_dict(title_set):

#     level_count=int(len(title_set)/10)+1
#     level_dict = {v: "l"+str(int(int(k)%10)) for k,v in enumerate(title_set)} 

#     print(level_dict,'=========')

# Read Sample Json Path
path='sample_input/sample_dataset.json'

# Read dict data
try:
    with open(path) as f:
        mapping_json = json.load(f)
        title_set = set()
        print(mapping_json, type(mapping_json))
        user_mapping={}
        max_reporter=0

        for data in mapping_json:
            print(user_mapping, data)
            
            if data is not None:
                user_mapping[data]=set()
            
            if len(data)>0:
                count=0
                
                for sub_data in mapping_json[data]:
                    count+=1
                    title_set.add(sub_data['title'].split(',')[0])
                    user_mapping[data].add(sub_data['email'])
                
                if count>max_reporter:
                    max_reporter=count

    # level_dict=create_sample_level_dict(title_set)

    print(user_mapping, "user_mapping")
    print(max_reporter, "max_reporter")
    column_list = [ 'Manager ' + str(x)for x in range(1,max_reporter+1)]
    print(new_cols, 'new_cols')

    df=pd.DataFrame(columns=column_list)

except JSONDecodeError:
    print("Please provide valid json as an input!!!")