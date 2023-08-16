import pandas as pd

cliente = input("Introduzca un nuevo cliente[+] ")
opcion = input("¿Quiere agregar más? ")

opcion2 = ""
cliente2 = ""
cliente3 = ""

if opcion == "si":
    cliente2 = input("Introduzca un nuevo cliente[+] ")
    opcion2 = input("¿Quiere agregar más? ")
    pago2 = input(f"{cliente2} ¿ha pagado? ")

if opcion2 == "si":
    cliente3 = input("Introduzca un nuevo cliente[+] ")
    print("Lo lamentamos, pero la tabla ya está llena.")
    pago3 = input(f"{cliente3} ¿ha pagado? ")

pago1 = input(f"{cliente} ¿ha pagado? ")

check1 = "x"
check2 = "x"
check3 = "x"

pago2=""
pago3=""
if pago1 == "si":
    check1 = "✓"

if pago2 == "si":
    check2 = "✓"

if pago3 == "si":
    check3 = "✓"

# Creación del DataFrame
df = pd.DataFrame({"columna1": [cliente, cliente2, cliente3], "columna2": [check1, check2, check3]})
print(df)

