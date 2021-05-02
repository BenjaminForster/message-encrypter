print('''
Message Encrypter
──────────────────''')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
special = '[@_!#$%^&*()<>?/\|}{~:]1234567890'
keySpecial = 'abcdefghijklmnopqrstuvwxyz[@_!#$%^&*()<>?/\|}{~:]'
newMessage = ''

message = input('Please enter a message: ').lower()
if len(message) < 2:
    print('Message needs to be at least 2 characters, exiting program')
    exit()

specialInMessage = [c for c in special if c in message]
if specialInMessage:
    print('Invalid character found in message, "', message, '" exiting program')
    exit()
        
key = input('Enter a key (1-26): ')
SpecialInMessage = [c for c in keySpecial if c in key]
if SpecialInMessage:
    print('Invalid number found in key, "', key, '" exiting program')
    exit()
key = int(key)
if key < 1 or key > 26:
    print('Invalid number found in key, exiting program')
    exit()

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('Your new message is: ', newMessage)
exit()
