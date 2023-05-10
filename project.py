import random

class Environment(object):
    def __init__(self):
# There are 4 areas, A,B,C,D
# 1 indicates infected 
# 0 indicates clean area
        self.locationcondition= { 'A' : '0', 'B' : '1'} #'C': '1', 'D' : 1

self.locationcondition['A']=random.randint(0,1)
self.locationcondition['B']=random.randint(0,1)
# self.locationcondition['C']=random.choice(0,1)
# self.locationcondition['D']=random.choice(0,1)

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
                # # If area 'C' is infected
                #     if Environment.locationcondition['C']==1:
                #         print("Area 'C' is INFECTED")
                #     # Spray() and make it clean
                #         Environment.locationcondition['C']==0;
                #         print("Area 'C' has been DISINFECTED")
                #     # If area 'D' is infected
                #         if Environment.locationcondition['D']==1:
                #             print("Area 'D' is INFECTED")
                #         # Spray() and make it clean
                #             Environment.locationcondition['D']==0
                #             print("Area 'D' has been DISINFECTED")
        else:
            # Moving sprayer to Area 'B'
            print("Moving to area 'B'")
            if Environment.locationcondition['B']==1:
                print("Area 'B' is INFECTED")
            # Spray() and make it clean
                Environment.locationcondition['B']==0;
                print("Area 'B' has been DISINFECTED")

                print("***********");
        

            elif sprayLocation==1:
                print("Sprayer is moved to Area B")
                # If area 'B' is infected
                if Environment.locationcondition['B']==1:
                    print("Area 'B' is INFECTED")
                # Spray() and make it clean
                    Environment.locationcondition['B']==0;
                    print("Area 'A' has been DISINFECTED")
                # If area 'A' is infected
                    if Environment.locationcondition['A']==1:
                        print("Area 'A' is INFECTED")
                    # Spray() and make it clean
                        Environment.locationcondition['A']==0;
                        print("Area 'A' has been DISINFECTED")
            else:
            # Moving sprayer to Area 'A'
                print("Moving to area 'A'")
            if Environment.locationcondition['A']==1:
                print("Area 'A' is INFECTED")
            # Spray() and make it clean
                Environment.locationcondition['A']==0;
                print("Area 'A' has been DISINFECTED")

                print("***********");


print(Environment.locationcondition)
theEnvironment = Environment()
theSpray = simplexAgent()