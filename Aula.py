import math

def area_triangulo(base, altura):
    area_triangulo = (base * altura)/2

base = float(input("coloque o valor da base do triangulo: "))
altura = float(input("coloque o valor da altura: "))
def mult():
    print(area_triangulo(base,altura))
mult()

print("  ")

print(" -"*30)
print("       Vinheria Agnello")
print(" -"*30)
print("")
print(" -"*30)
print("       Promoção de vinhos - queima de estoque")
print(" -"*30)

print("  ")
print("  ")


def linha_separacao():
    return print(" -"*30)
linha_separacao()
print("       Vinheria Agnello")
linha_separacao()
print("       Promoção de vinhos - queima de estoque")
linha_separacao()

print("  ")

def funcao():
    print("Bloco de código")
funcao()
funcao()


print("  ")


def imprime_nome(nome):
    print(f"Nome: {nome}")

imprime_nome("David D.")
imprime_nome("Luisa k.V")
imprime_nome("Victor H.")

print("  ")

#exercicio 1 - Crie uma funcao para calcular o dobro de um numero


def dobrar_numero():
    num1 = float(input("Digite um numero para saber o dobro: "))
    resultado = num1 * 2
    return resultado
print("O dobro do numero é: ",dobrar_numero())

print("  ")


#exercicio 2 - crie uma funcao que soma dois numeros inteiros
def somar_numero():
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero para ser somado: "))
    resultado = numero1 + numero2
    return resultado
print("A soma dos dois numeros é igual à",somar_numero())

print("  ")

#exercicio 3 - crie uma funcao que forneça o modulo de numero
def  valor_absolute():
    numero = float(input("digite um numero que vc queira saber o modulo: "))
    resultado = abs(numero)
    return resultado

print("o modulo do numero é: ",valor_absolute())

print("  ")

#exercicio 4 - crie uma funcao que forneça o quadrado do numero
def quadrado_do_n():
    numero = float(input("Digite um numero que deseja saber o quadrado desse numero: "))
    resultado = numero ** 2
    return resultado

print("O modulo do numero é",quadrado_do_n())

print("  ")

#exercicio 5 - crie um codigo para calcular o fatorial de um numero
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
n = int(input("digite um numero que vc quer calcular o fatorial: "))

print("o fatorial de",n,"é", fatorial(n))

print("  ")

#exercicio 6 - crie uma funcao que retorna o maior entre dois numeros
def busca_maior():
    print("Para saber qual é o maior entre eles")
    numero1 = float(input("digite o primeiro numero: "))
    numero2 = float(input("digite o segundo numero: "))
    if numero1 > numero2:
        return numero1
    else:
        return numero2

print("O maior numero é: ",busca_maior())

print("  ")

#exercicio 7 - crie uma funcao que retorne o antecessor do numero
def busca_antecessor():
    numero = float(input("digite um numero para saber o antecessor dele: "))
    antecessor = numero - 1
    return antecessor
print("o antecessor é: ",busca_antecessor())

print("  ")

#exercicio 8 - crie uma funcao que retorna o menor entre dois numeros
def busca_menor():
    numero1 = float(input("digite um numero: "))
    numero2 = float(input("digite um numero para descobrir qual é o menor entre eles: "))
    if numero1 < numero2:
        return numero1
    else:
        return numero2
print("o menor numero é",busca_menor())

#exercicio 9 - crie uma funcao que verifica se um numero é par
def busca_par():
    numero1 = float(input("digite um numero para saber se ele é par: "))
    if numero1 % 2 == 0:
        return print("o numero é par!")
    else:
        return print("o numero é impar!")

print(busca_par())


#exercicio 10 - crie uma funcao para calcular a raiz quadrada de um numero
import math

def calcular_raiz():
    numero = float(input("digite um numero para saber a raiz quadrada: "))
    raiz_quadrada = math.sqrt(numero)
    return raiz_quadrada

print("a raiz quadrada é "calcular_raiz())

print("  ")

#exercicio 11 - crie um codigo para somar dois numeros complexos

def somar_n_complexos(num1, num2):
    real = num1[0] + num2[0]
    imaginaria = num1[1] + num2[1]
    resultado = (real, imaginaria)
    return resultado

real1= float(input("digite a parte real do primeiro numero complexo: "))
imaginaria1 = float(input("digite a parte imaginaria do numero complexo: "))

real2 = float(input("digite a parte real do segundo numero complexo"))
imaginaria2 = float(input("digite a parte imaginaria do segundo numero complexo: "))

num1 = (real1, imaginaria1)
num2 = (real2, imaginaria2)

soma = somar_n_complexos(num1,num2)

print("a soma dos numeros é", soma)


print("  ")


#exercicio 12 - crie um codigo completoe detalhado que retorne as duas raizes de
# uma equacao de segundo grau usando a formula de baskhara

def calcular_raizes(a , b , c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante0)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante0)) / (2*a)
        return raiz1, raiz2

    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz, raiz
    else:
        parte_real = -b/(2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, parte_imaginaria)
        return raiz1, raiz2

coeficiente_a = float(input("digite o coeficiente a: "))
coeficiente_b = float(input("digite o coeficiente b: "))
coeficiente_c = float(input("digite o coeficiente c: "))

raiz1, raiz2 = calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c)

print("A raizes da equacao sao: ")
print("Raiz 1: ", raiz1)
print("Raiz 2: ", raiz2)