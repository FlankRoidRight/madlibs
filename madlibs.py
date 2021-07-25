#name = "John"
#string concatenation
#print("Hello " + name)
#print("Hello {}".format(name))
#print(f"Hello {name}")

person1 = input("Person 1: ")
person2 = input("Person 2: ")
adj1 = input("Adjective 1: ")
adj2 = input("Adjective 2: ")
bodypart1 = input("Body Part 1: ")
bodypart2 = input("Body Part 2: ")
emotion1 = input("Emotion 1: ")
emotion2 = input("Emotion 2: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
madlib = f"{person1} loves {person2}. \
{person1} loves {person2}’s {adj1} {bodypart1}. \
However, {person2} does not like {person1}’s {adj2} {bodypart2}. \
{person1} likes to pat his {adj2} {bodypart2}, \
and this makes {person2} angry. \
Also, {person2} wants to {verb1} and {verb2} with {person1}, \
but {person1} is sometimes too {emotion1} to do this. \
So {person2} starts to feel {emotion2}."

print(madlib)
