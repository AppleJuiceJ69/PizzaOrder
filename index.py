print('pizza order')

#pizza size prices
small = 15
medium = 20
large = 25

#price of toppings
small_toppings = 1
large_toppings = 2
cheese = 1

#set false so you can change to true when need be
toppings = False
extra_cheese = False

#inputs
size = input('Enter the size you would like: S, M, L ')

toppings = input("Extra toppings: Y or N " )

extra_cheese = input('would you like extra cheese: Y or N ')

# size = s, then small, size = m, size = medium, size = l, size = large
# toppings = yes, add on to size, toppings = no, don't add anything to size, if we keep these both seperate from size then it will save code
# extra_cheese = true, add on to size false, don't add on to size 
# then print out total once all calculations are meant, or possibilities are done. 

#set to true so that we can use that in our code 
if toppings == 'y':
    toppings = True
else:
    toppings = False

if extra_cheese == 'y':
    extra_cheese = True
else: 
    extra_cheese = False
    
    
#small pizza
if size == 's' and toppings == True and extra_cheese == True:
    print(small + small_toppings + cheese, f"dollars")
elif size == 's' and toppings == True:
    print(small + small_toppings, f"dollars")
elif size == 's':
    print(small, f"dollars")

#medium pizza
if size == 'm' and toppings == True and extra_cheese == True:
    print(medium + large_toppings + cheese , f"dollars")
elif size == 'm' and toppings == True:
    print(medium + large_toppings, f"dollars")
elif size == 'm':
    print(medium, f"dollars")

#large pizza
if size == 'l' and toppings == True and extra_cheese == True:
    print(large + large_toppings + cheese , f"dollars")
elif size == 'l' and toppings == True:
    print(large + large_toppings, f"dollars")
elif size == 'l':
   print(large, f"dollars")


    