sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

words = sentence.split(" ")
result = {ws : len(ws) for ws in words}

print(result)

