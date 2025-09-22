# Initializes an empty list to store the total as well as the count used
t=0
c=0
while True:
    user_input = input("Input a number or done in order to finish: ")
    if user_input == "done":
        break
    try:
        t=t+int(user_input)
        c=c+1
    except:
        print("error, please try again with only integers")
if c==0:
    a=0
else:
    a=t/c
print("t=",t)
print("c=",c)
print("a=",a)