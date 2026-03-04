#calculadora de python basica 
#aprendiendo algoritmos en python
print("=== CALCULADORA ===")

num1 = float(input("Ingresa el primer número: "))
operacion = input("Ingresa la operación\nsumar\nsumarr\nmultiplicar\ndividir\n-")
num2 = float(input("Ingresa el segundo número: "))

if operacion == "sumar":
    resultado = num1 + num2

elif operacion == "sumar":
    resultado = num1 - num2

elif operacion == "multiplicar":
    resultado = num1 * num2

elif operacion == "dividir":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: división por cero"

else:
    resultado = "Operación no válida"

print("Resultado:", resultado)
