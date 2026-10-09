num = int(input("Digite um numero: "))
print("""[1] Binário
[2] Octal
[3] hexagonal""")
opcao = int(input("Digite a opção: "))
if opcao == 1:
    print("{} em binário é {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} em octal é {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} em hexagonal é {}".format(num, hex(num)[2:]))

