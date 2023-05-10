import random
import time

class Environment(object):
    def __init__(self):
        self.locationCondition = {'A': '0', 'B': '0'}
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)


class SimpleReflexsprayAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        Score = 0
        sprayLocation = random.randint(0, 1)
        if sprayLocation == 0:
            print ("spray is randomly placed at Location A.")
            print ("Location A is INFECTED.") if Environment.locationCondition['A'] == 1 else print("Location A is DISINFECTED.")
            if Environment.locationCondition['A'] == 1:
                Environment.locationCondition['A'] = 0
                Score += 1
                print ("Location A has been DISINFECTED.") 
            print ("Moving to Location B...")
            print ("Location B is INFECTED.") if Environment.locationCondition['B'] == 1 else print("Location B is DISINFECTED.")
            if Environment.locationCondition['B'] == 1:
                Environment.locationCondition['B'] = 0;
                Score += 1
                print ("Location B has been DISINFECTED.")
            print("Environment is DISINFECTED.")
                
        elif sprayLocation == 1:
            print ("spray randomly placed at Location B.")
            print ("Location B is INFECTED.") if Environment.locationCondition['B'] == 1 else print("Location B is DISINFECTED.")
            if Environment.locationCondition['B'] == 1:
                Environment.locationCondition['B'] = 0
                Score += 1
                print ("Location B has been DISINFECTED.")
            print ("Moving to Location A...")
            print ("Location A is INFECTED.") if Environment.locationCondition['A'] == 1 else print("Location A is DISINFECTED.")
            if Environment.locationCondition['A'] == 1:
                Environment.locationCondition['A'] = 0;
                Score += 1
                print ("Location A has been DISINFECTED.")
            print("Environment is DISINFECTED.")    
            
        print (Environment.locationCondition)
        print ("Performance Measurement: " + str(Score))


theEnvironment = Environment()
thespray = SimpleReflexsprayAgent(theEnvironment)