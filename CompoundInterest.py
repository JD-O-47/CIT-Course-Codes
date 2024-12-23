
#  Compound Interest | J.D Ogo | 10/10/2024

#The Principal Investment is PV
PV = float (input ('Enter the starting principal: '))

#The Interest Rate is R
R = float (input ('Enter the annual interest rates: '))

#Compounding is m
m = int (input ('How many times per year is the interest compunded? '))

#t is the Number of Periods
t = float (input ('For how many years will the account earn interest? '))

#This part of code converts R into a decimal (Rx), which later gets divided by m (Ry), and finally added with +1 following the formula (Rz).
Rx = R / 100
Ry = Rx / m
Rz = Ry + 1

#This is part of the formula for FV.
mt = m * t

#This is the formula for FV, Future Value, which combines PV, Rz, and mt.
FV = PV * Rz ** mt
FV2 = (format(FV, '.2f'))

#This will return the output of everything put together.
print ('At the end of ' + (format(t)) + ' years you will have $ ' + (format(FV2))) 
