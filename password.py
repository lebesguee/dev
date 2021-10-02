#password generator
import random
import string
print("Welcome to random password generator!")
#password length input
length = int(input('\nPlease enter password length\n'))
#lowercase, uppercase, numbers and symbols
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
#mash-up
characters = lowercase + uppercase + numbers + symbols
#returns a random list from characters with the same number of elements as given by the user in length
strings = random.sample(characters,length)
#concatenate elements of strings list in a simple word
password = "".join(strings)
print('\nPassword ready!\n\n'+password)