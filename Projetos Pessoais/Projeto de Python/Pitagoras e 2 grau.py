# Write code below 💖
# Vamos começar pedindo o valor de a e b para o usuário
print("Vamos calcular a hipotenusa do triangulo retângulo!")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
# Agora vamos calcular a hipotenusa (queria fazer a pergunta: Os valores estão corretos?), mas posso fazer depois
c = (a**2 + b**2)**0.5
print(c)

# Agora vamos fazer uma equação do 2 grau!
print("Vamos calcular o valor das raizes em uma equação do 2 grau!")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)
