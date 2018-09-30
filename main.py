import numpy as np
import utility as util
import statistic
import plotter
import sys

"""
How to run :  $`python main.py <CSV file URL>`

"""

def main():
    URL = sys.argv[1]
    file_name = 'DeathsCSV.csv' # Added file name because URL did not contain fitting name
    
    #Download file if not present
    util.download_as_file(URL,file_name)

    #Create numpy array from data
    nparray = util.csv2array(file_name)

    ## run methods ##
    statistic.state_with_most_deaths(nparray,2016)
    statistic.state_with_least_deaths(nparray, 2016)
    statistic.smallest_incr(nparray, 1999, 2016)
    statistic.state_with_most_deaths(nparray, "2005", 'Kidney disease')
    state_with_biggest_incr = statistic.biggest_incr(nparray, 1999, 2016, "Alzheimer's disease")
    plotter.line_deaths(nparray, state_with_biggest_incr, 1999, 2016, "Alzheimer's disease")

    ## plot % wise increase
    not_numpy_arr = util.readFile(file_name)
    plotter.state_with_biggest_increase_of_alzheimers_1999_to_2016_plot(not_numpy_arr)

if __name__ == '__main__':
    main()