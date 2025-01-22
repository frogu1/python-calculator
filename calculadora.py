vet_numeros = []
vet_operadores = []
vet_final = []
operador = ''
num_fatores = 0
operadores_maior_prioridade = ["*", "/"]
operadores_menor_prioridade = ["+", "-"]
i = 0
mult_ou_div = 0

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

            mult_ou_div = 1        
        else:
            vet_operadores.append(operador)
            i += 1

    operador = input("\nDigite um operador [+, -, *, /. ou = para terminar a operação.]: ")

if mult_ou_div == 1 :                                  # checa se houve multiplicação ou divisao na expressao
    for j in range (num_fatores+(num_fatores-1)) :         # codigo para "montar" o vetor vet_final, 
        if j % 2 == 0 :                                    # unindo os dois vetores anteriores
            vet_final.append(vet_numeros[int(j/2)])
        else:
            vet_final.append(vet_operadores[j//2])
else:
    for b in range (i) :
        if b % 2 == 0 :                            
            vet_final.append(vet_numeros[int(b/2)])
        else:
            vet_final.append(vet_operadores[b//2])

resultado = vet_final[0]  # variavel 'resultado' recebe o valor do primeiro numero da expressao

for k in range (1, len(vet_final), 2) :  # codigo para transformar as informações no 
    operador = vet_final[k]              # vet_final em expressao matemática
    numero = float(vet_final[k+1])

    if operador == "+" :
        resultado += numero
    elif operador == "-" :
        resultado -= numero


print(f"\n{resultado}")

end = input("digite enter para finalizar o programa.")
