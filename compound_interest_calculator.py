import math

amount = None
principal = None
interestRate = None
interestCompYearly = None
years = None

principal = input("What is your principal amount? ")
interestRate = input("What is the interest rate? ")
interestCompYearly = input("How often is interest calculated? ")
years = input("How many years will your account be active? ")

amount = float(principal)*(1 + (float(interestRate)/float(interestCompYearly))) ** (float(interestCompYearly) * float(years))

print(round(amount, 2))
