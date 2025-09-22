# Initialize an empty list that stores numbers
nums=[]
while True:
    user_input = input("You can enter a number or done in order to finish: ")
    if user_input == "done":
        break
    try:
        n=int(user_input)
        nums.append(n)
    except:
        print("Please enter a number, or done")


if nums:
    print("max=",max(nums))
    print("min=",min(nums))

else:
    print("No numbers found")
