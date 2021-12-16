
#dictionary
d = {
    "sir": "matey", 
    "hotal": "fleabag-inn", 
    "student": "swabbie", 
    "boy": "matey", 
    "madam": "proud-beauty",
    "professer": "foul-blaggart",
    "restaurant": "gallery",
    "your": "yer",
    "excuse": "arr",
    "are": "be",
    "lawyer": "foul-blaggart",
    "the": "th'",
    "restroom": "head",
    "my": "me",
    "hello": "avast",
    "is": "be",
    "man": "matey",
    }

list = []

#prints out the words in dictionary
print()
print("Words In DICTIONARY;")
for ew in d.keys(): #order is not defined
   list.append(ew)
print(list)

#inputs the sentence
print()
print("Make sure to put spaces between words/charecters")
print(" 👇 Enter the text you would like to translate 👇")
x = input("     ") 
X = x.lower()


#translates the sentence
s = X.split()
n = []
for ew in s:
    if ew in d:
        f = d [ew]
    else:
        f = ew
    n.append(f)
n[0] = n[0].capitalize()


#creats tthe list to create the sentance
r = " "
new = r.join(n)
print()


#calls turtle wn
import turtle
wn = turtle.Screen()
wn.bgcolor("grey")

t = turtle.Turtle() 
t.color("brown")
t.pensize(4)

#semi- dircle
t.begin_fill()
t.penup()
t.goto(-300, 0)
t.pendown()
t.right(90)
t.circle(50,180)
t.goto(-250,0)
t.end_fill()

#rod
t.pensize(9)
t.color("black")
t.forward(200)

#flag
t.left(90)
t.left(90)
t.forward(100)
t.color("red")
t.begin_fill()
t.left(135)
t.forward(142)
t.left(135)
t.forward(100)
t.end_fill()



t.color("gold")
t.pensize(4)
#prints on turtle wn
t.penup()
t.goto(-200,50)
t.write(new, align="left", move=False, font=("Calibri", 20, "underline"))
t.hideturtle()

wn.exitonclick()
