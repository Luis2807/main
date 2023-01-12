import math

def calculate():
    operation = input('''
Ingresa el numero para realizar la operacion:
 1 Sumar
 2 Restar
 3 Multiplicar
 4 Dividir
 5 Raiz n
 6 Exponente n
 7 Seno
 8 Coseno
 9 Tangente
''')

    number_1 = int(input('Inngresa el primer numeror: '))
    number_2 = int(input('Ingresa el segundo numero: '))
    


    if operation == '1':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '2':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '3':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '4':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '5':
        
        print('La raíz cuadrada de {} es {} '.format(number_1, math.sqrt(number_1)))
        
    elif operation == '6':
        print('El exponente es:', number_1**number_2)
        
    elif operation == '7':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '8':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '9':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)


    else:
        print('You have not typed a valid operator, please run the program again.')
        

# Call calculate() outside of the function
calculate()