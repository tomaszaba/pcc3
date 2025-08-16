# ==============================================================================
#                                   Chapter 9                        
#                                   Classes
# ==============================================================================

## ---- Define a Class ---------------------------------------------------------

class Restaurant:
    """ A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Return the name of the restaurant and cuisine type"""
        x = f"Welcome to {self.restaurant_name}. Here we serve {self.cuisine_type}"
        return x.title()

    def open_restaurant(self):
        """Indicate whether the restaurant is open"""
        x = f"Restaurant {self.restaurant_name} is open"
        return x.title()

### Set a defined class instance and apply a method ----------------------------
restaurant = Restaurant("porta di roma", "pizzaria")
restaurant.cuisine_type
restaurant.restaurant_name

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant(
    restaurant_name="Galaxi",
    cuisine_type="Indian"
)

print(restaurant2.describe_restaurant())
print(restaurant2.open_restaurant())

## ---- A class about users ----------------------------------------------------

class User:
    """An attempt to describe my App users."""

    def __init__(self, first_name, last_name, age):
        """User's name."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        """Describe my users."""
        user = f"Hi, my name is {self.first_name.title()} {self.last_name.title()} and I am {int(self.age)}"
        return user


user = User("Tomás", "Zaba", "32")
user.age
user.describe_user()


## ---- Modifying attributes's values ------------------------------------------

class Restaurant:
    """A simple model of a program about restaurants."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Return a description of the restaurant."""
        desc = (
            f"This is {self.restaurant_name} serving {self.cuisine_type} cuisine.\n"
            f"We have served {self.number_served} clients today."
        )
        return desc

    def set_number_served(self, number_served):
        """Set the number of clients served."""
        self.number_served = number_served
        return f"Today we've served {self.number_served} clients."

    def increment_number_served(self, new):
        """Increase the number of clients served."""
        self.number_served += new
        desc = f"This car has {self.number_served} miles"
        return desc
        
rest = Restaurant("Ciao Bella", "Italian")
rest.number_served
rest.describe_restaurant()
rest.set_number_served(12)
rest.number_served = 50
rest.increment_number_served(2000)

## ---- Methods for a Child Class ----------------------------------------------

class Restaurant:
    """A simple model of a program about restaurants."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Return a description of the restaurant."""
        desc = (
            f"This is {self.restaurant_name} serving {self.cuisine_type} cuisine."
            f"\nWe have served {self.number_served} clients today."
        )
        return desc

    def set_number_served(self, number_served):
        """Set the number of clients served."""
        self.number_served = number_served
        return f"Today we've served {self.number_served} clients."

    def increment_number_served(self, new):
        """Increase the number of clients served."""
        self.number_served += new
        desc = f"This car has {self.number_served} miles"
        return desc

class ModernRestaurant(Restaurant):
    """ Represent aspects of modern restaurants."""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.restaurant_drinks = "cocktails"
    
    def get_drink_type(self):
        print(f"Here we serve {self.restaurant_drinks}")


modern_restaurant = ModernRestaurant("Bologna", "Roman")
modern_restaurant.describe_restaurant()
modern_restaurant.get_drink_type()

