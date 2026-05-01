#Cryptography 1: Caeser Shift Cipher

#this allows me to import character collections
import string
character_list=string.printable

#the input asks for a message that will be either encrypted or decrypted
message = input('What is your message? ')
#asks user for key
key = input('What is the shift key? ')
#makes sure key is within group bounds
key = int(key) % len(character_list)

def encrypt_message(message,key):
    encrypted_message = ''
    for i in range(len(message)):
        if message[i] in character_list:
            location = character_list.find(message[i])
            encrypted_message += character_list[(location + key)% len(character_list)]
        else:
            encrypted_message += message[i]
    return encrypted_message

def decrypt_message(message, key):
    decrypted_message = ''
    for i in range(len(message)):
        if message[i] in character_list:
            location = character_list.find(message[i])
            decrypted_message += character_list[(location - key)% len(character_list)]
        else:
            decrypted_message += message[i]
    return decrypted_message

print(encrypt_message(message, key))






            
        