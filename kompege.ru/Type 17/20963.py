# модуль используется когда речь идет про
# окончание числа либо про остаток от деления,
# либо проверку на 2-3-4значность

f = [int(x) for x in open('17')]
arr = []

for i in range(len(f)-2):
    if (len(str(abs(f[i])))==4 and abs(f[i])%100==27) or (len(str(abs(f[i+1])))==4 and abs(f[i+1])%100==27) or (len(str(abs(f[i+2])))==4 and abs(f[i+2])%100==27):
        if sum([f[i]**2,f[i+1]**2,f[i+2]**2]) <= min([int(x) for x in f if len(str(abs(x)))==4 and x%17==0])**2:
            arr.append(abs(f[i])+abs(f[i+1])+abs(f[i+2]))
print(len(arr), min(arr))