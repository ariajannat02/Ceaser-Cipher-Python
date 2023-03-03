LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()



def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            encrypted +=  LETTERS[num]

    return encrypted

def decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            decrypted +=  LETTERS[num]

    return decrypted

def main():
  while True:
    message = str(input('Enter your message: '))
    key = int(input('Enter you key [1 - 26]: '))
    choice = input('Encrypt/Decrypt? [E/D]: ')

    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    elif choice.lower().startswith('d'):
        print(decrypt(message, key))
    else:
        print("invalid choice")

    again= input("Do you want to encrypt/ decrypt another message(Y/N)? ")
    if again=="Y" or again=="y":
        continue
    elif again=="N" or again=="n":
        break
    else:
        print("invalid choice")

main()


    