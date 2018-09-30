import csv
import numpy as np
import requests
import os.path
import sys

def readFile(file_name):
    """
    Opens file from drive
    Args: 
        string : file_name
    """
    with open(file_name) as fp: 
        data = []
        reader = csv.reader(fp)
        for line in reader:
            if not line[0] == 'Year':
                data.append(line)
        return data

def csv2array(file_name):
    """
    Creates a numpy array from the .csv file and reverses is so the years are asc instead of desc
    
    """

    with open(file_name) as fp: 
        data = []
        reader = csv.reader(fp)

        # read first line which is the data description
        fp.readline()

        for line in reader:
            #data.append([int(line[0]), line[1], line[2], line[3], int(line[4]), float(line[5])])
            data.append(line)

        #data to numpy array
        arr = np.array(data)

        #reverse data to be asc instead of desc (years)
        reversed_arr = arr[::-1]
      
        return reversed_arr

        
def download_as_file(URL, file_name):
    """
    Download file from URL and save to file_name if not already present. If present, do nothing.
    
    """

    if not os.path.isfile(file_name):

        try:
            print("Downloading file...")
            response = requests.get(URL)
            as_string = response.text

            with open(file_name, 'w', encoding='utf8', newline='') as the_file:
                the_file.write(as_string)
        except Exception as e:
            print("Error downloading file; ", e)
            sys.exit(1)
        print("File downloaded.")
