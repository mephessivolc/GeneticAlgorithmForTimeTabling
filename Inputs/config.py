import csv
import random
import math

def show(conjunto):
    for i in conjunto:
        print(i)

def read_file(name="Inputs/timetabling.csv"):
    with open(name, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=" ", quotechar=',')
        infos = []
        for row in csvreader:
            tmp = [row[0]]
            for i in row[1:]:
                tmp.append(int(i))  
            
            infos.append(tmp)

    return infos