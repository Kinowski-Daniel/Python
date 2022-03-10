
file=open("DDD.txt", "r")
print(file.readlines()[::2])
file.close()