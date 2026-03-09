n1 = float(input("Digite um numero: "))
n2 = float(input("Dgitie outro numero:"))

op = input("Digite a operação desejada: +, -, *, /: ")

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    if n2 !=0:
        resultado =  n1 / n2
    else: 
        resultado = "Erro: Divisão por zero"

print(resultado)

