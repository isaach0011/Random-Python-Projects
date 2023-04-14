#Asks for input from user
reavers = int(input("How many Reavers: "))
units = int(input("How many units: "))

# Calculates amount of money given out for the party.
party = (reavers - 2) * 3
remainingunits = units - party

# Calculates Yondu's share
yshare = int(remainingunits * .13)
remainingunits = remainingunits - yshare

# Calculates Peter's share
pshare = int(remainingunits * .11)
remainingunits = remainingunits - pshare

# Calculates the crew's share
cshare = int(remainingunits / reavers)
yshare = yshare + cshare
pshare = pshare + cshare
remainingunits = remainingunits - (cshare * reavers)

rbfunits = remainingunits

#Prints outputs
print("Yondu's share:", yshare)
print("Peter's share:", pshare)
print("Crew's share:", cshare)
print("RBF:", rbfunits)