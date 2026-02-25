p1 = "Make lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click here"

message = input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    
    print("This comment is spam")

else:
    print("Commment is not a spam")