# list = [0, 1]
count = int(input("inter number "))
x= [0,1]
for i in range(count):
    x.append(x[i] + x[i+1])
print(x)
