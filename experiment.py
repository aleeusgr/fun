import random 
import statistics

print('Simulation for probablitiy of #HEADS in a sequence of fair coin tosses')
def experiment(l=2,n=100,h=1):
    '''simulate a sequence of fair coin tosses
    
    l: int, length of sequence
    n: int, number of experiments to run
    h: int, number of HEADs in the sequence
    returns: float, fraction of desired outcomes to number of experiments'''
    outcome=0
    for i in range(n):
        series = ''
        for n in range(l):
            series+=random.choice(['H','T'])
    if series.count('H')==h:
        outcome+=1
    return outcome/n
       
exp =int( input('Number experiment to run: '))
n =  int( input('number tries in an experiment: '))
l =  int( input('length of a sequence: '))
h =  int( input('How many HEADs?: '))

data = []
for _ in range(exp):
    data.append(experiment(l,n,h))
print(statistics.mean(data))
    
