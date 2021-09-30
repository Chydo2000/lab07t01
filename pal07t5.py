balance = 2000
print("Bank account balance: " + str(balance) + " €")
euros = int(input("How many euros will be added to the balance? "))
cents = int(input("How many cents will be added to the balance? "))

balance += euros + (cents/100)

print("Bank account balance: " + str(balance) + " €")