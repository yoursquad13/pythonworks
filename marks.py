name = input("Enter your name: ")
math = int(input("Enter you marks in math: "))
programming = int(input("Enter you marks in programming: "))
hardware = int(input("Enter you marks in Hardware: "))
information = int(input("Enter you marks in Information System: "))
english = int(input("Enter you marks in English: "))

total = (math + programming + hardware + information + english)/5

print(name)
print("Math: ",math,"\nProgramming: ",programming,"\nHardware: ",hardware,"\nInformation Syster: ",information,"\nEnglish: ",english)
if total > 70:
    print("You Scored: A")
elif total > 60:
    print("You Scored: B")
elif total > 50:
    print("You Scored: C")
elif total > 43:
    print("You Scored: D")
elif total > 40:
    print("You Scored: E")
else:
    print("You Scored: F")
    
    
