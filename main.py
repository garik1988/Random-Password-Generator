from random import randint, shuffle
import string

def passgenerator(letters,digits,symbols): #generates a list of random characters then shuffle it and returns string
  
  randompass=[]
  
  lettersstr=string.ascii_letters
  
  digitsstr=string.digits
  
  symbolsstr=string.punctuation
  
  for letter in range(0,letters):
    
    randompass.append(lettersstr[randint(0,len(lettersstr)-1)])
  
  for digit in range(0,digits):
    
    randompass.append(digitsstr[randint(0,len(digitsstr)-1)])
  
  for symbol in range(0,symbols):
  
    randompass.append(symbolsstr[randint(0,len(symbolsstr)-1)])
  
  shuffle(randompass)
  
  randompass=''.join(randompass)

  return (randompass)


def main():
  
  while True:
    
    passwordletters = int(input("how many letters would you like in your password?\n"))
    
    passworddigits = int(input("how many digits would you like in your password?\n"))    
    
    passwordsymbols = int(input("how many symbols would you like in your password?\n"))    
    
    print ("your random password is: {}".format(passgenerator(passwordletters,passworddigits,passwordsymbols)))
    
    exit=input("generate another password y/n ?\n")
    
    if exit.capitalize() == "N":
      
      break
  
main()