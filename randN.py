#Norma
#randN

import random

numRolls = int(input("Number: "))


def rand():
  sum = 0
  for count in range(numRolls):
    number = random.randint(1, 7)
    print("Number rolled: ", number)
    sum += number
  return sum


z = rand()
print("Total sum: ",z)
a = z/numRolls
print("Average: ", a)

#As numRolls gets larger we'd expect the average to get
# closer and closer to 3.5, which is the average of 1 and 6