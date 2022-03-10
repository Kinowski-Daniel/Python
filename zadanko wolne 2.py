
metry = float(input("Podaj ilośc w metrach: "))
wybor = float(input("1- na centymetry, 2- milimetry, 3- kilometry : "))
centymetry = metry / 0.01
milimetry  = metry / 0.001
kilometry = metry / 1000.0

if(wybor == 1):
    print(f"metry({metry}) => Centymetry({centymetry})")

if(wybor == 2):
    print(f"metry({metry}) => Milimetry({milimetry})")


if(wybor == 3):
    print(f"metry({metry}) => Kilometry({kilometry})")

