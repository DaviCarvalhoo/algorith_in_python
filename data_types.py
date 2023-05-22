import os
type = "sum"
os.system(f"figlet  -f ~/fonte_banner/figlet-fonts/3d.flf {type} | lolcat")
#enter a number
n1 = int(input("Digite um numero: "))
#enter another number
n2 = int(input("Digite outro numero: "))
#print result
print(f"A soma dos numeros é: {n1 + n2}")
