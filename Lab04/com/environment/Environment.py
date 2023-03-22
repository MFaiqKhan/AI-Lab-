from abc import abstractmethod # abstractmethod is a decorator that is used to declare abstract methods, 
# that is, methods that must be implemented in the derived class, but not in the base class. 
#The abstract method is defined by including the @abstractmethod decorator above the method definition.
 
class Environment(object): 
    # Environment is a class that is inherited from the object class.
    # object is the base class for all classes. It is the most base type in Python.
    # In Python 3.x, classes are implicitly derived from object,
    #  so you don't need to include it in the class definition. 
    ''''
        classdocs 
    '''

    @abstractmethod
    def __init__(self, n): 
        self.n = n  
        # n is an instance variable of the class Environment.
        # __init__ acts as a constructor for the class.
        # self is a reference to the current instance of the class, # here initialized an instance variable n.
        # and is used to access variables that belong to the class.


    def executeStep(self,n=1): 
        raise NotImplementedError('action must be defined!') 
        
        # executeStep is a method that takes a parameter n with a default value of 1.
        # raise is used to raise an exception. 
        # NotImplementedError means that the derived class must implement this method.



    def executeAll(self):
        raise NotImplementedError('action must be defined!')
        
        # executeAll is a method that takes no parameters.


    def delay(self,n=100):
        self.delay_time = n
        # delay is a method that takes a parameter n with a default value of 100.
        # sets delay of the environment to n.






# Path: Lab04\com\environment\environment.py


# what is a decorator?
# decorator is a function that takes another function and extends the behavior of the 
# latter function without explicitly modifying it.

# In Python, a decorator is a function that takes another function as an argument, 
# adds some functionality to it, and returns the modified function without changing its source code. 
# The @ symbol is used to apply a decorator to a function. Decorators can be used to modify the behavior of 
# functions or classes, add extra functionality, or to provide an alternative way of calling functions

# @abstractmethod is a decorator that is used to declare abstract methods, 
# that is, methods that must be implemented in the derived class, but not in the base class.