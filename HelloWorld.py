print("Hello World")

# comments start with # or with """
""" This is a 
multi line comment """
# python doesnt have types, just type hinting

someint = 5
somefloat = 5.6
somenum = someint + somefloat
print(somenum)

# type hinting
# convert to int
print(int(somenum)) # for 10.6 it prints 10
# convert to float
print(float(somenum))

# Strings
# single quotes, double quotes all the same
# python 3 supports unicode
print("-------Strings------")
name = "abc"
numstr = "123"
print(name.capitalize())
print(name.replace("a", "b"))
print(name.isalpha())
print(numstr.isdigit())
print("comma,separated,values".split(",")) # converts to array
print("Formatting {0} and {1}".format(name, numstr))
print(f"Formatting {name} and {numstr}")
print(r"Dont change anything here. R is for raw. ///\\\\")

print("--------Boolean and Null---------")
somethingtrue = True
somethingfalse = False
print(somethingtrue) 
print(int(somethingtrue))
print(somethingfalse) 
print(str(somethingfalse))
somethingnull = None
print(somethingnull)


print("---------IF-----------")
num = 3
if num==3:
    print("Num is 3")
else:
    print("Num is not 3")

if numstr:
    print("Text is defined and truthy")

if not somethingnull:
    print("this will print")

if num==3 and numstr=="123":
    print("all good")

if num==3 or numstr=="123sdfas":
    print("still good")

#ternary    
print("big" if num > 2 else "small")

print("-------Lists----------")
names = ["Roger", "Rafael", "John", "Stan", "Andy"]
print(names[0])
print(names[-1]) #last item in the list
names.append("Pete")

if "Pete" in names:
    print("Pete is in there")

print(len(names))

del names[4]
print(names)

print("----------Loop------------")
for n in names:
    print(n)

for i in range(0,len(names),1):
    print(names[i])

for n in names:
    if n == "John":
        print("Found him")
        break

for n in names:
    if n == "Stan":
        continue
    print(n) 

i = 0
while i < 10:
    print(i)
    i = i + 1

print("----------Dictionary------------")
players = [{ "Name" : "Rafael Nadal", "Country" : "Spain"},
{ "Name" : "Roger Federer", "Country" : "Switzerland"},
{ "Name" : "Pete Sampras", "Country" : "USA"}]

print(players)
def print_players():
    for player in players:
        str = player["Name"] + " " + player["Country"]
        print(str)

players.append({ "Name" : "Andre Agassi", "Country" : "USA"})
print_players()

for player in players:
    if player["Name"] == "Andre Agassi":
        players.remove(player)
print_players()

print("----------Exceptions------------")
try:
    #i = 5 + "abc"
    i = 5 / 0
except TypeError as error:
    print("TypeError happened")
    print(error)
except Exception as error:
    print(error)

print("----------Functions------------")
def add(i, j):
    return i + j

print(add(4,5))



print("-----------------------")
#Kind of like console.ReadLine()
input("Enter to exit...")
