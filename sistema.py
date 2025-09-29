from cliente import Cliente

class Habitacao:
    def __init__(self, id_habitacao, endereco, tipo, sustentabilidade, valor):
        self.id_habitacao = id_habitacao
        self.endereco = endereco
        self.tipo = tipo
        self.sustentabilidade = sustentabilidade
        self.valor = valor

    def resumo(self):
        return f'ID: {self.id_habitacao} | {self.tipo} | Sustentabilidade: {self.sustentabilidade} | Valor: R${self.valor:.2f} | Endereço: {self.endereco}'


habitacoes = [
    Habitacao(1, 'Rua das Palmeiras, 101', 'Casa Compacta', 'Básica', 120000),
    Habitacao(2, 'Rua das Palmeiras, 101', 'Casa Verde', 'Avançada', 180000),
    Habitacao(3, 'Av. Sustentável, 202', 'Casa Solar', 'Básica', 130000),
    Habitacao(4, 'Av. Sustentável, 202', 'Casa EcoLuxo', 'Avançada', 200000),
    Habitacao(5, 'Rua do Sol, 303', 'Casa Modular', 'Básica', 125000),
    Habitacao(6, 'Rua do Sol, 303', 'Casa Premium', 'Avançada', 210000),
    Habitacao(7, 'Travessa Verde, 404', 'Casa Reflorestada', 'Básica', 140000),
    Habitacao(8, 'Travessa Verde, 404', 'Casa BioLuxo', 'Avançada', 230000),
    Habitacao(9, 'Alameda Sustentável, 505', 'Casa Térmica', 'Básica', 135000),
    Habitacao(10, 'Alameda Sustentável, 505', 'Casa SolarLux', 'Avançada', 220000)
]

def cadastrar_cliente(nome, valor):
    return Cliente(nome, valor)

def filtrar_por_orcamento(valor):
    return [h for h in habitacoes if h.valor <= valor]