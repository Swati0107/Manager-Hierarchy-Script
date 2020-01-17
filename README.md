# Manager-Hierarchy-Script

## About the Script

This is a script written in python which is used to get generates a file with the managers' hierarchy and their own level for each user.

    1. Takes input json dataset named sample_dataset.json in the directory named sample_input
    2. Process it
    3. Create a csv file containing the hierarchy of managers for each user according to the highest level to lowest
    4. Output of this script get stored in the file sample_output.csv in the directory named sample_output

## Prerequisites
- python==3.5.8
- pandas==0.25.3

# Steps to run the script

- Go to the same directory and run the below command
- python managers_hierarchy.py


## Sample Employee and Manager Level mapping
{
  "Sales Operations Manager": "l1",
  "Head of Customer Experience Strategy": "l2",
  "Supervisor": "l3",
  "Sales Director - CSM": "l4",
  "Senior Sales Manager - Federal": "l5",
  "Regional Sales Director – Healthcare & SLED": "l6",
  "Sr. Manager Solution Consulting": "l10",
  "Sales Director - Spain": "l1",
  "Sr Manager": "l2"
}
