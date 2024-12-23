
# Lists and Real Estate Analyzer | J.D Ogo | 12/19/2024

# This function converts the user input string into a float while prompting them to input a number-
# greater than zero, meaning no letters. Exact same function from the PaintJob Assignment.
def getFloatInput(string):
    fNewValue = 0
    while fNewValue <= 0:
        try:
            sOldValue = input(string)
            fNewValue = float(sOldValue)
        except ValueError:
            print("Input a number that is greater than 0.")
    return float(sOldValue)

# This function gives the median from the Property List when called upon while taking account if the-
# list is odd or even in total entries.
def getMedian(sPropertyList):
    iTotalNumbers = len(sPropertyList)
    if iTotalNumbers % 2 != 0:
        fMedian = sPropertyList[int(iTotalNumbers/2)]
    else:
        fMedian = sPropertyList[int(iTotalNumbers/2)]
        fOtherMedian = sPropertyList[int((iTotalNumbers/2)-1)]
        fMedian = (fMedian + fSecondMedian)/2
    return float(fMedian)

# This is the main function, it houses everything else.
def main():
    sPropertyList = []
    sYesNo = "Y"
    while sYesNo != "N" and sYesNo != "n":
        if sYesNo == "Y" or sYesNo == "y":
            sPropertyValue = getFloatInput("Enter property sales value: ")
            sPropertyList.append(sPropertyValue)
            sYesNo = input("Enter another value Y or N: ")
        else:
            sYesNo = input("Enter another value Y or N: ")
            
# Sorts the Property List by smallest to greatest.
    sPropertyList.sort()
    
# Checks for every entry in the Property List and prints it out accordingly while numbering them.
# Trying to figure this out was the hardest part for me.
    for iEachProperty in range(len(sPropertyList)):
        print("Property " + str(iEachProperty + 1) + " $   "+ format((sPropertyList[iEachProperty]),',.2f'))
# Prints everything else.
    print(f"Minimum:    $    {min(sPropertyList):,.2f}")
    print(f"Maximum:    $    {max(sPropertyList):,.2f}")
    print(f"Total:      $    {sum(sPropertyList):,.2f}")
# Gets the average by totaling the list and dividing by how many entries there are.
    fAverage = sum(sPropertyList)/len(sPropertyList)
    print(f"Average:    $    {fAverage:,.2f}")
    print(f"Median:     $    {getMedian(sPropertyList):,.2f}")
# Gets the commission by totaling the list and multiplying it by .03 as stated.
    fCommission = sum(sPropertyList)*.03
    print(f"Commission: $    {fCommission:,.2f}")

# Calls the main function.
main()

# This assignment was so much easier than the last one, thank you very much! Somehow still ended up spending lots of time on it...
