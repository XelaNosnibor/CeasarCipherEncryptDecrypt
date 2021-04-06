# Caesar Cipher Encrypt / Decrypt

#sets mode to either encryption or decryption of the ceasar cipher
mode = input("Enter 'encrypt' for encryption or enter 'decrypt' for decryption mode: ")

#key - set to '13' for ceasar cipher
key = 13

#ciphertext or plaintext to be used
message = input("Enter text: ")

#Symbols/letters that can be used in the cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#store the encrypted/decrypted form of the message
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Perform encryption or decryption
        if mode == 'encrypt' or 'Encrypt' or 'e' or 'E':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt' or 'Decrypt' or 'd' or 'D':
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

else:
    translated = translated + symbol

#output result of decryption or encryption
print(translated)
