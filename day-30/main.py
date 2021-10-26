# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} dose not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up")

height = float(input("Height: "))
weight = int(input("weight: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height **2
print(round(bmi))