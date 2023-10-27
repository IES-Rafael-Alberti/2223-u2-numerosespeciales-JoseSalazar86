# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def parImpar(numero:int)-> bool:
    if numero %2 == 0:
        return True
    else:
        return False
    
def sumaPar(numero:int,suma:int) -> int :
    if numero %2 == 0:
        suma += parImpar(numero)
    return suma

def sumaImpar(numero:int,suma:int)-> int:
    if numero %2 !=0:
        suma += parImpar(numero)
    return suma
 

        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    opcion = input("¿Desea calcular la suma de pares o impares? (pares/impares): ")
    if opcion

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
