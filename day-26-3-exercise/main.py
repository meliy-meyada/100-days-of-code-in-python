

# Write your code above 👆
with open("file1.txt") as file1:
    f_1 = file1.readlines()
with open("file2.txt")as file2:
    f_2 = file2.readlines()
result = [int(n) for n in f_1 if n in f_2]    


print(result)


