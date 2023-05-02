import time
from com.environment import Environment
from com.environment import Room
from com.agent import Agent

class NRoomVaccumClearnerEnvironment(Environment.Environment):
    def __init__(self, agent, rooms=2):
        self.rooms = rooms # number of rooms
        self.rooms = [Room.Room(i, 'dirty') for i in range(1, rooms+1)] # initialize rooms 1 to n with status dirty
        self.agent = agent # agent is an instance of Agent.Agent
        self.currentRoom = self.rooms[0] # current room is room 1
        self.delay(1000) # delay in milliseconds
        self.step = 1 # step counter
        self.action = "" # action taken by agent

    def executeStep(self,n=1):
        for _ in range(0,n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            if res == "clean":
                self.currentRoom.status = "clean"
            elif res == "right":
                if self.currentRoom == self.rooms[-1]:
                    self.currentRoom = self.rooms[0]
                else:
                    self.currentRoom = self.rooms[self.rooms.index(self.currentRoom)+1] # move to the room on the right , index() returns the index of the room in the list
            elif res == "left":
                if self.currentRoom == self.rooms[0]:
                    self.currentRoom = self.rooms[-1]
                else:
                    self.currentRoom = self.rooms[self.rooms.index(self.currentRoom)-1]
            
            self.displayAction()
            self.step += 1
            time.sleep(self.delay_time/1000)

    def executeAll(self):
            ''' execute the environment until all rooms are clean '''
            raise NotImplementedError('action must be defined!')
        
    def displayPerception(self):
            ''' display the current room and it's status '''
            print(f"Perception at Step {self.step}:\nCurrent Room: {self.currentRoom.location}\nRoom Status: {self.currentRoom.status}")
        
    def displayAction(self):
            print("------- Action taken at step %d is [%s]" %(self.step,self.action))
        
    def delay(self,n=1000):
            ''' delay in milliseconds '''
            self.delay_time = n  

class VaccumAgent(Agent.Agent):

    def __init__(self):
        pass

    def sense(self,environment):
        self.environment = environment # store the environment

    def act(self):
        if self.environment.currentRoom.status == "dirty":
            return "clean"
        else:
            if self.environment.currentRoom == self.environment.rooms[-1]:
                return "left"
            else:
                return "right"
            
if __name__ == "__main__":
    agent = VaccumAgent()
    environment = NRoomVaccumClearnerEnvironment(agent, 10)
    environment.executeStep(10)





""" Explaination:
The NRoomVaccumClearnerEnvironment class represents an environment with N rooms for a vacuum cleaner agent to navigate and clean. 
Here's a step-by-step explanation of how the environment and the executeStep method work:

1. The constructor __init__ initializes the environment with the given agent and number of rooms (default is 2). 
It creates a list of Room objects with 'dirty' status, sets the current room to the first one, initializes the step counter and action, and sets a delay.

2. The executeStep method takes an optional parameter n (default is 1) and executes the agent's actions and updates the environment n times.
For each iteration: 
a. Call displayPerception to display the current room and its status. 
b. Call the agent's sense method and pass the environment, allowing the agent to access the environment's information. 
c. Call the agent's act method to get the agent's action based on the current room's status (clean, move right, or move left). 
d. Update the environment based on the agent's action:

If the action is "clean", set the current room's status to "clean".
If the action is "right", move the agent to the next room in the list or wrap around to the first room if it's the last room.
If the action is "left", move the agent to the previous room in the list or wrap around to the last room if it's the first room. 

e. Call displayAction to display the action taken by the agent at each step. 
f. Increment the step counter. g. Sleep for the specified delay time (in milliseconds) to simulate the passage of time.

The executeStep method allows the agent to interact with the environment and perform actions to clean the rooms. By calling this method with different values of n, 
you can control how many steps the agent takes in the environment.

In the __main__ block, an instance of the VaccumAgent is created, and an instance of the NRoomVaccumClearnerEnvironment with 10 rooms is created. Then, 
the executeStep method is called with n=10, which means the agent will perform actions for 10 steps in the environment.


"""