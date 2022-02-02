#Assume a suitable value for temperature of a city in Fahrenheit degrees. Write a 
#program to convert this temperature into centigrade degrees and print both temperature.

temp = float(input("Enter the temperature in farenheit:"))
C_temp = float(5/9*(temp-32))
print('Temperature in Farenheit is %.2f Farenheit'%(temp))
print('Temperature in centigrade is %.2f Centigrade'%(C_temp))
