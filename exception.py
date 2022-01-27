import sys
 # exception Handling 
 
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("dont use letter") # if erro tell user this error 
    sys.exit(1)

try:
  new = x / y

except ZeroDivisionError:
    print("Error: cannot divide by 0")
    sys.exit(1) 


print(f"the {x} / {y} the result is {new}") # dont forget add f

# to hand Error we use exception
# we use try


