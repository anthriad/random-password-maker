import random
import string # brings in all possible letters, numbers, and special characters

# create the password generator
def password_generator(min_length, numbers = True, symbols_n_characters = True):

  letters = string.ascii_letters # calls all possible letters
  nums = string.digits # calls all possible numbers
  specChars = string.punctuation # calls all possible special characters and symbols

# create string with all possible letters and numbers to choose from
  characters = letters
  if numbers:
    characters += nums
  if symbols_n_characters:
    characters += specChars

  password = ""   # password is empty
  criteria = False # not criteria yet to meet
  cont_num = False  # no numbers yet
  cont_symbol = False  # no special characters or symbols yet

  while not criteria or len(password) < min_length:
    character_new = random.choice(characters)
    password += character_new

    if character_new in nums:
      cont_num = True # checks if number is included
    elif character_new in specChars:
      cont_symbol = True    # checks if special character or symbol is included

    criteria = True
    if numbers:
      criteria = cont_num
    if symbols_n_characters:
      criteria = criteria and cont_symbol # if both are true, then the criteria will return true
  
  return password

# prompt the user to enter minimum length of password
min_length = int(input(" Enter desired minimum length of password:"))

# prompt user to enter if they prefer numbers in password
cont_num = input("Would you like to include numbers in the password (y/n)? ").lower() == "y" # converts to lowercase and checks if equal to "y" (yes

# prompt user to enter if they prefer special characters and symbols in password
cont_symbol = input("Would you like to include special characters and symbols in the password (y/n)? ").lower() == "y"

password = password_generator(min_length, cont_num, cont_symbol)
print("Your new password is: ", password)