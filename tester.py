import csv
import collections
import numpy as np

data = []

def readFile():
    with open('DeathsCSV.csv') as fp: 
        data = []
        reader = csv.reader(fp)
        for line in reader:
            if not line[0] == 'Year':
                data.append(line)
        return data
# 1 Which state has the most deaths in the year of 2016? (All causes)

def state_with_most_deaths_in_2016():
    reader = readFile()
    state = ""
    currentMostDeaths = 0
    for line in reader:
        if line[3] != 'United States' and line[0] == '2016' and line[2] == 'All causes' and int(line[4]) > currentMostDeaths:
            currentMostDeaths = int(line[4])
            state = line[3] 
    print(state, currentMostDeaths)
    
state_with_most_deaths_in_2016()

  





