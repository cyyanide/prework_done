print ("Równanie w postaci ax**2 + bx + c == 0")


a=int(input('podaj wartość parametru a: '))
b=int(input('podaj wartość parametru b: '))
c=int(input('podaj wartość parametru c: '))

delta = b**2-4*a*c

if delta > 0:
    x1 = (-b-delta**(1/2))/(2*a)
    x2 = (-b+delta**(1/2))/(2*a)
    print ("x1 = ")
    print (x1)
    print ("x2= ")
    print (x2)


elif delta == 0:
    x0 = -b/(2*a)
    print ("x0 = "), x0


else:
    print ("brak rozwiązań")







# if (b ** 2 - 4 * a * c) > 0
    # print (x1= )

# if  (b ** 2 - 4 * a * c) < 0
  #   print ("Delta jest ujemna")





# Napisz program do pomocy licealistom w liczeniu pierwiastków równań kwadratowych. Program ma:

# wyświetlić na ekranie komunikat: "Równanie w postaci ax**2 + bx + c == 0",
# wyświetlić na ekranie komunikat: "Podaj a",
# wyświetlić na ekranie komunikat: "Podaj b",
# wyświetlić na ekranie komunikat: "Podaj c",
# Policzy deltę i wyznaczy wartości x_1 i x_2. Jeśli delta >= 0, program ma wyświetlić x_1,2 = wartość.
# Uwaga Nie musisz sprawdzać czy wejście jest poprawne.

# Jeżeli delta jest ujemna, wypisz na ekran odpowiednią informację.