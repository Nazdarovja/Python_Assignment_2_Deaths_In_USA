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
    
 # state_with_most_deaths_in_2016()

 # 1 Which state has the least deaths in the year of 2016? (All causes)

def state_with_least_deaths_in_2016():
    
    state = ""
    current_least_deaths = 100000000000
    for line in reader:
        if line[3] != 'United States' and line[0] == '2016' and line[2] == 'All causes' and int(line[4]) < current_least_deaths:
            current_least_deaths = int(line[4])
            state = line[3] 
    print(state, current_least_deaths)

  
# state_with_least_deaths_in_2016()




