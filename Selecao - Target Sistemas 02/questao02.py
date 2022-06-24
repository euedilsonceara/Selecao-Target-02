#QUESTÃO 02

numero = int(input("Insira um numero: "))
fibonacci = [0,1]

while numero > fibonacci[-1]:
  fibonacci.append(fibonacci[-1]+fibonacci[-2])
  
if numero in fibonacci:
  print("O número pertence à sequência de Fibonacci")
else:
  print("O número não pertence à sequência de Fibonacci")