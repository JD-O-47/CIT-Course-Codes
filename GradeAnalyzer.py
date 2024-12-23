
# Grade Analyzer | J.D Ogo | 11/1/2024

#Takes user input for name and the test scores.
sName = str (input ("Name of person that we are calculating the grades for: "))
nTest1 = int (input ("Test 1: "))
nTest2 = int (input ("Test 2: "))
nTest3 = int (input ("Test 3: "))
nTest4 = int (input ("Test 4: "))

#Takes user input on if they want to drop the lowest grade.
sDrop = str (input ("Do you wish to Drop the Lowest Grade Y or N? "))

#Automatically stopsthe program if any of the test scores are less than zero.
if nTest1 < 0 or nTest2 < 0 or nTest3 < 0 or nTest4 < 0:
    print ("Test scores must be greater than 0")
    exit()

#Makes sure you enter Y or N, otherwise the program stops. I made sure to include options for lowercase as well.
if sDrop != "Y" and sDrop != "N" and sDrop != "y" and sDrop != "n":
    print ("Enter Y or N to Drop the Lowest Grade.")
    exit()


#Saying yes, this part identifies and removes the lowest test score, while giving the average for the other 3 test scores.
if sDrop == "Y" or sDrop == "y":

    if nTest1 < nTest2 and nTest1 < nTest3 and nTest1 < nTest4:
        nAverage = float ((nTest2 + nTest3 + nTest4)/3)

    elif nTest2 < nTest1 and nTest2 < nTest3 and nTest2 < nTest4:
        nAverage = float ((nTest1 + nTest3 + nTest4)/3)

    elif nTest3 < nTest1 and nTest3 < nTest2 and nTest3 < nTest4:
        nAverage = float ((nTest1 + nTest2 + nTest4)/3)

    elif nTest4 < nTest1 and nTest4 < nTest2 and nTest4 < nTest3:
        nAverage = float ((nTest1 + nTest2 + nTest3)/3)


#Saying no, it will calculate the average of all 4 test scores.
if sDrop == "N" or sDrop == "n":
    nAverage = float ((nTest1 + nTest2 + nTest3 + nTest4)/4)


#This is a list of all the magic numbers, renamed.
#Grade A+
GRADE_A1 = float (97.0)
#Grade A
GRADE_A2 = float (96.9)
GRADE_A3 = float (94.0)
#Grade A-
GRADE_A4 = float (93.9)
GRADE_A5 = float (90.0)
#Grade B+
GRADE_B1 = float (89.9)
GRADE_B2 = float (87.0)
#Grade B
GRADE_B3 = float (86.9)
GRADE_B4 = float (84.0)
#Grade B-
GRADE_B5 = float (83.9)
GRADE_B6 = float (80.0)
#Grade C+
GRADE_C1 = float (79.9)
GRADE_C2 = float (77.0)
#Grade C
GRADE_C3 = float (76.9)
GRADE_C4 = float (74.0)
#Grade C-
GRADE_C5 = float (73.9)
GRADE_C6 = float (70.0)
#Grade D+
GRADE_D1 = float (69.9)
GRADE_D2 = float (67.0)
#Grade D
GRADE_D3 = float (66.9)
GRADE_D4 = float (64.0)
#Grade D-
GRADE_D5 = float (63.9)
GRADE_D6 = float (60.0)
#Grade F
GRADE_F = float (59.9)


#This part of the code calculates what the Grade Letter will be using the average.
if nAverage > GRADE_A1:
    sGradeLetter = str ("A+")
elif nAverage < GRADE_A2 and nAverage > GRADE_A3:
    sGradeLetter = str ("A")
elif nAverage < GRADE_A4 and nAverage > GRADE_A5:
    sGradeLetter = str ("A-")
elif nAverage < GRADE_B1 and nAverage > GRADE_B2:
    sGradeLetter = str ("B+")
elif nAverage < GRADE_B3 and nAverage > GRADE_B4:
    sGradeLetter = str ("B")
elif nAverage < GRADE_B5 and nAverage > GRADE_B6:
    sGradeLetter = str ("B-")
elif nAverage < GRADE_C1 and nAverage > GRADE_C2:
    sGradeLetter = str ("C+")
elif nAverage < GRADE_C3 and nAverage > GRADE_C4:
    sGradeLetter = str ("C")
elif nAverage < GRADE_C5 and nAverage > GRADE_C6:
    sGradeLetter = str ("C-")
elif nAverage < GRADE_D1 and nAverage > GRADE_D2:
    sGradeLetter = str ("D+")
elif nAverage < GRADE_D3 and nAverage > GRADE_D4:
    sGradeLetter = str ("D")
elif nAverage < GRADE_D5 and nAverage > GRADE_D6:
    sGradeLetter = str ("D-")
else: 
    sGradeLetter = str ("F")


#The final outputs for all of the entered and calculated data.
print (sName + " test average is: " + format ((nAverage), '.1f'))
print ("Letter Grade for the test is: " + format (sGradeLetter))

