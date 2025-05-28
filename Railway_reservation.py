import random
class Account():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def checkpassword(self,password):
        return self.password==password
account=[
    Account("user1","p1"),
    Account("user2","p2")
    ]
class Train_details():
    def __init__(self,train_number,source,destination,seats):
            self.train_number=train_number
            self.source=source
            self.destination=destination 
            self.seats=seats
    def information(self):
            print(f"enter the train number:{self.train_number}")
            print(f"enter the source:{self.source}")
            print(f"enter the destination:{self.destination}")
            print(f"enter the seats:{self.seats}")
    def book_tickets(self,num_tickets):
            if num_tickets>self.seats:
                return None
            else:
                pnr_lists=[]
                for i in range(num_tickets):
                     pnr_lists.append(random.randint(10000,999999))
                self.seats -= num_tickets
                return pnr_lists
class passenger_details():
    def __init__(self,Name,age,gender,mobile_no):
                self.Name=Name
                self.age=age
                self.gender=gender
                self.mobile_no=mobile_no
    def display_info(self):
                print(f"Name:{self.Name}")
                print(f"age:{self.age}")
                print(f"gender:{self.gender}")
                print(f"mobile_no:{self.mobile_no}")
class ticket():
    def __init__(self,train,source,destination,passengers,pnr_no):
        self.train=train
        self.source=source
        self.destination=destination
        self.passengers=passengers
        self.pnr_no=pnr_no
    def display_info(self):
        print(f"train no:{self.train.train_number}")
        print(f"source:{self.source}")
        print(f"destination:{self.destination}")
        print(f"pnr_no:{self.pnr_no}")
        for passenger in self.passengers:
            passenger.display_info()


loginaccount=None
while True:
    print("enter 1 for creating new account\n or enter 2 for login")
    choice= input("enter the number:")
    if choice=="1":
       username=input("enter the username:")
       password=input("enter the password:")
       account.append(Account(username,password))
       print("account created succesfully")
    elif choice=="2":
        username=input("enter the username:")
        password=input("enter the password:")
        for user in account:
            if user.username==username and user.checkpassword(password):
               loginaccount=user
               break
        if loginaccount is None:
            print("invalid username or password")
        else:
            print(f"login sucessful{loginaccount.username}")

            break
if loginaccount is not None:
    trains=[
        Train_details("1234","hyderabad","goa",15),
        Train_details("4567","bangalore","hyderabad",25),
        Train_details("4321","goa","hyderabad",30),
        Train_details("7654","hyderabad","bangalore",20),
     ]
for train in trains:
    train.information()


while True:
    try:
      trainnumber=input("enter the train number:")
      no_of_tickets=int(input("enter no of tickets:"))
      if no_of_tickets<=0:
        raise ValueError("no of tickets should be grater than 0 :")
      for train in trains:
          if train.train_number==trainnumber:
            if no_of_tickets>train.seats:
               raise ValueError("selected tickets are more than available")
            break
      else:
          raise ValueError("invalid train number")
      break
    except ValueError as e:
        print(f"invalid input:{e}")

train=None
for t in trains:
    if t.train_number==trainnumber:
        train=t
        break
if train is None:
    print("invalid train number")
else:
    passengers=[]
    for i in range(no_of_tickets):
        print(f"enter the passenger details:(i+1)")
        while True:
            Name=input("name")
            age=int(input("age"))
            gender=input("gender")
            mobile_no=int(input("mobile_num"))
            passenger=passenger_details(Name,age,gender,mobile_no)
            passengers.append(passenger)
            break
    pnrlist=train.book_tickets(no_of_tickets)
    if pnrlist is None:
      print("tickets not available")
    else:
     print("booking succesful")
     for i in range(no_of_tickets):
          ticket = ticket(train,train.source,train.destination,[passengers[i]],pnrlist[i])
          ticket.display_info()
          print("booking successfully")
                    
                    
                        
