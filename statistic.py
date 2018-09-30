import numpy as np
from utility import csv2array



"""
 0            1                2          3        4                5
Year,   113 Cause Name,   Cause Name,   State,   Deaths,   Age-adjusted Death Rate
"""



def biggest_incr(array, f_year, t_year, cause='All causes'):
    """
        Returns the state with biggest increase in death in specified interval
        Args:
            numpy array: array with data
            int: from, year
            int: to, year
            str: cause (default=All causes)
        Returns:
            str: state
    """

    # raise error if f_year >= t_year
    if f_year >= t_year:
        raise ValueError('from year must be less then to year')

    # creates an array of unique states
    state_keys = np.unique(array[:,3])
    # but without 'United States'
    state_keys = state_keys[np.where(state_keys != 'United States')]

    # create masks which only consider the chosen years and cause
    f_mask = (array[:,0].astype(int) == f_year) & (array[:,2] == cause)
    t_mask = (array[:,0].astype(int) == t_year) & (array[:,2] == cause)

    # create arrays with sum of death for every state at both years
    f_death_per_state = np.array([np.sum(array[f_mask & (array[:,3] == state)][:,4].astype(int)) for state in state_keys])
    t_death_per_state = np.array([np.sum(array[t_mask & (array[:,3] == state)][:,4].astype(int)) for state in state_keys])

    # calculating the differens in death in the interval for every state
    diff_death_per_state = t_death_per_state - f_death_per_state

    # only show states with a increase (since the question mentions an increase, only 'positive' numbers)
    state_keys = state_keys[diff_death_per_state > 0]

    try:
        # find index of smallest positive number
        # (np.argmax() raises an ValueError if it gets an empty array)
        index_max_incr = np.argmax(diff_death_per_state[diff_death_per_state > 0])
        
        # print result (for exercise)
        print(f'State with biggest increase of deaths ({diff_death_per_state[diff_death_per_state > 0].max()}) from {f_year} to {t_year} is {state_keys[index_max_incr]} by {cause}')

        return state_keys[index_max_incr]
    except:
        # print result (for exercise)
        print(f'no state had an increase in death by {cause} from {f_year} to {t_year}')

        return None


def smallest_incr(array, f_year, t_year, cause='All causes'):
    """
        Returns the state with smallest increase in death in specified interval
        Args:
            numpy array: array with data
            int: from, year
            int: to, year
            str: cause (default=All causes)
        Returns:
            str: state
    """

    # raise error if f_year >= t_year
    if f_year >= t_year:
        raise ValueError('from year must be less then to year')

    # creates an array of unique states
    state_keys = np.unique(array[:,3])
    # but without 'United States'
    state_keys = state_keys[np.where(state_keys != 'United States')]

    # create masks which only consider the chosen years and cause
    f_mask = (array[:,0].astype(int) == f_year) & (array[:,2] == cause)
    t_mask = (array[:,0].astype(int) == t_year) & (array[:,2] == cause)

    # create arrays with sum of death for every state at both years
    f_death_per_state = np.array([np.sum(array[f_mask & (array[:,3] == state)][:,4].astype(int)) for state in state_keys])
    t_death_per_state = np.array([np.sum(array[t_mask & (array[:,3] == state)][:,4].astype(int)) for state in state_keys])

    # calculating the differens in death in the interval for every state
    diff_death_per_state = t_death_per_state - f_death_per_state

    # only show states with a increase (since the question mentions an increase, only 'positive' numbers)
    state_keys = state_keys[diff_death_per_state > 0]

    try:
        # (np.argin() raises an ValueError if it gets an empty array)
        # find index of smallest positive number
        index_min_incr = np.argmin(diff_death_per_state[diff_death_per_state > 0])

        # print result (for exercise)
        print(f'State with smallest increase of deaths ({diff_death_per_state[diff_death_per_state > 0].min()}) from {f_year} to {t_year} is {state_keys[index_min_incr]} by {cause}')

        return state_keys[index_min_incr]
    except:
        # print result (for exercise)
        print(f'No state had an increase in death by {cause} from {f_year} to {t_year}')

        return None


def state_with_most_deaths(arr, year, cause='All causes'):
    """
    Returns the state with highest amount of deaths
    Args:
        numpy array: array with data
        int: year
        str: cause (default=All causes)
    Returns:
        str: state
    """
    # find correct list of states
    list_of_states = arr[(arr[:,0] == str(year)) & (arr[:,2] == cause) & (arr[:,3] != "United States")]  

    # fint largest deaths number in a states & find state with this death number
    result_state = list_of_states[list_of_states[:,4] == np.max(list_of_states[:,4].astype(int)).astype(str)][0]       
    
    #print for assignment
    print(f'The state with most deaths from {cause}, in {year} was {result_state[3]} with {result_state[4]} deaths')
    
    return result_state

def state_with_least_deaths(arr, year, cause='All causes'):
    """
    Returns the state with least amount of deaths
    Args:
        numpy array: array with data
        int: year
        str: cause (default=All causes)
    Returns:
        str: state
    """
    # find correct list of states
    list_of_states = arr[(arr[:,0] == str(year)) & (arr[:,2] == cause) & (arr[:,3] != "United States")]  
    
    # fint largest deaths number in a states & find state with this death number
    result_state = list_of_states[list_of_states[:,4] == np.min(list_of_states[:,4].astype(int)).astype(str)][0]      
    
    #print for assignment
    print(f'The state with least deaths in 2016 was {result_state[3]} with {result_state[4]} deaths')
    
    return result_state