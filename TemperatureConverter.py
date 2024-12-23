
# Temperature Converter | J.D Ogo | 10/17/2024

#Prints the name and purpose of the code.
print ('''J.D's Temp Converter: \n''')

#Asks the user to input some values.
nTemp = float (input ("Enter a temperature: "))
sTempType = str (input ("Is the temp F for Fahrenheit or C for Celsius? "))

#Checks if the user put F or C, lowercase included, otherwise stops the code.
if sTempType == 'C' or sTempType == 'c':
    sEqual = str ("Fahrenheit")
elif sTempType == 'F' or sTempType =='f':
    sEqual = str ("Celcius")
else:
    print ("Enter a F or C")
    quit()

#Converts the user input temperature to Fahrenheit if Celsius was used. If the value is higher than the limit it will stop the code.
if nTemp > 100 and (sTempType == 'C' or sTempType == 'c'): 
    print ("Temp can not be > 100")
    quit()
elif nTemp < 101 and (sTempType == 'C' or sTempType == 'c'):
    nTempEqual = (float (((9.0/5.0) * nTemp) + 32))

#Converts the user temperature to Celsius if Fahrenheit was used. If the value is higher than the limit it will stop the code.
if nTemp > 212 and (sTempType == 'F' or sTempType == 'f'): 
    print ("Temp can not be > 212")
    quit()
elif nTemp < 213 and (sTempType == 'F' or sTempType == 'f'):
    nTempEqual = (float ((5.0/9) * (nTemp - 32)))
    

#Gives back the final output of everything that was input
print ("The " + sEqual + " equivalent is: " + format ((nTempEqual), '.1f'))
