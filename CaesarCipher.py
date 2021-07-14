
"""
Caesar Cipher is about shifting letter 

Example: If we take 'b' as encrypting charactor and key as 2
we will replace the b charactor with the charactor i.e 2 step after 'b' i.e. 'd'

Logic
encrypting char ='b'
key =2
all calc is done using ascii so ascii of b=98 and a=97 d=100

first we do b-a i.e 
(b - a)+(key)
(98-97)+  2  =3

second we do modules of the answer we got with 26
3%26=3

Now we add the answer with ascii value of a
3+97=100

convert the 100 into charactor we get 'd'
so the encrypted char of 'b' is 'd' for key=2 

For Decryption it is reverse
"""

def encrypt(msg,key):
    result=""
    for charactor in msg:
        if(charactor.isalpha()):
            if(charactor.isupper()):
                charactor=(ord(charactor)-ord('A'))+key
                charactor=charactor%26
                charactor=chr(charactor+ord('A'))
                result+=charactor
            else:
                charactor=(ord(charactor)-ord('a'))+key
                charactor=charactor%26
                charactor=chr(charactor+ord('a'))
                result+=charactor
        else:
            result+=charactor
    return str(result)



def decrypt(msg,key):
    result=""
    for charactor in msg:
        if(charactor.isalpha()):
            if(charactor.isupper()):
                charactor=(ord(charactor)-ord('A'))-key
                charactor=charactor%26
                charactor=chr(charactor+ord('A'))
                result+=charactor
            else:
                charactor=(ord(charactor)-ord('a'))-key
                charactor=charactor%26
                charactor=chr(charactor+ord('a'))
                result+=charactor
        else:
            result+=charactor
    return result

def brute_force(msg):
    for i in range(1,26):
        decrypt_str=decrypt(msg,i)
        print("Index="+str(i)+" & Decypted text= "+decrypt_str)

