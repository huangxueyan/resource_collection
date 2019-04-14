#调用低通api实现RSA
import rsa
import time
#计算下时间 
start_time = time.time()
key = rsa.newkeys(1024) #数字代表 p * q 产生的存储空间 bit 大小, 也就是密文长度，数字越大，时间越长
privateKey = key[1]
publicKey = key[0]
#print(privateKey)
#print(publicKey)
end_time = time.time()
print("make a key:", end_time - start_time)
#产生公钥和私钥
 
message = 'hello'
message = message.encode()
 
cryptedMessage = rsa.encrypt(message, publicKey)
print("crypted:", cryptedMessage)
print("length of cryptedMessage：", len(cryptedMessage))
# 加密的过程
 
decrypetdMessage = rsa.decrypt(cryptedMessage, privateKey)
print("decrypet:", decrypetdMessage)
# 解密的过程
 
now_time = time.time()
print("crypt and decrypt:", now_time - end_time)

