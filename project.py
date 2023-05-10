import random

class Environment(Object):
    def __init__(self):
# There are 3 areas, A,B,C
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
        # if sprayer is in Area 'A'
        if sprayLocation==0:
            print("Sprayer is moved to Area A")
            # If area 'A' is infected
            if Environment.locationcondition['A']==1:
                print("Area 'A' is INFECTED")
            # Spray() and make it clean
                Environment.locationcondition['A']==0;
                print("Area 'A' has been DISINFECTED")
            # If area 'B' is infected
            if Environment.locationcondition['B']==1:
                print("Area 'B' is INFECTED")
            # Spray() and make it clean
                Environment.locationcondition['B']==0;
                print("Area 'B' has been DISINFECTED")
            # If area 'C' is infected
            if Environment.locationcondition['C']==1:
                print("Area 'C' is INFECTED")
            # Spray() and make it clean
                Environment.locationcondition['C']==0;
                print("Area 'C' has been DISINFECTED")