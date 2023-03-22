
### This class represents a room in the hotel. It has a location and a status.


# Room is a class that is inherited from the object class.
class Room: 
    def __init__(self,location,status="dirty"):  # status here is a default parameter with a default value of "dirty"
        self.location = location    
        self.status = status    # status is a string that is either "dirty" or "clean"
        # default status is dirty
