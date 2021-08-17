

nome_do_funcionario = input("Qual o nome do funcionário?:")
horas_trabalhadas = float(input("Quantas horas esse funcionário trabalhou esse mês:"))
valor_da_hora = float(input("Quanto esse funcionário recebe por hora?:"))
salario_bruto = (valor_da_hora * horas_trabalhadas)
print("Salário bruto:", salario_bruto)
desconto_inss = (salario_bruto *9/100)
print("Desconto INSS:", desconto_inss)
salario_liquido = (salario_bruto - desconto_inss)
print("Salário Líquido:", salario_liquido)


from time import sleep

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
l.reverse()
for i in l:
        sleep(3)
print ("Fim do programa :)")




