compra = float(input("Preço das compras:R$ "))
print('{:=^40}'.format(" LOJA DARITA "))
print("FORMA DE PAGAMENTOS"
      "\n[1] A VISTA DINHEIR/CHEQUE"
      "\n[2] A VISTA CARTÃO"
      "\n[3] 2X NO CARTÃO"
      "\n[4] 3X NO CARTÃO"
      "")

print("="*40)
opcao = int(input("Qual sua opcao: "))

print("="*40)
if opcao == 1:
    desconto = compra - (compra * 0.20)
    print(f"O valor a vista e: {desconto}")
    print("Voce recebeu um desconto de 20%")
if opcao == 2:
    desconto = compra - (compra * 0.10)
    print(f"O valor a vista e: {desconto}")
    print("Voce recebeu um desconto de 10%")
if opcao == 3:
    num = compra / 2
    print(f"O valor total das parcelas sera: {num}")
if opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    num = compra / parcelas
    print(f"O valor total das parcelas sera: {num}")


print("="*40)
