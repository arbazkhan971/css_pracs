import math
def encrypt(msg):
    text1 =[v for i,v in enumerate(msg) if i%2==0 ]
    text2 =[v for i,v in enumerate(msg) if i%2!=0 ]
    return "".join(text1+text2)

def decrypt(msg):
    text1 = msg[:math.ceil(len(msg)/2)]
    text2 = msg[math.ceil(len(msg)/2):]
    
    temp = " "
    for i,v1 in enumerate(text1):
        for j,v2 in enumerate(text2):
            if i==j:
                temp+=v1+v2
    
    if len(msg)%2!=0:
        temp+=text1[-1]
    return temp

print("before decryption",encrypt("SFIT ki maaaki"))
print("\n\n\n")
print("after decryption",decrypt(encrypt("SFIT ki maaaki")))
print("\n\n\n")