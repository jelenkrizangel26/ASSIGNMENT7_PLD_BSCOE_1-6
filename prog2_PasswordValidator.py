#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex. input: P@ssw0rd+P@ssw0rd
#ouput: Valid
#Tip: loop through each character of the input then process it letter by letter

#STEPS:
#1. Ask for the password:
print("Good day, kindly input your password below\U0001F601")
password = input("\n\33[3mYour password\33[0m: ")


#2. Give the conditions:
def passwordValid(password):
    
    characters = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '/', ":", ";", '"', "'", '<', '>', '.', "?", ',']
    val = True

    if len(password) < 15: #a. Greater than 15 letters
        print("Your password must be gretater than 15 letters.") 
        val = False

    if not any(char.isupper() for char in password): #b. Have at least one capital letter
        val =False
            
    if not any(char.isdigit() for char in password): #c. Have at least one number
        val =False

    if not any(char in characters for char in password): #d. Have at least one special char (!@#$%^&*()_+ etc)
        val =False
    
    if val:
        return val








