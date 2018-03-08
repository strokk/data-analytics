#Guilherme Paes - Feb 2018
#Program that reads iris data and is nicely formatted

with open("iris.csv") as f:
    for line in f:
        line = line.replace(',', ' ')
        line = line.rstrip()
        print(line[:11], line[12:16].strip())