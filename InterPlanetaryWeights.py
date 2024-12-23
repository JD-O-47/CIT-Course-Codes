
# Inter Planetary Weights | J.D Ogo | 10/11/2024


#Name and Weight inputs.
sName = str (input ('What is your name: '))
nWeight = float (input ('What is your weight: '))

#These are my named constants so no magic numbers.
MERCURY_WEIGHT = 0.38
VENUS_WEIGHT = 0.91
MOON_WEIGHT = 0.165
MARS_WEIGHT = 0.38
JUPITER_WEIGHT = 2.34
SATURN_WEIGHT = 0.93
URANUS_WEIGHT = 0.92
NEPTUNE_WEIGHT = 1.12
PLUTO_WEIGHT = 0.066

#These get the weight for each planet using the formula given.
nMercury = nWeight * MERCURY_WEIGHT
nVenus = nWeight * VENUS_WEIGHT
nMoon = nWeight * MOON_WEIGHT
nMars = nWeight * MARS_WEIGHT
nJupiter = nWeight * JUPITER_WEIGHT
nSaturn = nWeight * SATURN_WEIGHT
nUranus = nWeight * URANUS_WEIGHT
nNeptune = nWeight * NEPTUNE_WEIGHT
nPluto = nWeight * PLUTO_WEIGHT

#The final part of the code gives the output for what the user had entered above.
print (format (sName) + ''' here are your weights on our solar system's planets:''')
print ('Weight on Mercury:' + (format (nMercury, ' >14,.2f')))
print ('Weight on Venus:' + (format (nVenus, ' >16,.2f')))
print ('Weight on our Moon:' + (format (nMoon, ' >13,.2f')))
print ('Weight on Mars:' + (format (nMars, ' >17,.2f')))
print ('Weight on Jupiter:' + (format (nJupiter, ' >14,.2f')))
print ('Weight on Saturn:' + (format (nSaturn, ' >15,.2f')))
print ('Weight on Uranus:' + (format (nUranus, ' >15,.2f')))
print ('Weight on Neptune:' + (format (nNeptune, ' >14,.2f')))
print ('Weight on Pluto:' + (format (nPluto, ' >16,.2f')))
