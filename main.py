# Assignment 1
# ICS3U
# <Alex Harris>
# March 28, 2018

###### uncomment this when you are ready to work on it
#def CtoF ():
#

###### uncomment this when you are ready to work on it
#def FtoC ():
#
def CtoF(C):
    """Input a temperature in Celicius to return a temperature in Fahrenheit
        C=Temperature in Celsius"""
    F = (1.8)*C+32

    if C<-273.15:
        return ("Invalid entry")

    else:
        return (F)

def FtoC(F):
    """Input a temperature in Fahrenheit to return a temperature in Celsius
        F=Temperature in Fahrenheit"""
    C = (0.55556)*(F-32)

    if F<-459.67:
        return ("Invalid entry")

    else:
        return (C)





pick = int(input('Enter 1 for Celsius or 2 for Fahrenheit: '))

if pick == 1:

    temperature = int(input('Enter your temperature in Celsius: '))
    print(CtoF(temperature))

elif pick == 2:

    temperature = int(input('Enter your temperature in Fahrenheit: '))
    print(FtoC(temperature))

else:
    print("learn how to count shithead")
