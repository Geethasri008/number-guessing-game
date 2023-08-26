import random
import math

lower=int(input("Enter lower bound: "))
upper=int(input("Enter upper bound: "))

x=random.randint(lower,upper)
count=0
limit=round(math.log(upper - lower +1,2))
print("You have only",limit,"chances to guess the number!")
while count<limit :
  count+=1
  guess=int(input("\nGuess the number:"))
 
  if x==guess:
    print("\nCongratulations you did it in",count,"try")
    break
  elif x>guess:
    print("you guessed too small!")
  elif x<guess:
    print("you guessed too high!")

if count>=limit:
  print("\nyour chances are over the number is %d" %x)
  print("Better luck next time!")