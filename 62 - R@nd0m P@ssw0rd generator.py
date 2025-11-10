import random  

def generate_password(): 
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|"
    
    all_characters = letters + numbers + symbols 
    
    password = ""  
    
   
    for i in range(62):
        password = password + random.choice(all_characters) 

    return password

print("Random Password Generator")
print("--------------------------")
testPassword = generate_password()
print("Your random 62-character password is:")
print(testPassword)
