def processar_pedido_online(valor, cupom):
  if cupom == "DESC10":
    desconto = valor * 0.90
  elif cupom == "DESC20":
    desconto = valor * 0.80
  else:
    desconto = 0
  return valor - desconto