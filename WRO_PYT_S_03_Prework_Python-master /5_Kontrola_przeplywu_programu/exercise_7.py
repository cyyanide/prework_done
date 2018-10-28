tab= []
x= int(input("ile liczb: "))

for i in range (x):
    y=int(input("liczba:"))
    tab. append(y)

suma = sum(tab)
srednia = sum(tab)/x

print(suma)
print(srednia)

if suma >srednia:
    print ("suma wieksza od sredniej")

else:
    print ("srednia wieksza od sumy")


""" 
Napisz program, który:

przyjmie od użytkownika informację ile liczb ten chce wprowadzić
przyjmie X liczb (gdzie X - podane przez użytkownika)
policzy ich sumę i średnią
wypisze na ekran te liczby i czy suma jest większa od średniej (postaci "Suma: X, średnia: X, suma jest większa!")

"""
