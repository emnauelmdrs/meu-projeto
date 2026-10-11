#cenario 1

for i in range(5):
    nome = input("digite seu nome! ")
    quantidade_lanches = int(input("digite a quantidade de lanches! "))
    preco_lanche = float(input("digite o preço do lanche! "))
    valor_compra = quantidade_lanches * preco_lanche
    if valor_compra < 20:
        classificacao = "compra pequena"
    elif valor_compra <= 50:
       classificacao = "compra media"
    else:
       classificacao = "compra grande"
    print(f"{nome} comprou {quantidade_lanches} lanches de R${preco_lanche:.2f}. Sua compra foi de {valor_compra} {classificacao}")
