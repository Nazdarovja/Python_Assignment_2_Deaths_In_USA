import csv

def readFile():
    with open('DeathsCSV.csv') as fp: 
        data = []
        reader = csv.reader(fp)
        for line in reader:
            if not line[0] == 'Year':
                data.append(line)
        return data