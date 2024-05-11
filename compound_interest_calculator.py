import math

amount = None
principal = None
intrestRate = None
intrestCompYearly = None
years = None

principal = input("What is your principal amount? ")
intrestRate = input("What is the intrest rate? ")
intrestCompYearly = input("How often is intrest calculated? ")
years = input("How many years will your account be active? ")

amount = float(principal)*(1 + (float(intrestRate)/float(intrestCompYearly))) ** float(years)

print(round(amount, 2))