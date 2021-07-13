# encryptMap is like a key 
encryptMap = "qwertyuiopasdfghjklzxcvbnm"
# decryptMap is used to return the index of the charactor from encryptMap. 
# Example encrypt msg is "w" then it will return 2 if "b" then 23
def decryptMap(msg):
    for index,character in enumerate(encryptMap):
        if(character==msg):
            return index
    return -1

def encrypt(msg):
    #ord() convert char to ascii  chr() ascii to char
    result=""
    for character in msg:
        if(character.isalpha()):
            if(character.isupper()):
                # example "B" is to be encrypted ascii of b is 98 and a is 97
                # encryptMap[98-97]=encryptMap[2]=w 
                character=encryptMap[ord(character.lower())-ord('a')].upper()
                character.upper()
                result+=character
            else:
                character=encryptMap[ord(character)-ord('a')]
                result+=character
        else:
            result+=character
    return result

def decrypt(msg):
    result=""
    for character in msg:
        if(character.isalpha()):
            if(character.isupper()):
                # example "B" is to be decrypted 
                # from decryptMap we get the index of w i.e. 1 according to the encryptMap
                # ascii of a is 97 
                # 97+1=98 i.e ascii value of b 
                character=chr(ord('a')+decryptMap(character.lower())).upper()
                result+=character
            else:
                character=chr(ord('a')+decryptMap(character))
                result+=character
        else:
            result+=character
    return result

encrypt=encrypt("B1we")
decrypt=decrypt(encrypt)
print("Encrypted String: "+encrypt)
print("Decrypted String: "+decrypt)
