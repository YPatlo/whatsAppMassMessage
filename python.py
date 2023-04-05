import pywhatkit
#initializingAndDeclaringVariables
i=0
msg = input("Enter a message : ")
#declaringArrays/lists
phnumbers = ["+918050531619","+918618894356","+918147310199","+917676438001","+919482760489","+919538431511","+919884172862",
           "+919538372123","+919945052167","+917299817214","+919566223248","+919880111854","+919108822323","+919019989603",
           "+919742978118","+918762106560","+918747890892","+919972136536","+918660849489","+918197603665","+918722217223",
           "+919019336224","+919739281374","+919886328269"]

firstname = ["Anjana","Bhuvana","Thanmayi","Prakruthi","Thanmayi","Sanvi","Thanvanth","Dhanya","Vikram","Mithra","Mithra","Tharak",
        "Nagarjun","Nagarjun","Samia","Samia","Ayush","Janani","Avni","Vivan","Avni","Bhoomi","Rahul","Prathika"]

#whileLoopToSendMessages
while i<24:
    msgToBeSent = (f"Hi {firstname[i]}, "+msg+"This message was sent to by a Python program ```PyWhatKit```. ")
    pywhatkit.sendwhatmsg_instantly(phnumbers[i],msgToBeSent,)
    print(f"Message sent to {firstname[i]}")
    i+=1
#confirmationThatCodeHasRunCompletelyWithoutErrors
print("Messages succesfully sent to all contacts.")