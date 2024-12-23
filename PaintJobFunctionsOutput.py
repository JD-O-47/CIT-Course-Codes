
# Paint Job with Functions and Output Files | J.D Ogo | 12/6/2024

#First function takes string inputs from the user and converts them to floats.
def getFloatInput(string):
    fNewValue = 0
    while fNewValue <= 0:
        try:
            sOldValue = input(string)
            fNewValue = float(sOldValue)
        except ValueError:
            print("Input must be a positive numeric value greater than zero. Please try again.")
    return float(sOldValue)
#If an actual string of words is inputed then a message will appear asking to redo your input. Same with negative numbers or zeros.


#Second function and the main, this is where all the questions are given for the user and variables are made. Utilizes the first function. 
def main():
    fWallSpace = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborPrice = getFloatInput("Labor charge per hour: ")
    sJobState = input("State job is in: ")
    sLastName = input("Customer Last Name: ")
    
#Calls the final two functions because I was having lots and lots of trouble figuring out all the parameters and dealing with "undefined" errors on everything once I tried adding the main and showFinalEstimate functions.
    showCostEstimate(fWallSpace, fPaintPrice, fFeetPerGallon, fLaborPerGallon, fLaborPrice, sJobState)
    createFile(sLastName)

#This function gives you how many gallons of paint you need, while also rounding and turning the variable into an int (because whole cans).
def getGallonsOfPaint(fWallSpace,fFeetPerGallon):
   fGallonsNeeded = fWallSpace/fFeetPerGallon
   iGallonsNeeded = int(round(fGallonsNeeded))
   return int (iGallonsNeeded)

#This function calculates the labor hours.
def getLaborHours(fLaborPerGallon,iGallonsNeeded):
    fLaborHours = fLaborPerGallon*iGallonsNeeded
    return float (fLaborHours)

#This function gets the total paint cost.
def getPaintCost(fPaintPrice,iGallonsNeeded):
    fPaintCharges = fPaintPrice*iGallonsNeeded
    return float (fPaintCharges)

#This function gets the total labor cost.
def getLaborCost(fLaborPrice,fLaborHours):
    fLaborCharges = fLaborPrice*fLaborHours
    return float (fLaborCharges)

#Using whatever you inputed, it decides if you have extra state tax or not, and then calculates it together with the other charges.
def getSalesTax(sJobState,fPaintCharges,fLaborCharges):
    if sJobState == "CT":
        fStateTax = .06
    elif sJobState == "MA":
        fStateTax = .0625
    elif sJobState == "ME":
        fStateTax = .085
    elif sJobState == "NH":
        fStateTax = .0
    elif sJobState == "RI":
        fStateTax = .07
    elif sJobState == "VT":
        fStateTax = .06
    else:
        fStateTax = 0
    fSalesTax = ((fPaintCharges + fLaborCharges)*fStateTax)
    return float(fSalesTax)

#Calculates everything altogether and prints it all out nicely.
def showCostEstimate(fWallSpace, fPaintPrice, fFeetPerGallon, fLaborPerGallon, fLaborPrice, sJobState):
    iGallonsNeeded = getGallonsOfPaint(fWallSpace,fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborPerGallon,iGallonsNeeded)
    fPaintCharges = getPaintCost(fPaintPrice,iGallonsNeeded)
    fLaborCharges = getLaborCost(fLaborPrice,fLaborHours)
#I spent hours trying to get the parameters for fSalesTax to work...
    fSalesTax = getSalesTax(sJobState,fPaintCharges,fLaborCharges)
    fTotalCost = fPaintCharges+fLaborCharges+fSalesTax
    
    print(f"Gallons of paint: {iGallonsNeeded}")
    print(f"Hours of labor: {fLaborHours}")
    print("Paint charges: $"+ format ((fPaintCharges),',.2f'))
    print("Labor charges: $"+ format ((fLaborCharges),',.2f'))
    print("Tax: $"+ format ((fSalesTax),',.2f'))
    print("Total cost: $"+ format ((fTotalCost),',.2f'))

#Creates a file with the last name the user entered. I am not exactly sure if I did this part right.
def createFile(sLastName):
    sCustomerFile = open(sLastName + "_PaintJobOutput.txt", 'w')
    print(f"File: {sLastName}_PaintJobOutput.txt was created.")

#Calls the main function.
main()

#Extra comments: I thought this would be a lot easier and simplier after reading through the book and watching the lectures but getting the parameters and functions to work properly-
#without any errors was seriously frustrating and nightmarish to me. I was able to do some things really fast and efficient but the smallest of things gave me the biggest problems.

    
