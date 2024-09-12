idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif 18 <= idade < 60:
    print("Adulto")
else:
    print("Idoso")