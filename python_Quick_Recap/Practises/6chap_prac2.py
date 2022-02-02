m1 = int(input("Enter marks:"))
m2 = int(input("Enter marks:"))
m3 = int(input("Enter marks:"))
overall = (m1 + m2 + m3) / 3

if(overall >= 40):
    if(m1 >= 33 and m2 >= 33 and m3 >= 33):
        print("you have passed")
    else:
        print("you haven't passed")
else:
        print("you haven't passed")