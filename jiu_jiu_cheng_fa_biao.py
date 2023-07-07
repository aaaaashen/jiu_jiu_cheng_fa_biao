i = 0
while i < 9:
    i+=1
    j=1
    while j <= i:
        print("%d*%d=%-3d"%(i,j,i*j),end =" ")
        j+=1
    print()
#下三角九九乘法表while表示
print("------------------------------我是分界线------------------------------")
i = 10
while i > 1:
    i-=1
    j=1
    while j <= i:
        print("%d*%d=%-3d"%(i,j,i*j),end =" ")
        j+=1
    print()
# 上三角九九乘法表while表示
print("------------------------------我是分界线------------------------------")
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()
#下三角九九乘法表for表示




