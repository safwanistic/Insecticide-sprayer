import random

class Environment(Object):
    def __init__(self):
# There are 3 rooms, A,B,C
# 1 indicates infected 
# 0 indicates clean area
        self.locationcondition= {'A': '1','B': '0','C': '1', 'D' : 1}

self.locationcondition['A']=random.choice(0,1)
self.locationcondition['B']=random.choice(0,1)
self.locationcondition['C']=random.choice(0,1)
self.locationcondition['D']=random.choice(0,1)

class simplexAgent(Environment):
    def __init__(self, Environment):
        print(Environment.locationcondition)
        # Placing the sprayer at random location
        sprayLocation = random.randint(0,1)
        # if sprayer is in Room 'A'
        
