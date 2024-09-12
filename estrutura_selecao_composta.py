idade = int(input("Digite sua idade: "))
""" 
Este programa mostra a faixa etária.
"""

if idade < 18: # Esta é a primeira condição.
    print("Menor de idade") # Menor de idade.
elif 18 <= idade < 60: #
    print("Adulto")
else:
    print("Idoso")