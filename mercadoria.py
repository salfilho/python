preco = float(input("Valor da mercadoria:"))
percentual = float(input("Qual o percentual do desconto:"))
desconto = preco * (percentual / 100)
print ("O valor do desconto é: %5.2f" % desconto, " reais")
preco_final = preco - desconto
print ("O valor final da mercadoria é: %5.2f" % preco_final, " reais")