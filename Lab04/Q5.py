"""
To convert the VaccumAgent to a model-based reflex agent, you need to maintain an internal state to keep track of the cleanliness status of each room. You can then update the agent's act method to consider the internal state while making decisions
"""
class ModelBasedReflexVaccumAgent():
    def __init__(self, model):
        self.model = model
        self.currentRoom = 1
        self.actions = ['clean', 'right', 'left']
        self.step = 1

    def updateModel(self, location, status):
        for room in self.model:
            if room['location'] == location:
                room['status'] = status

    def displayPerception(self):
        ''' display the current room and its status '''
        print(f"Perception at Step {self.step}:\nCurrent Room: {self.currentRoom}\nRoom Status: {self.model[self.currentRoom - 1]['status']}")

    def act(self):
        self.displayPerception()
        ''' return the action to be taken based on the current percept '''
        if self.model[self.currentRoom - 1]['status'] == 'dirty':
            self.updateModel(self.currentRoom, 'clean')
            action = 'clean'
        else:
            self.updateModel(self.currentRoom, 'clean')
            if self.currentRoom == len(self.model):
                self.currentRoom = 1
                action = 'left'
            else:
                self.currentRoom += 1
                action = 'right'
        self.step += 1
        return action

# Test
n_rooms = 5
model = [{'location': i + 1, 'status': 'dirty'} for i in range(n_rooms)]
modell = [{'location': 1, 'status': 'dirty'}, {'location': 2, 'status': 'clean'}, {'location': 3, 'status': 'dirty'}, {'location': 4, 'status': 'dirty'}, {'location': 5, 'status': 'dirty'}]
agent = ModelBasedReflexVaccumAgent(modell)
for i in range(10):
    print(agent.act())


# Converting the agent to the model-based reflex agent and took out the sensors and perceptions away from the agent.
# The agent now has an internal model of the environment and uses it to decide its actions.
# # Does your agent still work fine? Explain why.    

""" 
The provided code does not rely on any sensors or perceptions. It uses the internal model of the agent to 
determine the state of each room and decide its actions. 
The agent's model is pre-populated with room status information and gets updated as the agent performs actions.
The code will work fine in this specific scenario since it's a simple, 
deterministic environment where the agent only needs to clean the rooms in a linear sequence. 
However, in more complex or dynamic environments, the lack of sensors or 
perceptions would limit the agent's ability to adapt to changes or uncertainties.
In those cases, incorporating sensor data into the agent's logic would be necessary to make 
better decisions and adapt to the environment's changes. But for this simple vacuum cleaner example, 
the code will work as intended without the need for sensors.
"""




# Explanation of the code
"""
Initialization: The agent initializes its internal model with n_rooms, where each room has a location and a 'dirty' status. 
The agent starts in room 1 and sets its available actions to 'clean', 'right', and 'left'.
Updating the model: The agent updates its internal model when it cleans a room or moves to another room.
Displaying the perception: The agent displays the current room and its status at each step.
Acting: The agent decides which action to take based on its internal model. 
If the current room is dirty, it cleans the room. If the room is clean, 
it moves to the next room (right) or returns to the first room (left) if it's the last room.
To test the agent, create an instance with the desired number of 
rooms and execute the act() method for a certain number of iterations:
This code snippet represents a simple, model-based reflex agent that does not use sensors to perceive its environment. 
Instead, it relies on its internal model to make decisions and update room statuses.
"""

"""
The act method in the code is responsible for deciding the action the ModelBasedReflexVaccumAgent should take based on the current state of the environment (represented by the internal model)
Check if the current room ('status') is dirty:

if self.model[self.currentRoom - 1]['status'] == 'dirty':

If the room is dirty, update the model to set the room's status to 'clean', and set the action to 'clean':

    self.updateModel(self.currentRoom, 'clean')
    action = 'clean'

If the room is not dirty (i.e., it's clean), update the model to ensure the room's status is 'clean':
else:
    self.updateModel(self.currentRoom, 'clean')

If the agent is in the last room (i.e., the length of the model), set the current room to the first room (1) and set the action to 'left':

    if self.currentRoom == len(self.model):
        self.currentRoom = 1
        action = 'left'

If the agent is not in the last room, increment the current room by 1 and set the action to 'right':

    else:
        self.currentRoom += 1
        action = 'right'

Increment the step counter by 1:

self.step += 1

Call the displayPerception method to display the current room and its status:
self.displayPerception()

Return the decided action
"""

"""
The agent uses this internal model to decide its actions based on the current room and its status. 
For example, if the agent is in Room 1 and its status is 'dirty', the agent will clean the room and update the model accordingly. 
The agent also uses the model to decide whether to move right or left, depending on the current room's position within the model.
This model-based approach allows the agent to make decisions without directly sensing the environment, as it relies on the internal 
model to represent the state of the environment. However, this also means that the agent might not be well-suited for environments with 
dynamic changes or uncertainties, as it relies solely on the pre-defined and updated model to make decisions.
"""
    
    
""" Is a full observable
  A simple reflex agent acts only based on the current percept, ignoring the percept history. 
  In the context of the vacuum cleaner problem, a simple reflex agent would take actions based on the current location and the dirt status of the room it's in. 
"""

"""
A model-based reflex agent, on the other hand, can handle partially observable environments by maintaining an internal state based on the percept history. 
In the case of the vacuum cleaner problem, a model-based reflex agent could keep track of the cleanliness status of each room
"""
