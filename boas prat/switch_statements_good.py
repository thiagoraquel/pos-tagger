def valor_com_desconto(valor, desconto):
  return valor * (1 - desconto)

def valor_desconto_cupom(cupom):
  cupom = cupom.upper().strip()  # Trata entrada para evitar erros com espaços ou minúsculas

  if cupom == "NONE":
    return 0
  elif cupom.startswith("DESC"):
    try:
      percentual = int(cupom[4:]) / 100
      return percentual
    except ValueError:
      return 0
  return 0