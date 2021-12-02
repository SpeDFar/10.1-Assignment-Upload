# Spencer Farley
# 10.1: Your Own Class
# This code implements a class to mimic a real-world object.

# import random, need this for many functions in this project.
import random

class Human:
    # Class variable
    __has_brain = True

    # init
    def __init__(self, name=None, personality=None, age=random.randint(0, 90)):
        # Declare self variables--ENCAPSULATION
        self.__name = str(name).title()
        self.__personality = str(personality).lower()
        try:
            if age >= 0:
                self.__age = int(age)
            else:
                print("Age input is not accepted, setting age to a random positive integer...")
                self.__age = random.randint(0, 90)
        except:
            print("Age input is not accepted, setting age to a random positive integer...")
            self.__age = random.randint(0, 90)

    # get/set functions
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = str(name).title()
    
    def get_personality(self):
        return self.__personality
    
    def set_personality(self, personality):
        self.__personality = str(personality).lower()
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        try:
            if age >= 0:
                self.__age = int(age)
            else:
                print("Unable to set age to this input. Must be a positive int or float.")
        except:
            print("Unable to set age to this input. Must be a positive int or float.")

    def get_brain(self):
        return self.__has_brain

    def get_human(self):
        # Return a string describing our human.
        return f"{self.get_name()}, is {self.get_personality()}, and is {self.get_age()} year(s) old."

    # Randomizes names, personalities, and ages
    def random_name(self):
        # Randomize name using a list of names and selecting using random module.
        names = ['Ben', 'Frederick', 'Rich', 'Ashley', 'Kevin', 'Bacon', 'Alice', 'Shelby', 'Megan']
        self.set_name(names[random.randint(0, len(names)-1)])

    def random_personality(self):
        # Randomize personality using a list of personalities and selecting one using random module.
        personalities = ['rude', 'chipper', 'moody', 'quirky', 'kind', 'boisterous']
        self.set_personality(personalities[random.randint(0, len(personalities)-1)])

    def random_age(self):
        # Randomize age using random module.
        self.set_age(random.randint(0, 90))

    # Randomize human
    def random_human(self):
        """This method randomizes a human by randomly selecting the name, personality, and age of a human. It then returns get_human for each of those values."""
        # User our random functions above to randomize self variables
        self.random_name()
        self.random_personality()
        self.random_age()
        return self.get_human()

    def human_position(self):
        """Create a human and have them walk around a city."""
        # Create a name or randomize one
        self.__name = input("Input a name or random >>> ")
        if self.__name == "random":
            self.random_name()
        # Set initial coords
        coord_a = random.randint(-3, 3)
        coord_b = random.randint(-3, 3)
        print(f"{self.__name} is walking around a city. They just left their house at coordinates ({coord_a}, {coord_b}). Where will they go?")
        while True:
            # Get user input for direction person is going or exit.
            user_input = input(f"Your inputs are north, south, east, or west, or 'exit' to leave. >>> ")
            # if and elif statements to process user input.
            if user_input == "north" or "south" or "east" or "west" or "exit":
                # Go north
                if user_input == "north":
                    # If user input would cause human to walk beyond the city border, reject input.
                    if coord_b >= 3:
                        print(f"The boundaries of the city are to the {user_input}, {self.__name} is unable to leave. Please try another input.")
                        continue
                    # If user input acceptable, add or subtract one from the associated axis.
                    else:
                        coord_b += 1
                        print(f"{self.__name} is now at coordinates ({coord_a}, {coord_b}).")
                        continue
                # Go south
                elif user_input == "south":
                    if coord_b <= -3:
                        print(f"The boundaries of the city are to the {user_input}, {self.__name} is unable to leave. Please try another input.")
                    else:
                        coord_b -= 1
                        print(f"{self.__name} is now at coordinates ({coord_a}, {coord_b}).")
                        continue
                # Go east
                elif user_input == "east":
                    if coord_a >= 3:
                        print(f"The boundaries of the city are to the {user_input}, {self.__name} is unable to leave. Please try another input.")
                        continue
                    else:
                        coord_a += 1
                        print(f"{self.__name} is now at coordinates ({coord_a}, {coord_b}).")
                        continue
                # Go west
                elif user_input == "west":
                    if coord_a <= -3:
                        print(f"The boundaries of the city are to the {user_input}, {self.__name} is unable to leave. Please try another input.")
                        continue
                    else:
                        coord_a -= 1
                        print(f"{self.__name} is now at coordinates ({coord_a}, {coord_b}).")
                        continue
                # Exit option
                elif user_input == "exit":
                    print("Exiting...")
                    break
            # If user input is not recognized as an acceptable input, reject user input.
            print("Input not accepted, please try again.")

def main():
    # Create human, will also randomize age if nothing is inputted, but will make name None and personality None if no inputs.
    human1 = Human('Daniel', 'boisterous', 10)
    # Gets the name of human (Daniel). Also capitolizes input
    print(human1.get_name())
    # Gets the personality of human (boisterous). Also lowers the input
    print(human1.get_personality())
    # Gets the age of human
    print(human1.get_age())
    # Gets whether or not human has a brain for displaying class variable
    print(human1.get_brain())
    # Displays all info about human
    print(human1.get_human())


    # human2 doesn't need any inputs since we are going to randomize them
    human2 = Human()
    # Gives human2 a random name, personality, and age. Returns a string describing human2
    print(human2.random_human())

    # Displaying set functions. Will capitolize name and lower personality if inputs aren't already so.
    human2.set_name('benjamin')
    human2.set_personality('Rowdy')
    human2.set_age(32)
    human2.set_age('d')

    # Display all info about human2 again
    print(human2.get_human())

    # Creates human3 to use human_position()
    human3 = Human()
    # A game allowing a human with either a random name or inputted name to wander around a city at the user's control. Restricts user to a grid with axes going from -3 to 3.
    human3.human_position()

if __name__ == "__main__":
    main()