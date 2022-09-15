print("Welcome to my computer quiz!")

playing=input("Do you want to play?")

if playing!="yes":
    quit()
Result=0
print("Okey! Let's play:)")
answer=input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print("Currect!")
    Result=Result+1
else:
    print("Wrong!")

answer=input("What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print("Currect!")
    Result=Result+1
else:
    print("Wrong!")

answer=input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("Currect!")
    Result=Result+1
else:
    print("Wrong!")

answer=input("What does ROM stand for?")
if answer.lower() == "read only memory":
    print("Currect!")
    Result=Result+1
else:
    print("Wrong!")

answer=input("What does PSU stand for?")
if answer.lower() == "power supply unit":
    print("Currect!")
    Result=Result+1
else:
    print("Wrong!")

print(f"You got {Result} out of 5")
if Result<3:
    print("Now you are not good at this sector. Please learn more then try again ")
elif Result==5:
    print("You are totally impressive! keep it up")
elif Result>3:
    print("Your are in intermediate level.Learn more")

