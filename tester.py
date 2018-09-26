import collections
import numpy as np
import utility
import matplotlib.pyplot as plt

reader = utility.readFile() # data

# 1 Which state has the most deaths in the year of 2016? (All causes)

def state_with_most_deaths_in_2016():
    state = ""
    current_most_deaths = 0
    for line in reader:
        if line[3] != 'United States' and line[0] == '2016' and line[2] == 'All causes' and int(line[4]) > current_most_deaths:
            current_most_deaths = int(line[4])
            state = line[3] 
    print(state, current_most_deaths)
    

 # 2 Which state has the least deaths in the year of 2016? (All causes)

def state_with_least_deaths_in_2016():
    
    state = ""
    current_least_deaths = 100000000000
    for line in reader:
        if line[3] != 'United States' and line[0] == '2016' and line[2] == 'All causes' and int(line[4]) < current_least_deaths:
            current_least_deaths = int(line[4])
            state = line[3] 
    print(state, current_least_deaths)


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

    state_year = []
    state_change = []
    for line in reader:
        if line[3] == state and line[2] == "Alzheimer's disease":
            state_year.append(line[0])
            state_change.append(line[4])
    state_change = list(reversed(state_change))
    state_year = list(reversed(state_year))

    xs = range(1, 19)
    ys = state_change
    plt.title(f"Change over Alzheimers in {state}", fontsize=16)
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("Frequency of deaths", fontsize=12) 
    plt.xticks(xs, state_year, rotation='vertical')
    plt.tight_layout(pad=2.0)
    plt.bar(xs, ys)
    plt.show()
    print("jsd")

state_with_biggest_increase_of_alzheimers_1999_to_2016_plot()

  




