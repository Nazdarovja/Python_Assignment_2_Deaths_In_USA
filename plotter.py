import matplotlib.pyplot as plt
import numpy as np

def line_deaths(array, state, f_year, t_year, cause='All causes'):
    """
        Shows a 'line' graph with years on x-axis and deaths on the y-axis
        Args:
            numpy array: array with data
            str: state
            int: from, year
            int: to, year
            str: cause (default=All causes)
    """

    # raise error if f_year >= t_year
    if f_year >= t_year:
        raise ValueError('from year must be less then to year')

    # create array of years
    years = np.arange(f_year, t_year + 1)

    # create array with all arrays which matches the criterias 
    deaths = array[(array[:,3] == state) & (array[:,2] == cause) & (array[:,0].astype(int) >= f_year) & (array[:,0].astype(int) <= t_year)]
    # remove all values but deaths as int
    deaths = [int(case[4]) for case in deaths]

    # plot result
    plt.plot(years, deaths)
    plt.show()