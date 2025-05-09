def calcular_total(itens, aplicar_desconto):
    total = sum(itens)
    desconto = 0

    # Código morto: nunca usado
    if aplicar_desconto:
        desconto = total * 0.1
    
    valor_frete = 20  # valor fixo
    # desconto não é usado!
    return total + valor_frete
