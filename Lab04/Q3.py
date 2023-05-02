# Does not have a stopping condition, It will continue to clean the rooms even if the rooms are already clean, 
# It depends on the number of steps specified in the execute method.

# Yes we can make it stop by modifying the execute method in the Environment class to check if the rooms are clean or not.
# Then in execute method we can modify the for loop to stop when all the rooms are clean.

def act(self):
        ''' This method returns an action to take based on the current perception of the environment. '''
        if all(room.status == "clean" for room in self.environment.rooms):
            return "stop" # if all rooms are clean, return "stop"
        elif self.perception == "dirty":
            return "clean" # if the current room is dirty, return "clean"
        else:
            return "right" # if the current room is clean, move to the room on the right
        

# Another way: modify the execute all function :

def executeAll(self):
    while any(room.status == "dirty" for room in self.rooms):
        self.executeStep()


#  Its not rational because it doesnt take the long term consequences into account.

# the agent is somewhat rational, as it tries to clean the rooms and move to the next one. 
# However, the agent's decision-making process could be improved by considering more factors, 
# like the number of dirty rooms or the overall efficiency of its actions. 
# The current implementation is a simple reflex agent, which only reacts to the current room's status and does not consider the overall state of the environment.
# A more rational agent would take into account the entire environment and choose actions accordingly.




        

