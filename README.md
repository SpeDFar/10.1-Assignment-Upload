Spencer Farley
10.1: Your Own Class - README
Read this before using the "your_own_class.py" file.

The Human class creates an object meant to mimic a human with 4 overall variables. The class variable __has_brain 
will always be 'True'. This variable can only be used to get its value. The other three variables, name, personality, 
and age, can be modified, randomized, and viewed. The name variable must have an input or it will be 'None', similarly 
to the personality variable. The age variable can take either one input or no inputs, randomizing the value if it 
receives no input. If the age variable receives an input that is not a positive float or int, the program prints an error 
and creates a random age.

The get_ methods are fairly self-explanatory. These methods return the value for their respective variables. get_name() 
returns the __name variable, get_personality() returns the __personality variable, and get_age() returns the __age variable. 
However, the set_ methods are a little different. The set_name() method takes an input, turns that input into a capitolized 
string, and set the __name variable to the string. set_personality() is similar, but it takes an input, turns that input into
a lower case string, and sets the __personality variable to the string. set_age() will only accept an int or float greater 
than or equal to 0 as an input, returning an error if the input is anything else. If set_age() receives a proper input, 
it will set the __age variable to the int() of the input.

The get_brain() method will always return 'True' because it returns the value of __has_brain. The get_human() method returns 
a string describing our human by stating their name, personality, and age. get_human() calls on get_name(), get_personality(), 
and get_age() to accomplish this. 

The random_ methods change data variables by randomly selecting a name or personality randomly from a list or randomly 
selecting an age from 0 to 90. All of these functions are accomplished using the random module. random_human() calls on 
random_name(), random_personality(), and random_age() to create a human. It then returns the get_human() function.

The human_position() function requests the user to input a name or input 'random' to get a random name using random_name(). 
It will then randomly choose a set of coordinates from -3 to 3 for each coordinate to determine a starting position. The 
program then states where the user starts and requests an input 'north', 'south', 'east', or 'west' to go that direction 
or to input 'exit' to exit the while loop. If the user inputs anything other than a proper input, the program prints an error 
and requests a new input and repeats this. If the user inputs 'north', 'south', 'east', or 'west', the program will add or 
subtract 1 from the associated coordinates and display the user's new position. The program the requests a new input unless 
the user's input would cause any coordinate to be greater than or less than 3 or -3 respecitively. The program will then 
print an error and request a new input. This cycle will loop until the user inputs 'exit'.

The demo program in main() first creates the object human1, with a name 'Daniel', personality 'boisterous', and age '10'. 
The program then prints human1's name, personality, age, and the __has_brain value. Then the program prints the get_human 
output. Then, the program creates the object human2 with no attributes, then randomizes their name, personality, and age. Then, the 
program prints human2's randomized name, personality, and age. The program now sets human2's name to 'benjamin', capitolizing the name, 
sets human2's personality to 'Rowdy', lower-casing the personality, sets human2's age to 32, and then sets human2's age to 'd', printing an 
error.
After this, the program creates human3, without any attributes, and running through the human_position() function. The user must give inputs
for this demo. See the human_position() explanation to know what this function does and how to navigate it or follow the instructions printed
by the program.

To use the demo program, simply run the program. Follow the printed text until you reach the prompt "Input a name or random >>> ". 
Then follow the instructions the program gives you.
