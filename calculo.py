
 


import math


opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los números elegidos
    5) Sacar raiz cuadrada del numero
    6) Exponente
    7) Seno
    8) Coseno
    9) Tangente
    00) apagar calculadora 
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
    elif opcion == 3:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print("RESULTADO: El Resultado de division de",n1,"/",n2,"es igual a",n1/n2)
    elif opcion == 5:
        n1 = float(input("Introduce tu primer número: ") )
        
        print(" ")
        print('La raíz cuadrada de {} es {} '.format(n1, math.sqrt(n1)))
    elif opcion == 6:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: Del Exponente  es",n1,"**",n2,"es igual a",n1**n2)
    elif opcion == 7:
        n1 = int(input("Introduce los radianes: ") )
        
        print(" ")
        print("El seno de {} es {}".format(n1, math.sin(n1)))
    elif opcion == 8:
        n1 = int(input("Introduce los radianes: ") )
      
        print(" ")
        print("El coseno de {} es {}".format(radianes, math.cos(radianes)))
    elif opcion == 9:
        n1 = float(input("Introduce tu primer número: ") )
        
        print(" ")
        print("La tangente de {} es {}".format(radianes, math.tan(radianes)))    
    elif opcion == 00:
        break
    else:
        print("Opción incorrecta")