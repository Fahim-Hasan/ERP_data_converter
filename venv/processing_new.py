import pandas as pd # Importing packages
import os
import glob


# Declaring keys and dictionary
keys = ['IDN00','IDN01','IDN02','IDN03','IDN04','PAT00','PAT01','PAT02','PAT03','PAT04','PAT05','PAT13','PAT20','PAT21','PAT23']    # add additional keys here
data = {} # Declaring empty dictionary


for i in keys:  # Creating empty dictionary with the declared keys and empty list
    data[i] = []


def read_file(file_name): # custom read function
    with open(file_name, "r") as file:  # reading text file
        lines = file.read().replace("\n", '').replace("!", "").replace("ENDIDN", "").replace("ENDPAT","")  # removing special characters and new lines

    values = lines.replace("IDN:", "").replace("PAT:", "").replace("$", "").split("|")

    return values

def processing(value): # processing data function
    data[str(value.split("=")[0])].append(str(value.split("=")[1])) # appending to the dictionary on specific key

def pre_processing(values): # This function will pre process the values from the file.
    for i in values:
        if len(i) > 0:
            processing(i.strip())  # strip() for removing white spaces
    df = pd.DataFrame(data)  # converting dictionary to dataframe
    return df



if __name__ == '__main__': # main function
    path = os.path.join(os.getcwd(),"data","*.txt")
    for filename in glob.glob(path):
        print(filename)
        contents = read_file(filename) # contents of the file, returned from read_file function

        final_df = pre_processing(contents) # final dataframe after processing the text data
        file = filename.split("/")[len(filename.split("/"))-1].replace(".txt","") # getting the latest file name and use it for final excel file

    final_df.to_excel(file+".xlsx",index=False) # final xlsx format output








