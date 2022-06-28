#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Letters
l_letter = len(letters)
t_letters = str()

for n in range(0, nr_letters):
  r_letter = random.randint(0, l_letter - 1)
  t_letters += letters[r_letter]

#Numbers
l_number = len(numbers)
t_numbers = str()

for n in range(0, nr_numbers):
  r_number = random.randint(0, l_number - 1)
  t_numbers += numbers[r_number]

#Symbols
l_symbol = len(symbols)
t_symbols = str()

for n in range(0, nr_symbols):
  r_symbol = random.randint(0, l_symbol - 1)
  t_symbols += symbols[r_symbol]

print(f"{t_letters}{t_numbers}{t_symbols}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

l = [t_letters, t_numbers, t_symbols]
rl = random.shuffle(l)

print(f"{l[0]}{l[1]}{l[2]}")
