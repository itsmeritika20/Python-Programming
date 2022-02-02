spam = ["subscibe", "click", "buy"]
#email = "this is a nice talk...you need to click and buy"
email = input("enter email:")
if("subscribe" in email):
    spam = True
if("click" in email):
    spam = True
if("buy" in email):
    spam = True
print("Spam is",spam)