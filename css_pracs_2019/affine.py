def encode(msg,key):
    a,b = key
    text = [ord(i)-ord("A") for i in msg.upper()]
    temp = [(a*i+b)%26 + ord("A") for i in text ]
    return "".join(chr(i) for i in temp)
def decode(msg,key):
    a,b = key
    text = [ord(i)-ord("A") for i in msg]
    temp = [(modinv(a)*(i-b))%26 for i in text]
    return "".join(chr(i) for i in temp)
print("before decryption",encode("cryptography",(7,2)))
print("\n\n\n")
ans = decode(encode("cryptography",(7,2)),(7,2))
print("after decryption",ans)
print("\n\n\n")