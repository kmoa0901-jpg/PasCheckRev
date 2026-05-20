# This will consider "Good Password" if it contains upper case letter,numbers and more than 8 characters long
def pascheck(pas):
    has_upper = False
    has_num = False
    for char in pas:
        if char.isupper():
            has_upper= True
        if char.isdigit():
            has_num=True
    if has_upper:
        if has_num:
            if len(pas)>=8:
                return("Good Password!")
            else:
                return("Pssword need to ne at least 8 characters long")
        else :
            return("It needs to contain numbers")
    else:
        return("It needs to contain upper case letter")
    
print("This checks if your password is good or bad\n")
pas = input("Enter Your Password : ")
check = pascheck(pas)
print(check)