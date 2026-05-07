# 1. Write a program that takes salary as input. Using conditional statements, calculate the final tax 
# based on the following rules: 

salary=int(input("Enter your salary: "))
if salary<30000:
    tax=salary*0.05
elif salary>=30000 and salary<70000:
    tax=salary*0.15
elif salary>70000:
    tax=salary*0.25
print("Your tax is: ", tax)






# 2. Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"]          
# Create a dictionary that maps each word to its corresponding length. 
# Example Output: ({"apple": 5, "banana": 6, "kiwi": 4, "cherry": 6, "mango": 5}) 

words = ["apple", "banana", "kiwi", "cherry", "mango"]
word_lenght={word:len(word) for word in words}
print(word_lenght)







#  Create a Chat System using Object-Oriented Programming (OOP) concepts.             
# • User  
# • Message  
# • ChatRoom  
#                The system should implement the following functionalities: 
# • Sending messages  
# • Viewing chat history  
# • User joining and leaving the chat room 



from datetime import datetime

class User:
    def __init__(self,name):
        self.name=name

class Message:
    def __init__(self,sender,content):
        self.sender=sender
        self.content=content
        self.timestamp=datetime.now().strftime("%H:%M:%S")

class Chatroom:
    def __init__(self,room_name):
        self.room_name=room_name
        self.users=[]
        self.messages=[]
    def join(self,user):
        self.users.append(user)
        print(f"({user.name} has joined the chatroom {self.room_name})")
    def leave(self,user):
        if user in self.users:
            self.users.remove(user)
            print(f"({user.name} has left the chatroom {self.room_name})")
    def send_message(self,user,content):
        if user in self.users:
            message=Message(user,content)
            self.messages.append(message)
            print(f"{message.timestamp} - {message.sender.name}: {message.content}")
        else:
            print(f"{user.name} is not in the chatroom {self.room_name}. Please join to send messages.")
    def view_chat_history(self):
        print(f"Chat history for {self.room_name}:")
        for message in self.messages:
            print(f"{message.timestamp} - {message.sender.name}: {message.content}")
room = Chatroom("Friends Group")

ali   = User("Ali")
sara  = User("Sara")
ahmed = User("Ahmed")
room.join(ali)
room.join(sara)
room.join(ahmed)

room.send_message(ali,   "Hello everyone!")
room.send_message(sara,  "Hi Ali!")
room.send_message(ahmed, "Assalam o Alaikum!")

room.view_chat_history()

room.leave(ali)
room.send_message(ali, "Can I still message?")



    
        
    
