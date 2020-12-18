# 内容输出
print('我的尼玛的，BUG那么的多，加油干吧，草')
#加法
num = 1
num1 = 1
num2 = 1
num3 = 1
num4 = 1
num5 = 1
num6 = num+num1+num2+num3+num4+num5
print(num6)
#乘法
num7 = 3*5
print(num7)

# 元组
# 将列表转换成元组
list = tuple([1,2,3,4,5])
# 类型判断
print(type(list))
# 元组输出
print(list)

#除法
num8 = float(9//2)
print(float(num8))

# 基础判断
age = 100
if age:
    print('2333')
else:
    print('4555')

# 循环+输入+判断
while 1:
    month = int(input('请输入月份'))
    if month == 3 or month == 4 or month == 5:
        print('春季')
    elif month == 6 or month == 7 or month == 8:
        print('秋季')
    elif month == 9 or month == 10 or month == 11:
        print('冬季')
    elif month == 12 or month == 1 or month == 2:
        print('春季')
    elif month == 111:
        break
    else:
        print('请重新输入')


# 循环+判断
num = 0
while num < 100:
    if num == 99:
        print("午时已到")
    num+=1
    print(num)


# 打印三角形
i = 0
while i <5:
    j = 0
    while j<i:
        print("*",end=" ")
        j+=1
    print("\n")
    i+=1

# 九九乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (i,j,i*j),end= "  ")
        j+=1
    print("\n")
    i+=1

# 切片
# 指对操作的对象截取其中一部分的操作
# 字符串 列表 元祖 支持 切片操作
name = "abcdefg"
print(name[0:5:2])
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*",end=" ")
        j+=1
    print("\n")
    i+=1

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,(i*j)),end=" ")
    print("")