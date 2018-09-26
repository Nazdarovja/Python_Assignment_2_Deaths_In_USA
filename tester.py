import collections
import numpy as np
import utility

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
    print(collections.Counter.most_common(increase_per_state)[0])
    # print(increase_per_state)

smallest_increase_from_1999_2016()


  




