"""
To convert the VaccumAgent to a model-based reflex agent, you need to maintain an internal state to keep track of the cleanliness status of each room. You can then update the agent's act method to consider the internal state while making decisions
"""

import time
from com.environment import Environment
from com.environment import Room
from com.agent import Agent

class NRoomVaccumCleanerEnvironment(Environment.Environment):
    def __init__(self, agent, rooms=2):
        self.rooms = rooms
        self.rooms = [Room.Room(i, 'dirty') for i in range(1, rooms+1)]
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay(1000)
        self.step = 1
        self.action = ""
        self.score = 0  # Initialize the score

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            res = self.agent.act()
            self.action = res

            if res == "clean":
                if self.currentRoom.status == "dirty":
                    self.score += 25  # Add 25 points for cleaning a dirty room
                    print("Adding 25 points: Cleaned a dirty room")
                self.currentRoom.status = "clean"
            elif res == "right":
                self.score -= 1  # Subtract 1 point for moving from a room
                print("Subtracting 1 point: Moved from a room")
                if self.currentRoom == self.rooms[-1]:
                    self.currentRoom = self.rooms[0]
                else:
                    self.currentRoom = self.rooms[self.rooms.index(self.currentRoom) + 1]
            elif res == "left":
                self.score -= 1  # Subtract 1 point for moving from a room
                print("Subtracting 1 point: Moved from a room")
                if self.currentRoom == self.rooms[0]:
                    self.currentRoom = self.rooms[-1]
                else:
                    self.currentRoom = self.rooms[self.rooms.index(self.currentRoom) - 1]

            if self.currentRoom.status == "dirty":
                self.score -= 10  # Subtract 10 points if the current room is dirty
                print("Subtracting 10 points: Current room is dirty")

            self.displayAction()
            self.step += 1
            time.sleep(self.delay_time / 1000)
            self.displayScore()  # Display the score after each action

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

    def displayScore(self):
        print(f"Agent's score at step {self.step}: {self.score}")
        
        
        

"""
class ModelBasedReflexVacuumAgent(Agent.Agent):
    def __init__(self):
        self.previous_action = "clean"

    def act(self):
        if self.previous_action == "clean":
            next_action = "right"
        elif self.previous_action == "right":
            next_action = "clean"
        else:
            next_action = "clean"

        self.previous_action = next_action
        return next_action
    """

class ModelBasedReflexVaccumAgent(Agent.Agent):
    def __init__(self):
        self.room_status = {}

   # def sense(self, environment):
    #    self.environment = environment  # store the environment
      #  location = self.environment.currentRoom.location
     #   status = self.environment.currentRoom.status
       # self.room_status[location] = status

    def act(self):
        location = self.environment.currentRoom.location
        status = self.environment.currentRoom.status

        if status == "dirty":
            return "clean"
        else:
            next_location = (location + 1) % len(self.environment.rooms)
            if self.room_status.get(next_location, None) != "clean":
                return "right"
            else:
                return "left"
            
     """
     This agent will not work properly, as it cannot update its internal state based on the environment's actual state. 
     The agent's decisions will be based on the initial, incomplete knowledge of the environment, which may not be accurate. 
     Since the agent cannot perceive the environment, it cannot update its internal model, and its performance will degrade.
     In conclusion, taking the sensors away from a model-based reflex agent will prevent it from working effectively because it cannot maintain an accurate internal model of the environment.
     """
            

if __name__ == "__main__":
    agent = ModelBasedReflexVaccumAgent()
    environment = NRoomVaccumCleanerEnvironment(agent, 10)
    environment.executeStep(10)
    print(f"Agent's score: {environment.score}")
    
    
    
  """ Is a full observable
  A simple reflex agent acts only based on the current percept, ignoring the percept history. 
  In the context of the vacuum cleaner problem, a simple reflex agent would take actions based on the current location and the dirt status of the room it's in. 
  """

"""
A model-based reflex agent, on the other hand, can handle partially observable environments by maintaining an internal state based on the percept history. 
In the case of the vacuum cleaner problem, a model-based reflex agent could keep track of the cleanliness status of each room
"""
