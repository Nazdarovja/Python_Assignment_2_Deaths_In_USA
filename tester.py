import collections
import numpy as np
import utility
import matplotlib.pyplot as plt

reader = utility.readFile() # data

# 1 Which state has the most deaths in the year of 2016? (All causes)

def state_with_most_deaths_in_2016():
    arr = np.array(reader)
    list_of_states = arr[(arr[:,0] == "2016") & (arr[:,2] == "All causes") & (arr[:,3] != "United States")]  # find correct list of states
    result_state = list_of_states[list_of_states[:,4] == np.max(list_of_states[:,4].astype(int)).astype(str)][0]       # fint largest deaths number in a states & find state with this death number
    print(result_state[3] + ": "+result_state[4])


 # 2 Which state has the least deaths in the year of 2016? (All causes)

def state_with_least_deaths_in_2016():
    arr = np.array(reader)
    list_of_states = arr[(arr[:,0] == "2016") & (arr[:,2] == "All causes") & (arr[:,3] != "United States")]  # find correct list of states
    result_state = list_of_states[list_of_states[:,4] == np.min(list_of_states[:,4].astype(int)).astype(str)][0]       # fint largest deaths number in a states & find state with this death number
    print(result_state[3] + ": "+result_state[4])


# 3 Which state has had the smallest increase in deaths from 1999-2016? (All causes)

def smallest_increase_from_1999_2016():
    deaths_2016 = []
    deaths_1999 = []
    increase_per_state = {}
    for line in reader:
        if line[3] != 'United States' and line[0] == '2016' and line[2] == 'All causes':
            deaths_2016.append({'state': line[3], 'deaths': int(line[4])})
        if line[3] != 'United States' and line[0] == '1999' and line[2] == 'All causes':
            deaths_1999.append({'state': line[3], 'deaths': int(line[4])})
    for i in range(0, len(deaths_1999)):
        state = deaths_1999[i]['state']
        increase = (deaths_2016[i]['deaths'] / deaths_1999[i]['deaths']) * 100 - 100
        increase_per_state[state] = increase
    print(collections.Counter.most_common(increase_per_state)[-1])
    # print(increase_per_state)

# 4 Which state has the most deaths caused by kidney disease in the year of 2005?

def state_with_most_deaths_by_kidneydisease_2005(): # samme struktur som opg 1 - kan lave en generisk
    state = ""
    current_most_deaths = 0
    for line in reader:
        if line[3] != 'United States' and line[0] == '2005' and line[2] == 'Kidney disease' and int(line[4]) > current_most_deaths:
            current_most_deaths = int(line[4])
            state = line[3]
    print(state, current_most_deaths)

# 5 Which state has had the biggest increase in the death of Alzheimers from 1999-2016?
#  Plot the increase year for year using matplotlib

def state_with_biggest_increase_of_alzheimers_1999_to_2016_plot():

    # Finding out which state has had the biggest increase...

    deaths_2016 = []
    deaths_1999 = []
    increase_per_state = {}
    for line in reader:
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
    for line in reader:
        if line[3] == state and line[2] == "Alzheimer's disease":
            state_year.append(line[0])
            state_change.append(line[4])
    state_change = list(reversed(state_change))
    state_year = list(reversed(state_year))

    # plotting this shit, doesnt work though
    # data isnt sorted on y axis

    xs = range(1, 19)
    ys = state_change
    plt.title(f"Change over Alzheimers in {state}")
    plt.xlabel("Years")
    plt.ylabel("Frequency of deaths") 
    plt.xticks(xs, state_year, rotation='vertical')
    plt.bar(xs, ys)
    plt.show()


state_with_most_deaths_in_2016()
state_with_least_deaths_in_2016()
smallest_increase_from_1999_2016()
state_with_most_deaths_by_kidneydisease_2005()
state_with_biggest_increase_of_alzheimers_1999_to_2016_plot()

  




