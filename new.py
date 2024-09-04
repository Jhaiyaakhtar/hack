import random
import datetime 
import os
print(os.system("clear"))
print("    ",datetime.datetime.now())
print("\n")
def run():
  r = random.randint(0,100)
  c = 10
  while True:
    g = int(input('     Enter Your Guess Number: '))
    if r > g:
      print("\n")    
      print("    please try again..low..\n")
      c -=1
      print(f"       YOUR CHANCE = {c}")
      if c == 0:
        break
      continue
    elif r < g:
      print("\n")    
      print("    Please try again...high..\n")
      c -=1
      print(f"       YOUR CHANCE = {c}")
      if c == 0:
        break
      continue
    else:
      print("\n")    
      print("    You are win Congratulations..❤️❤️")
      break
run()
      
        
      
  
