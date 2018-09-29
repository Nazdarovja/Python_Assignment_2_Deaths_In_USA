import csv
import numpy as np

def readFile():
    with open('DeathsCSV.csv') as fp: 
        data = []
        reader = csv.reader(fp)
        for line in reader:
            if not line[0] == 'Year':
                data.append(line)
        return data

def csv2array(file_name):
    with open(file_name) as fp: 
        data = []
        reader = csv.reader(fp)

        # read first line which is the data description
        fp.readline()

        for line in reader:
            #data.append([int(line[0]), line[1], line[2], line[3], int(line[4]), float(line[5])])
            data.append(line)

        #print(type(data[0][0]))
        return np.array(data)