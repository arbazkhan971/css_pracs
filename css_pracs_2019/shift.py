def encrypt(msg,k):
    cypher = ""
    for i in msg.replace(" ",""):
        if i.islower():
            cypher+=chr((((ord(i)+k)-ord("a"))%26)+ord("a"))
        else :
            cypher+=chr(((ord(i)+k)-ord("A"))%26 +ord("A") )
    return cypher

def decrypt(msg,k):
    cypher = ""
    for i in msg.replace(" ",""):
        if i.islower():
            cypher+=chr(((ord(i)-k)-ord("a"))%26 + ord("a"))
        else :
            cypher+=chr(((ord(i)-k)-ord("A"))%26 +ord("A"))
    return cypher

print("before decryption",encrypt("SFIT",1))
print("\n\n\n")
print("after decryption",decrypt(encrypt("SFIT",1),1))
print("\n\n\n")