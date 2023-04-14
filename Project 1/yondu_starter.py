"""
Project Name: 
Author: Isaac Hill
Due Date: 09/11/2020
Course: CS1400-X04

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

This program when giving the amount of pirates and gold, will split the gold between Yondu,
Peter, the Crew, and the fund.

"""


def main():
    """
    Program starts here.
    """
    try:
        # Asks for input from user
        reavers = int(input("How many Reavers: "))
        units = int(input("How many units: "))

    except ValueError:
        print("Enter postive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # Calculates amount of money given out for the party.
    party = (reavers - 2) * 3
    remainingunits = units - party

    # Calculates Yondu's share
    yshare = int(remainingunits * 0.13)
    remainingunits = remainingunits - yshare

    # Calculates Peter's share
    pshare = int(remainingunits * 0.11)
    remainingunits = remainingunits - pshare

    # Calculates the crew's share
    cshare = int(remainingunits / reavers)
    yshare = yshare + cshare
    pshare = pshare + cshare
    remainingunits = remainingunits - (cshare * reavers)

    rbfunits = remainingunits

    # Prints outputs
    print("Yondu's share:", yshare)
    print("Peter's share:", pshare)
    print("Crew's share:", cshare)
    print("RBF:", rbfunits)


if __name__ == "__main__":
    main()
