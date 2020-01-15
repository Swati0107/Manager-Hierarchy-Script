import json
from json.decoder import JSONDecodeError

# Creating random roles list to defind levels as of now
def create_sample_level_dict(title_set):

    level_count=int(len(title_set)/10)+1
    level_dict = {"l"+str(k): [] for k in range(1,level_count+1)} 

    for ind, role in enumerate(title_set):
        val=int(int(ind)/10)+1
        print(val)
        level_dict["l"+str(val)].append(role)
    print(level_dict, "level_dict")
    return level_dict

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

        for data in mapping_json.values():
            user_mapping[data]=set()

            for sub_data in data:
                title_set.add(sub_data['title'].split(',')[0])
                user_mapping[data].add(sub_data['email'])
                
    level_dict=create_sample_level_dict(title_set)


except JSONDecodeError:
    print("Please provide valid json as an input!!!")