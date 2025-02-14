vet_numeros = []
vet_operadores = []
operador = ''
num_fatores = 0
operadores_maior_prioridade = ["*", "/"]
operadores_menor_prioridade = ["+", "-"]
i = 0

# nao aumentar o tamanho da lista se for mult/div

while operador != '=' :
    numero_digitado = float(input("\nDigite um número: "))
    i += 1
    vet_numeros.append(numero_digitado)
    num_fatores = len(vet_numeros)-1

    if ((operador in operadores_maior_prioridade) or (operador in operadores_menor_prioridade)) :
        if operador in operadores_maior_prioridade :
            if operador == "*" :
                vet_numeros[num_fatores-1] = vet_numeros[num_fatores-1] * vet_numeros[num_fatores]
                vet_numeros.pop(num_fatores)
            elif operador == "/"  and numero_digitado != 0 :
                vet_numeros[num_fatores-1] = vet_numeros[num_fatores-1] / vet_numeros[num_fatores]
                vet_numeros.pop(num_fatores)
        
        else:
            vet_operadores.append(operador)
            i += 1

    operador = input("\nDigite um operador [+, -, *, /. ou = para terminar a operação.]: ")

vet_resultado = []
for i in range(len(vet_numeros) + len(vet_operadores)) :
    if i % 2 == 0 :
        if i == 0 :    
            vet_resultado.append(vet_numeros[0])
        else:
            vet_resultado.append(vet_numeros[i//2])
    else:
        if i == 1:
            vet_resultado.append(vet_operadores[0])
        else:
            vet_resultado.append(vet_operadores[i//2])

resultado = eval(' '.join(map(str, vet_resultado)))

print(f"\n{resultado}") # calma

end = input("digite enter para finalizar o programa.")
