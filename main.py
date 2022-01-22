# Write a Pythom program to add "ing" at the end of a given string (length of string should be atleast 3). If the given string already ends with "ing" then add "ly" instead. If string length is less than 3, leave it unchanged
x=input()
l=len(x)
if(x[:l-3]=="ing" and l>3):
    x.remove("ing","ly")
elif(l>3 and x[:l-3]!="ing"):
  print(x+"ing")
else:
  print(x)