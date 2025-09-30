from model import Cliente, Habitacao

def cadastrar_cliente(nome):
    return Cliente(nome)

habitacoes = [
    Habitacao(1, 'Rua das Palmeiras, 101', 'Casa Compacta', 'Básica', 120000),
    Habitacao(2, 'Av. Sustentável, 202', 'Casa Solar', 'Básica', 130000),
    Habitacao(3, 'Travessa Verde, 404', 'Casa Reflorestada', 'Básica', 140000),
    Habitacao(4, 'Rua do Sol, 303', 'Casa Modular', 'Mediana', 160000),
    Habitacao(5, 'Alameda Sustentável, 505', 'Casa Térmica', 'Mediana', 170000),
    Habitacao(6, 'Rua das Palmeiras, 101', 'Casa Verde', 'Mediana', 175000),
    Habitacao(7, 'Av. Sustentável, 202', 'Casa EcoLuxo', 'Avançada', 200000),
    Habitacao(8, 'Rua do Sol, 303', 'Casa Premium', 'Avançada', 210000),
    Habitacao(9, 'Travessa Verde, 404', 'Casa BioLuxo', 'Avançada', 230000),
]

def obter_habitacoes_por_categoria(categoria):
    return [h for h in habitacoes if h.sustentabilidade.lower() == categoria.lower()][:3]

def detalhes_casa_basica(tipo):
    detalhes = {
        'Casa Compacta': [
            'Design otimizado para pequenos terrenos',
            'Isolamento térmico eficiente',
            'Sistema de captação de água da chuva'
        ],
        'Casa Solar': [
            'Painéis solares integrados ao telhado',
            'Iluminação natural abundante',
            'Materiais recicláveis na construção'
        ],
        'Casa Reflorestada': [
            'Jardim vertical e área verde integrada',
            'Uso de madeira certificada',
            'Sistema de compostagem doméstica'
        ]
    }
    return detalhes.get(tipo, [])

def detalhes_casa_mediana(tipo):
    detalhes = {
        'Casa Modular': [
            'Estrutura flexível e expansível',
            'Sistema de ventilação cruzada',
            'Materiais pré-fabricados sustentáveis'
        ],
        'Casa Térmica': [
            'Paredes com isolamento térmico avançado',
            'Vidros duplos para controle de temperatura',
            'Sistema de aquecimento solar de água'
        ],
        'Casa Verde': [
            'Telhado verde com vegetação nativa',
            'Reuso de água cinza',
            'Sistema de irrigação automatizado'
        ]
    }
    return detalhes.get(tipo, [])

def detalhes_casa_avancada(tipo):
    detalhes = {
        'Casa EcoLuxo': [
            'Automação residencial completa',
            'Materiais de alto desempenho ecológico',
            'Certificação LEED de construção sustentável'
        ],
        'Casa Premium': [
            'Sistema de energia solar com bateria',
            'Acabamentos de luxo com baixo impacto ambiental',
            'Controle inteligente de iluminação e climatização'
        ],
        'Casa BioLuxo': [
            'Bioconstrução com materiais orgânicos',
            'Sistema de purificação de ar interno',
            'Design biofílico integrado à natureza'
        ]
    }
    return detalhes.get(tipo, [])