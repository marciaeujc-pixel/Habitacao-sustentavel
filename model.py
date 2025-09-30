class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Habitacao:
    def __init__(self, id_habitacao, endereco, tipo, sustentabilidade, valor):
        self.id_habitacao = id_habitacao
        self.endereco = endereco
        self.tipo = tipo
        self.sustentabilidade = sustentabilidade
        self.valor = valor

    def resumo(self):
        return (
            f"🏡 ID: {self.id_habitacao}\n"
            f"Tipo: {self.tipo}\n"
            f"Sustentabilidade: {self.sustentabilidade}\n"
            f"Valor: R${self.valor:.2f}\n"
            f"Endereço: {self.endereco}"
        )