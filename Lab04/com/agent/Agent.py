# abstract agent class

from abc import abstractmethod


class Agent(object):
    '''
    classdocs
    '''


    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def sense(self,environment):
        pass

    @abstractmethod
    def act(self):
        pass

    # here all the methods are abstract methods, so they must be implemented in the derived class.