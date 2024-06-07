from .models import Pessoa, SplitRule

def calcular_split(deposito, conta_filha):
    conta_mae = conta_filha.conta_mae
    taxa_deposito = conta_mae.taxa_deposito

    splits = []
    valor_restante = taxa_deposito

    # Adiciona os splits fixos
    for pessoa in Pessoa.objects.filter(porcentagem_fixa__isnull=False):
        valor_split = (pessoa.porcentagem_fixa / 100) * deposito
        splits.append((pessoa.nome, valor_split))
        valor_restante -= pessoa.porcentagem_fixa

    # Adiciona os splits especiais com requisito de CPF
    for split_rule in SplitRule.objects.filter(conta_mae=conta_mae, requisito_cpf=True):
        pessoa = split_rule.pessoa
        if conta_filha.cpf in pessoa.cpf_validos.split(','):
            valor_split = (split_rule.porcentagem / 100) * deposito
            splits.append((pessoa.nome, valor_split))
            valor_restante -= split_rule.porcentagem

    # Adiciona o split dinâmico para Infinity
    valor_split_infinity = (valor_restante / 100) * deposito
    splits.append(("Infinity", valor_split_infinity))

    return splits
