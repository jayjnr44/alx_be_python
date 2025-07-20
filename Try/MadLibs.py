noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")

story = f"One day, a {adjective} {noun} decided to {verb} at the {place}. Suddenly, a {animal} appeared! "

# Conditional touch
if animal.lower() == "dragon":
    story += "It breathed fire and everyone ran away!"
elif adjective.lower() == "funny":
    story += "Everyone laughed so hard that they fell over!"
else:
    story += f"The {animal} and the {noun} became friends and had a great adventure."

print("\nYour Mad Libs story:")
print(story)


