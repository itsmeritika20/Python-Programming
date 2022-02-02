oxford = {
    "kath" : "wood",
    "baksho" : "box",
    "chiruni" : "comb"
}
key = input("Enter the key:")
if oxford.get(key) == None:
    print("value not found")
else:
    print("The value corresponding to the key is",oxford.get(key))