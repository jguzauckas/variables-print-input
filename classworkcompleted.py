# In this classwork, we are going to practice some skills that incorporate the three pieces of today's lesson

# Perform a "magic trick" with numbers: Perform a set of operations on a number that will eventually
# return the number to its original state. We do this through opposite operations (i.e. + and -)
# If you give me 5 and I add 3, we get 8, then minus 3 is 5, the original number.
# Have the user enter a number (integer or float, your choice), and perform at least 4 different
# operations/assignments during the "magic trick". Each time you modify the number, print the result!

# For my sample magic trick I will use the four basic operations: +, -, *, //
# I'm using integer division because I want to use an integer and not turn it into a double by accident
num = int(input("Enter your favorite integer: "))
num += 10
print("Your number is now", num)
num *= 3
print("Your number is now", num)
num //= 3
print("Your number is now", num)
num -= 10
print("Your number was", num)

# Create a "mad libs" style short story (around 2 sentences)
# Example sentence: "My ______ is in _____ condition."
# In this sentence, the first blank needs to be a noun, and the second blank needs to be an adjective
# Use inputs/variables to get a noun and an adjective from the user and then use a complex print
# statement to incorporate them into the original sentence (so it looks like it was supposed to be there!)
# The user should not see the sentence beforehand, just ask them for the types of words you need!

# My story is "Mr. G was _(verb)_ the lesson for the day when he realized he forgot _(noun)_.
# To make up for it, he set up a(n) _(adjective)_ lesson for next class."
verb = input("Enter a verb: ")
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
print(
    "Mr. G was", verb, "the lesson for the day when he realized he forgot", noun + "."
)
print("To make up for it, he set up a(n)", adjective, "lesson for next class.")
