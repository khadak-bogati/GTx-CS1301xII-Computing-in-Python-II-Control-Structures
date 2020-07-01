#Write a function called password_check. password_check should
#take as input a single string. It should return a boolean:
#True if the password is a valid password according to the rules
#below, False if it is not.
#
#A string is a valid password if it meets ALL the following
#conditions:
#
# - It must be at least 8 characters long.
# - It must contain at least one character from each of the
#   following categories: capital letters, lower-case letters,
#   numbers, and punctuation. For punctuation, the following
#   punctuation marks are acceptable: !@#$%&()-_[]{};':",./<>?
# - It may not contain any characters that do not fit into the
#   four categories above. This includes any punctuation marks
#   not listed in the bullet point above, spaces, and any other
#   character.


#Add your code here!
def password_check(passwd): 
      
    SpecialSym =['!', '@', '#', '$', '%', '&', '()', '-', '_', '[]', '{}', ';',':' ,',', '.', '/', '<', '>', '?'] 
    val = True
      
    if len(passwd) <8:
        return False
        
    
        
          
    if not any(char.isdigit() for char in passwd):
        return False
        
        
          
    if not any(char.isupper() for char in passwd):
        return False
        
        
          
    if not any(char.islower() for char in passwd):
        return False
        
        
          
    if not any(char in SpecialSym for char in passwd):
        return False
        
        
    if val: 
        return True 


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(password_check("tHIs1sag00d.p4ssw0rd."))
print(password_check("3@t7ENZ((T"))
print(password_check("2.shOrt"))
print(password_check("all.l0wer.case"))
print(password_check("inv4l1d CH4R4CTERS~"))
print(password_check("(Kc[6xnN"))



