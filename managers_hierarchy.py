# Import all dependencies required to run the script
import json
import pandas as pd
from json.decoder import JSONDecodeError
import csv
import time
import datetime

# Track starting time
start_time = time.time()

# Creating random roles list to defind levels as it's value
def create_sample_level_dict(title_set):

    level_count=int(len(title_set)/10)+1
    level_dict = {v: "L"+str(int(int(k)%10)+1) for k,v in enumerate(title_set)} 
    return level_dict

# Read Sample Input Json Path
input_path='sample_input/sample_dataset.json'

# Read Sample Output Json Path
output_path="sample_output/sample_output_"+ str(int(start_time)) +"_.csv"

# Read dict data
try:
    # Open Input file stored in above mentioned path
    with open(input_path) as f:
        # load dictionary inside a variable
        mapping_json = json.load(f)
        title_set = set()           # To store all role to help creating sample role and manager level dict
        user_reporter_mapping={}    # To store each user and reporter mapping
        max_reporter=0              # To get the count of max reporters to create column list at the end
        user_role={}                # Store mapping of each user and thier role, if exists!
        u_list=[]                   # Create data to dump in csv
        
        for data in mapping_json:
            
            if data is not None:
                user_reporter_mapping[data]=set()
            if len(data)>0:
                count=0
                
                for sub_data in mapping_json[data]:
                    count+=1
                    title_set.add(sub_data['title'].split(',')[0])
                    user_reporter_mapping[data].add(sub_data['email'])

                    user_role.update({sub_data['email']:sub_data['title'].split(',')[0]})

                u_list.append([data]+list(user_reporter_mapping[data]))

                if count>max_reporter:
                    max_reporter=count

    # Method call to create dummy sample role and manager level dict
    level_dict=create_sample_level_dict(title_set)
    
    ul_list_final = []  # Store final data with manager level
    
    for ul in u_list:
        if(ul[0] in user_role):
            val=level_dict[user_role[ul[0]]]
        else:
            val=None

        if len(ul)>1:
            ul_list_final.append([ul[0]]+[val]+ul[1:])
        else:
            ul_list_final.append([ul[0]]+[val])

    # Define column using pandas to dump in csv
    column_list = [ 'Manager ' + str(x)for x in range(1,max_reporter+1)]
    column_list.insert(0, 'User')
    column_list.insert(1,'Manager_Role_Position')
    
    df = pd.DataFrame(data=ul_list_final, columns=column_list).fillna('')

    df['Manager Level']=df['Manager_Role_Position']
    del df['Manager_Role_Position'] 
    df.to_csv(output_path, index=None)
 
except JSONDecodeError:
    print("Please provide valid json as an input!!!")

except Exception as ex:
    print("There is something went wrong int the script!", ex)

finally:
    print("Start time of script: ", int(start_time))
    print("Total execution time: ", time.time()-start_time)

