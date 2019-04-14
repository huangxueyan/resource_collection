##手动实现RSA算法
#%% 手动实现RSA算法
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def exgcd(a,b):
    if b==0:
        x,y=1,0
        return a,x,y
    else:
        ans,x2,y2=exgcd(b,a%b)
        x1=y2
        y1=x2-a//b*y2
    #解得的x1有可能是负数，将其转为正数
    #ax+by=1-->a(x+b)+b(y-a)=1
    while x1<0:
        x1+=b
        y1-=a
    return ans,x1,y1
q,p=97,103
N=q*p
phi=(p-1)*(q-1)
e=53
d=exgcd(e,(q-1)*(p-1))[1]

message=1234
code=message**e%N
decode=code**d%N
print(message,decode)



#%% 扩展版本
print('输入两个质数q,p,推荐103,97')
q=int(input('q='))
p=int(input('p='))
N=q*p
print('得到公钥N=pq={}'.format(N))
print('为了得到私钥d,先计算phi(N)=(q-1)(p-1)={}'.format((q-1)*(p-1)))
print('输入一个数e与phi(n)互质,e为公钥,可随机取一个质数，推荐为53')
e=int(input('输入e='))
d=exgcd(e,(q-1)*(p-1))[1]
print('计算私钥d,d=exgcd(e,phi(N))={}'.format(d))
print('目前得到的公钥(N,e)=({},{})'.format(p*q,e))
print('目前得到的私钥d={}'.format(d))

print('输出要加密的数据message,数值小于N的整型')
message=int(input('message='))
print('message is {}'.format(message))
code=(message**e)%N
print('code is {}'.format(code))
decode=(code**d)%N
print('decode is {}'.format(message))

if message==decode:
    print('correct!! message == decode ')
else:
    print('message !=decode.')
