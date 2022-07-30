# the code below has a FIZZBUZZ method that prints out the numbers 1 through 100
# Instead of numbers divisible by 3, the method should output "Fizz"
# Instead of numbers divisible by 5, the method should output "Buzz".
# Instead of numbers divisible by 3 and 5, the method should output "FizzBuzz".

def FIZZBUZZ():
    for fizzbuzz in range(101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)


print(FIZZBUZZ())

# the code below has a FIZZBUZZ method that prints out the numbers 1 through 100
# Instead of numbers with a three in them, print "Fizz".
# Instead of numbers with a five in them, print "Buzz".
# Instead of numbers with a three and a five in them, print "FizzBuzz".




