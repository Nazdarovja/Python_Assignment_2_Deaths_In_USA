from utility import csv2array
import numpy as np
import statistic
import plotter

def main():
    file_name = 'DeathsCSV.csv'
    nparray = csv2array(file_name)

    statistic.most_death(nparray, 2016)
    statistic.least_death(nparray, 2016)
    statistic.smallest_incr(nparray, 1999, 2016)
    statistic.most_death(nparray, 2005, 'Kidney disease')
    statistic.biggest_incr(nparray, 1999, 2016, "Alzheimer's disease")
    # plot udviklingen af deaths fra New Work, da ingen stater havde en stigning i deaths
    # i 1999-2016 med grunden "Alzheimer's disease"
    plotter.line_deaths(nparray, 'New York', 1999, 2016, "Alzheimer's disease")


if __name__ == '__main__':
    main()