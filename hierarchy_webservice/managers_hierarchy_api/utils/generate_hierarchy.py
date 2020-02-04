# Import all dependencies required to run the script
import json
import pandas as pd
from json.decoder import JSONDecodeError
import csv
import time
import traceback

class GenerateCSVController():
    # Creating random roles list to defind levels as it's value
    def create_level_mapping(self, user_level_dict):
        for k,v in user_level_dict.items():
            if user_level_dict[k]:
                user_level_dict[k]="L"+str(max(user_level_dict[k]))
        return user_level_dict


    def start_process(self):
        # Track starting time
        start_time = time.time()
        # Read Sample Input Json Path
        input_path='hierarchy_webservice/managers_hierarchy_api/sample_input/sample_input.json'

        # Read Sample Output Json Path
        output_path="hierarchy_webservice/managers_hierarchy_api/sample_output/sample_output.csv"
        
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
                
                user_level_mapping={}
                for data in mapping_json:
                    
                    if data is not None:
                        user_reporter_mapping[data]=set()
                    if len(data)>0:
                        count=0
                        index=0
        
                        for sub_data in mapping_json[data]:
                            count+=1
                            index=index+1
                            
                            # Check if the key aleady exist for the existing users
                            if sub_data['email'] not in user_level_mapping:
                                user_level_mapping[sub_data['email']]=set()
                            else:
                                user_level_mapping[sub_data['email']].add(index)
                            
                            user_reporter_mapping[data].add(sub_data['email'])
        
                        u_list.append([data]+list(user_reporter_mapping[data]))
        
                        if count>max_reporter:
                            max_reporter=count
        
            # Method call to get identify exact level of the employee 
            level_dict=self.create_level_mapping(user_level_mapping)
            ul_list_final = []  # Store final data with manager level
            
            for ul in u_list:
                if ul[0] in level_dict and len(level_dict[ul[0]])>0:
                    val=level_dict[ul[0]]
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
            traceback.print_exc()
            print("There is something went wrong in the script!", ex)
        
        finally:
            print("Total execution time: ", time.time()-start_time)
        