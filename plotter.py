import matplotlib.pyplot as plt
import numpy as np
import collections

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

    #Label the plots
    plt.title(f"Biggest increase in death count form \nAlzheimers in {state}")
    plt.xlabel("Years")
    plt.ylabel("Deaths")
    plt.xticks(rotation='vertical')
    
    # plot result
    plt.plot(years.astype(str), deaths)
    plt.show()

def state_with_biggest_increase_of_alzheimers_1999_to_2016_plot(data):
    
    """
        5) Which state has had the biggest increase in the death of Alzheimers from 1999-2016?

        Plot the increase year for year using matplotlib

        Uses a regular list and finds and plots the data, but this one checks % increase insted of death count increase.
        
    """
    
    # Finding out which state has had the biggest increase...

    deaths_2016 = []
    deaths_1999 = []
    increase_per_state = {}
    for line in data:
        if line[3] != 'United States' and line[0] == '2016' and line[2] == "Alzheimer's disease":
            deaths_2016.append({'state': line[3], 'deaths': int(line[4])})
        if line[3] != 'United States' and line[0] == '1999' and line[2] == "Alzheimer's disease":
            deaths_1999.append({'state': line[3], 'deaths': int(line[4])})
    for i in range(0, len(deaths_1999)):
        state = deaths_1999[i]['state']
        increase = (deaths_2016[i]['deaths'] / deaths_1999[i]['deaths']) * 100 - 100
        increase_per_state[state] = increase
    state = collections.Counter.most_common(increase_per_state)[0][0]

    # Given the state from above, get data from all years of it

    state_year = []
    state_change = []
    for line in data:
        if line[3] == state and line[2] == "Alzheimer's disease":
            state_year.append(line[0])
            state_change.append(int(line[4]))
    state_change = list(reversed(state_change))
    state_year = list(reversed(state_year))

    # plotting this shit, doesnt work though
    # data isnt sorted on y axis

    xs = state_year
    ys = state_change
    
    plt.title(f"Death count from biggest % increase in deaths \nfrom Alzheimers in {state}")
    
    plt.xlabel("Years", rotation='vertical')
    plt.ylabel("Deaths") 
    plt.xticks(rotation='vertical')
    
    plt.bar(xs, ys)
    plt.show()
