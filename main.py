from random import choice, shuffle
import string

def passgenerator(letters,digits,symbols): #generates a list of random characters then shuffle it and returns string 
  
  randompass=[]
  
  lettersstr=string.ascii_letters
  
  digitsstr=string.digits
  
  symbolsstr=string.punctuation
  
  for letter in range(0,letters):
    
    randompass.append(choice(lettersstr))
  
  for digit in range(0,digits):
    
    randompass.append(choice(digitsstr))
  
  for symbol in range(0,symbols):
  
    randompass.append(choice(symbolsstr))
  
  shuffle(randompass)
  
  randompass=''.join(randompass)

  return (randompass)


def main(): #mainloop
  
  while True:
    
    passwordletters = int(input("how many letters would you like in your password?\n"))
    
    passworddigits = int(input("how many digits would you like in your password?\n"))    
    
    passwordsymbols = int(input("how many symbols would you like in your password?\n"))    
    
    print (f"your random password is: {passgenerator(passwordletters,passworddigits,passwordsymbols)}\nyour password legth is:  {len(passgenerator(passwordletters,passworddigits,passwordsymbols))}")
   
    exit=input("generate another password y/n ?\n")
    
    if exit.capitalize() == "N":
      
      break
  
main()
