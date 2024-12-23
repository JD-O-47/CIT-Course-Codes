
# Compounding Interest Loops | J.D Ogo | 11/22/24

#This loop takes the user input for the Original Deposit and makes sure a positive numeric value was set.
fDep = 0
while fDep <= 0:
    try:
        fDep = float (input ("What is the Original Deposit (positive value): "))
        if fDep <= 0:
            print ("Input must be a positive numeric value")
    except ValueError:
        print ("Input must be a positive numeric value")

#This loop takes the user input for the Interest Rate and makes sure a positive numeric value was set.
fIntRat = 0
while fIntRat <= 0:
    try:
        fIntRat = float (input ("What is the Interest Rate (positive value): "))
        if fIntRat <= 0:
            print ("Input must be a positive numeric value")
    except ValueError:
        print ("Input must be a positive numeric value")

#This loop takes the user input for how many Months and makes sure a positive numeric value was set.
iMonth = 0
while iMonth <= 0:
    try:
        iMonth = int (input ("What is the Number of Months (positive value): "))
        if iMonth <= 0:
            print ("Input must be a positive numeric value")
    except ValueError:
        print ("Input must be a positive numeric value")

#This loop takes the user input for the Goal Amount and makes sure a numeric value either equal or greater than zero was set.
fGoal = -1
while fGoal < 0:
    try:
        fGoal = float (input ("What is the Goal Amount (can enter 0 but not negative): "))
        if fGoal < 0:
            print ("Input must be 0 or greater")
    except ValueError:
        print ("Input must be 0 or greater")

#The top command is the formula for the Monthly Interest Rate, and the bottom two commands set up the next two loop formulas.
fMonIntRat = float (fIntRat/100/12)
fBal = fDep
fSavBal = fDep

#This loop was a NIGHTMARE for me to figure out, but its finally done! Wooohoo! This is a for loop that uses the range function so it keeps doing the given formula and print command for the balance.
iTotalMonth = 0
for iTotalMonth in range (1, iMonth + 1):
    fInterest = fBal * fMonIntRat
    fBal += fInterest 
    print ("Month: " + '\t' + format (iTotalMonth) + "  Account Balance is: $ " + format ((fBal), ',.2f'))

#The final loop... uses fSavBal instead of fBal for the formula, and gives the amount of months needed to reach the Goal Amount (fGoal). 
iTotalMonth = 0
while fSavBal < fGoal:
    fInterest = fSavBal * fMonIntRat
    fSavBal += fInterest
    iTotalMonth = iTotalMonth + 1
    if fSavBal >= fGoal:
       print ("It will take: " + '\t' + format (iTotalMonth) + "  months to reach the goal of $ " + format ((fGoal), ',.2f'))




   
