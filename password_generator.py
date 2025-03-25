import random as r
import string as s

chars = []

for i in s.ascii_letters:
    chars.append(i)

for j in range(0,10):
    chars.append(str(j))

symbols = ['.',',','-',':','_','?','!','+','%','(',')']
chars_symbols = chars.copy()
for s in symbols:
    chars_symbols.append(s)

print('Hey, I can generate a password for you, based on your needs. \n'
      'I just need to know the required length and if you need any special symbols.\n'
      'The password is recommended to be at least 8 but no more than 32 characters. \n'
      'In case you enter a lower or higher number, the generated password will be 20 characters long.')

def get_integer(prompt,max_attempts=3):
    attempts = 0
    while max_attempts-attempts > 0:
        try:
            return int(input(prompt))
        except ValueError:
            attempts += 1
            print(f'Please enter a valid number between 8 and 32. You have {max_attempts-attempts} attempts left.')
    print('No more attempts left. Exiting.')
    return None

length = get_integer('How many characters shall the password consist of? ')
if length < 8 or length > 32:
    length = 20

att = 0
pw_generated_list = []
spec_char = None
while (spec_char != 'Y' and spec_char != 'N') and att < 4:
    spec_char = input('Would you like to have special characters in the password? (Y/N) ').upper()
    if spec_char == 'Y': # 1st character is not a special character anyway
        pw_generated_list.append(chars[r.randint(0, len(chars) - 1)])
        for k in range(length-1):
            pw_generated_list.append(chars_symbols[r.randint(0,len(chars_symbols)-1)])
    elif spec_char == 'N':
        for l in range(length):
            pw_generated_list.append(chars[r.randint(0,len(chars)-1)])
    else:
        att += 1
        print('Please only enter Y or N characters to proceed. Remaining attempts: {}'.format(4-att))
if att < 4:
    password = ''.join(pw_generated_list)
    print(f'Your generated password consists of {length} characters. Here you go: {password}')
else:
    print('No answer about special characters. Exiting.')