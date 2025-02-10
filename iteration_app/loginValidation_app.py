attempts = 3
print("Ënter password to proceed: ")
Hash_pass = ["Goddy", "Omondi"]
n = input("Ënter password to proceed:")
usr_pass = n.split()
if (Hash_pass == usr_pass):
    print("Login Success!!")
else:
    attempts -= 1
    for i in range(attempts):
        n = input("You have " + str(attempts) + " attempts Left" + "Ënter password to proceed:")
        usr_pass = n.split()
        if (Hash_pass == usr_pass):
            print("Login Success!!")
            break
        else:
            attempts -= 1
        print("You are not a user!!!")
