#I. DEFINING FUNCTIONS

#example
def greeting(name): #name is the parameter, here there is only one. then comes the body
    print("welcome, "+ name)#this is the body, it must be indented and can have many lines

greeting("Kay")
greeting("Cameron")
# the outputs are: "welcome, Kay" "welcome, Cameron"

#now more complex
def greeting1(name, department):#2 parameters
    print("Welcome, "+ name)
    print("You're part of the "+ department +" department")
#and it will print 2 seperate messages
greeting1("Blake","IT Support")
#output: "Welcome, Blake"
#"You're part of IT Support"
greeting1("Ellis", "Software engineering")

#POPQUIZ: Flesh out the body of the print_seconds function so that it prints
#the total amount of seconds given the hours, minutes, and seconds function
#parameters. Remember that there are 3600 seconds in an hour and 60 seconds
#in a minute.

def print_seconds(hours, minutes, seconds):
    print(3600*hours + 60*minutes + 1*seconds)

print_seconds(1,2,3)
#corect output: 3723

#RECAP: We looked at a few examples of built-in functions in Python, but being
#able to define your own functions is incredibly powerful. We start a function
#definition with the def keyword, followed by the name we want to give our
#function. After the name, we have the parameters, also called arguments, for the
#function enclosed in parentheses. A function can have no parameters, or it can
#have multiple parameters. Parameters allow us to call a function and pass it data,
#with the data being available inside the function as variables with the same name
#as the parameters. Lastly, we put a colon at the end of the line.

#After the colon, the function body starts. It’s important to note that in Python
#the function body is delimited by indentation. This means that all code indented
#to the right following a function definition is part of the function body. The
#first line that’s no longer indented is the boundary of the function body. It’s
#up to you how many spaces you use when indenting -- just make sure to be
#consistent. So if you choose to indent with four spaces, you need to use four
#spaces everywhere in your code.

#II. RETURNING VALUES

#if you need to do a simular equation mulitple times on you program you can use
#the return functions. for ex. our past area code, see below

base2 = 6
height2 = 3
area2 = (base2*height2)/2
#now this new function can Calculatethis mulitpletime for us. see below

def area_triangle2(base2, height2):
    return base2*height2/2 #return tell python that this is the return value
    # of the functions, when we call teh function we store that value in a variables
#lets say there are 2 triangles that we want to ad, this is how we would Calculate
area_a = area_triangle2(5,4)
area_b = area_triangle2(7,3)
sum = area_a+area_b
print("The sum of both areas is: "+str(sum))

#POPQUIZ: Use the get_seconds function to work out the amount of seconds in 2
#hours and 30 minutes, then add this number to the amount of seconds in 45
#minutes and 15 seconds. Then print the result.

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + 1*seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a+amount_b
print(result)
#output: 11715

def convert_seconds(seconds1):
    hours1 = seconds1 //3600 #// means floor division
    minutes1 = (seconds1-hours1*3600)//60
    remaining_seconds = seconds1-hours1*3600-minutes1*60
    return hours1, minutes1, remaining_seconds

hours1, minutes1, seconds1 = convert_seconds(5000)
print(hours1, minutes1, seconds1)
