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
    state_with_biggest_incr = statistic.biggest_incr(nparray, 1999, 2016, "Alzheimer's disease")
    plotter.line_deaths(nparray, state_with_biggest_incr, 1999, 2016, "Alzheimer's disease")


if __name__ == '__main__':
    main()