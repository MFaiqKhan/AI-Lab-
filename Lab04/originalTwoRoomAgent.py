# These are import statements that bring in code from other modules. 
# The Environment, Room, and Agent classes are imported from their respective modules.
import time

from com.environment import Environment
from com.environment import Room
from com.agent import Agent


#subclass that extend the Environment class
class TwoRoomVaccumCleanerEnvironment(Environment.Environment):
    ''' classdocs '''

    def __init__(self, agent):
        ''' This is the constructor for the TwoRoomVaccumCleanerEnvironment class. 
        It initializes the two rooms (r1 and r2), sets the agent that will act in the environment (agent), 
        sets the initial room (currentRoom) to r1, delays for 1000 milliseconds, 
        and initializes some other variables (step and action). 
        ''' 

        self.r1 = Room.Room('A', 'dirty') # initialize room A
        self.r2 = Room.Room('B', 'dirty') # initialize room B

        self.agent = agent # agent is an instance of Agent.Agent
        self.currentRoom = self.r1 # current room is room A
        self.delay(1000) # delay in milliseconds
        # why delay is needed?  # to slow down the execution of the program so that we can see the output

        self.step = 1 # step counter
        self.action = "" # action taken by agent

        # above are the environment variables

    def executeStep(self,n=1):
            ''' This defines a method called executeStep, which runs the environment for a specified number of steps 
            (default is 1 step). It loops through the specified number of steps, displaying the current room and 
            its status, sensing the environment with the agent, having the agent act based on its perception, 
            updating the action taken, and displaying the action. The if/elif statements update the status of the 
            current room based on the action taken by the agent, and the step counter is incremented. 
            '''
            
            for _ in range(0,n): # _ is used to indicate that the variable is not used in the loop
            # using an underscore in this way is a way to indicate to other programmers that the value is not important
                # e.g. for i in range(0,10): print(i) will print 0 to 9

                self.displayPerception() # display the room and it's status
                self.agent.sense(self) # calls the sense method of the agent object to get a perception of the current state of the environment
                res = self.agent.act() # agent acts on the environment
                # calls the act method of the agent object to perform an action based on the current perception
                self.action = res # store the action taken by the agent

                if res == "clean":
                    self.currentRoom.status = "clean"
                elif res == "right":
                    self.currentRoom = self.r2
                elif res == "left":
                    self.currentRoom = self.r1

                self.displayAction() # display the action taken by the agent
                self.step += 1 # increment the step counter by 1
                time.sleep(self.delay_time / 1000) # delay in seconds

        
    def executeAll(self):
            ''' execute the environment until all rooms are clean '''
            raise NotImplementedError('action must be defined!')
        
    def displayPerception(self):
            ''' display the current room and it's status '''
            print(f"Perception at Step {self.step}:\nCurrent Room: {self.currentRoom.location}\nRoom Status: {self.currentRoom.status}")
        
    def displayAction(self):
            print("------- Action taken at step %d is [%s]" %(self.step,self.action))
        
    def delay(self,n=100):
            ''' delay in milliseconds '''
            self.delay_time = n         


# subclass that extends the Agent class
class VaccumAgent(Agent.Agent):
    ''' classdocs '''

    def __init__(self):
        ''' Constructor '''
        pass

    def sense(self,environment):
        ''' sense the environment '''
        self.environment = environment # store the environment

    def act(self):
        ''' act on the environment '''
        if self.environment.currentRoom.status == "dirty":
            return "clean"
        elif self.environment.currentRoom.location == "A":
            return "right"
        return "left"
    

# main function
if __name__ == '__main__':
    agent = VaccumAgent() # create an instance of the VaccumAgent class
    environment = TwoRoomVaccumCleanerEnvironment(agent) # create an instance of the TwoRoomVaccumCleanerEnvironment class
    environment.executeStep(20) # execute the environment for 5 steps







