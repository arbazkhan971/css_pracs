def encrypt(msg,k):
    cypher = ""
    for i in msg.replace(" ",""):
        if i ==" ":
            cypher += i
        if i.islower():
            cypher+=chr(((ord(i)+k-65)%26)+65)
        else :
            cypher+=chr((ord(i)+k-97)%26 +97 )
    return cypher

def decrypt(msg,k):
    cypher = ""
    for i in msg.replace(" ",""):
        if i ==" ":
            cypher +=i
        if i.islower():
            cypher+=chr(((ord(i)-k-65)%26)+65)
        else :
            cypher+=chr((ord(i)-k-97)%26 +97 )
    return cypher

print("before decryption",encrypt("arbaz khan saleem",15))
print("\n\n\n")
print("after decryption",decrypt(encrypt("arbaz khan saleem",15),15))
print("\n\n\n")