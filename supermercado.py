listaCompra = []
listaCaixa = []
print(">>>>>>>>>> Mercadinho BigBom <<<<<<<<<<\n")
compra = int(input("Deseja iniciar um registro? 1 - Sim, 2 - Não: "))

while compra != 2:
  valor = float(input("Digite um valor: RS "))
  listaCompra.append(valor)
  if valor == 0:
    listaCompra.remove(0)
    listaCaixa.append(sum(listaCompra))
    print("")
    for i in range(len(listaCompra)):
      print("Produto {}: R$: {}" .format([i + 1], listaCompra[i]))

    print(f"\nValor a pagar: R$ {sum(listaCompra)}")
    pagar = float(input("\nDinheiro: R$ "))
    troco = pagar - sum(listaCompra)
    print("Troco: R$ {}" .format(round(troco, 2)))
    listaCompra = []

    compra = int(input("\nDeseja iniciar um registro?: 1 - Sim, 2 - Não: "))
    if compra == 1:
      continue
    else:
      print("\nTotal de transações do caixa: {}." .format(len(listaCaixa)))
      print("Valor total do caixa: R$ {}." .format(sum(listaCaixa)))
