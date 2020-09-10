import pymongo

dbclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = dbclient["mytestdatabase"]
mycol = mydb["users"]
print("Connected to DB")

def add():
    try:
        name = input("Digit your name: ")
        age = int(input("Digit your age: "))
        mycol.insert_one({"name": name, "age": age})
        print("Added! :-)")
    except:
        print("Error! :-(")

def consult():
    try:
        name = input("Who is the name: ")
        x = mycol.find({"name": name}, {"_id": 0, "name": 0, "age": 1})
        for age in x:
            print("{} is {} years old".format(name, age))
    except:
        print("Error! :-(")
    
def delete():
    try:
        name = input("Who is the name: ")
        mycol.delete_one({name})
        print("{} deleted!".format(name))
    except:
        print("Error! :-(")

def update():
    try:
        name = input("Who is the name: ")
        age = input("New age: ")
        mycol.update_one({name}, {"$set": {age}})
        print("{} updated! New age is: {}".format(name, age))
    except:
        print("Error! :-(")

print("Hello! Here, you can select a task to do in MongoDB!\n")
myOptions = {0: add, 1: consult, 2: update, 3: delete}
while(True):
    print("Please, select what you want:")
    print("0: insert")
    print("1: make a query")
    print("2: update a row")
    print("3: delete a row")
    print("4: exit \n")
    try:
        option = int(input("Digit your option: "))
        if(option == 4):
            print("Thanks for use this app")
            break
        if(option >= 0 and option < 4):
            myOptions[option]()
    except:
        print("Error!")