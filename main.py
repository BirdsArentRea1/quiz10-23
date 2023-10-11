#from winsound import beep
#1.1
for i in range (6, 39, 3):
    print(i, end =" ")
    
print()

#1.2
def CountByThrees(x,y):
    print(x, "*", y, "is", x*y )
     
CountByThrees(3,12)

print()
#2
ex = int(input("How much exercize do you get in a week"))
if ex < 20:
    print ("Thats not enough exercize")
elif ex > 20, and ex < 101:
    print("get more exercize")
elif ex > 100, and ex < 500:
    print("Thats the perfect amount of exercize")
else ex > 500:
    print("thats alot, too much even.")
    
print()
#3
#choice = "Enter a number"
#while choice != "noise":
    #print(choice)
    #choice = input("")
