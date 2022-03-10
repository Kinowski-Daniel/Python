wysokosc = float(input("Podaj wysokosc w metrach: "))
waga = float(input("podaj swoja wage w kg: "))

bmi = waga/(wysokosc**2)

print("Twoje BMI wynosi: {0} i Masz: ".format(bmi), end='')

if (bmi < 16):
    print("mocna niedowaga")
elif ( bmi >= 16 and bmi < 18.5):
    print("Niedowaga")

elif( bmi >= 18.5 and bmi < 25):
    print("Zdrowa waga")

elif( bmi >= 25 and bmi < 30):
    print("Nadwaga")

elif ( bmi >=30):
   print("Duża Nadwaga")