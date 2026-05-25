"""""Gerenciador de pedidos refatorado."""

# Constantes substituindo magic numbers
DESCONTO_VIP = 0.85
DESCONTO_PREMIUM = 0.90
DESCONTO_DESC10 = 0.90
DESCONTO_DESC20 = 0.80
JUROS_CARTAO = 1.05
LIMITE_FRETE_GRATIS = 200

FRETE_POR_REGIAO = {
    "SP": 15,
    "RJ": 20,
    "MG": 18,
}
FRETE_PADRAO = 30


def calcular_subtotal(itens):
    """Calcula o subtotal somando preco * quantidade de cada item."""
    total = 0
    for item in itens:
        total += item["preco"] * item["quantidade"]
    return total


class GerenciadorPedidos:
    """Gerencia o processamento de pedidos."""

    def processar_pedido(
        self,
        cliente_nome,
        cliente_email,
        cliente_tipo,
        itens,
        cupom,
        regiao,
        forma_pagamento,
    ):
        """Processa um pedido e retorna o comprovante com totais."""
        total = calcular_subtotal(itens)
        total = self._aplicar_desconto_cliente(total, cliente_tipo)
        total = self._aplicar_cupom(total, cupom)
        frete = self._calcular_frete(total, regiao)
        total_final = self._aplicar_juros(total + frete, forma_pagamento)
        comprovante = self._montar_comprovante(cliente_nome, cliente_email, total_final)
        return {
            "cliente": cliente_nome,
            "subtotal": total,
            "frete": frete,
            "total": round(total_final, 2),
            "comprovante": comprovante,
        }

    def _aplicar_desconto_cliente(self, total, cliente_tipo):
        """Aplica desconto conforme tipo do cliente."""
        if cliente_tipo == "vip":
            return total * DESCONTO_VIP
        if cliente_tipo == "premium":
            return total * DESCONTO_PREMIUM
        return total

    def _aplicar_cupom(self, total, cupom):
        """Aplica desconto de cupom promocional."""
        if cupom == "DESC10":
            return total * DESCONTO_DESC10
        if cupom == "DESC20":
            return total * DESCONTO_DESC20
        return total

    def _calcular_frete(self, total, regiao):
        """Calcula frete por região, grátis acima do limite."""
        if total > LIMITE_FRETE_GRATIS:
            return 0
        return FRETE_POR_REGIAO.get(regiao, FRETE_PADRAO)

    def _aplicar_juros(self, total, forma_pagamento):
        """Aplica juros para pagamento em cartão."""
        if forma_pagamento == "cartao":
            return total * JUROS_CARTAO
        return total

    def _montar_comprovante(self, nome, email, total_final):
        """Monta o texto do comprovante."""
        linha1 = f"Pedido para {nome} ({email})\n"
        linha2 = f"Total: R$ {round(total_final, 2)}"
        return linha1 + linha2

    def calcular_total_relatorio(self, pedidos):
        """Calcula o total geral de uma lista de pedidos."""
        total = 0
        for pedido in pedidos:
            total += calcular_subtotal(pedido["itens"])
        return total
    