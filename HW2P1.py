users = []
Count = int(input("Enter users count : "))
for x in range(Count):
    name = str(input("Enter user.name : "))
    age = int(input("Enter user.age : "))
    user = {"name":name,"age":age}
    users.append(user)

searchName = str(input("Enter name to search : "))

isCorectName = False
for i in users:
    if searchName == i['name']:
        isCorectName = True
        print(int(i['age']))

if isCorectName == False:
    print("There is no user with given name!")
