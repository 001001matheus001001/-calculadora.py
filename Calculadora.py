#Script Calculadora Feito por Matheus Silva
#30/01/2018 Hs 01:57
#Dependencias LINUX/GNU python 3
print("Calculadora.py")
# Pede ao usuario que forneça um problema matematico
problem = input("entre com um problema matematico, ou PRESS 'q' para Sair: ")
#Continua ate que o usuario entre com o problema matematico ou press 'q' para sair
while (problem != "q"):
    #Apresenta o problema, e mostra a resposta usando eval()
    print("A resposta é ", problem, "é -> :", eval(problem) )
    #pede outro problema matemático
    problem = input("Entre com outro problema, ou press 'q' para sair :")
    # Este laço while continuará ate voce entrar com q para sair