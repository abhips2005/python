print("Temperature Calculator")
choice=int(input("Choose the conversion you need to do: \n1.Degree Celcius to Degree Faranheit\n2.Degree Faranheit to Degree Celcius\n"))
if choice==1:
    celcius=float(input("Enter temperature in degree celcius: "))
    faranheit= (9/5*celcius)+32
    print(faranheit)
else:
    faranheit=float(input("Enter temperature in degree faranheit: "))
    celcius=5/9*(faranheit-32)
    print(celcius)