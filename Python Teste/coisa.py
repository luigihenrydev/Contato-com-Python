num = int(input("Digite um número: "))
fib1 = 0
fib2 = 1
while fib2 < num:
    temp = fib2
    fib2 = fib1 + fib2
    fib1 = temp
if fib2 == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
