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
    """Input a temperature in Celicius to return a temperature in fahrenheit
        C=Temperature in Celsius"""
    F = (1.8)*C+32

    if C<-273:
        return ("Invalid entry")
    else:
        return (F) 

temperature = int(input('Enter your temperature in Celsius: '))
print(CtoF(temperature))
