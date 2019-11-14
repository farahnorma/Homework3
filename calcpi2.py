#Norma
#calcpi2
import math

num_terms = int(input("Number of terms: "))

def estimate():
  sum = 0
  sign = -1.0
  for count in range(num_terms):
    sign = -1*sign
    term = sign / (2 * count + 1)
    sum += term
  return sum

pi_estimate = estimate()
z = 4*pi_estimate
error = abs(math.pi-z)

print(" approx. Pi is: ", z, "error:" , error)
