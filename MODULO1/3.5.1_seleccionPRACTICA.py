from PIL import Image

img = Image.open('images.py/C3.5.1.png')
img.show()

#resolucion
tempCelsius = float(input())
tempFahrenheit = tempCelsius * (9/5) + 32 
print(tempCelsius,"grados Celsius en grados Fahrenheit es",tempFahrenheit)