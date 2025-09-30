from controller import (
    cadastrar_cliente,
    obter_habitacoes_por_categoria,
    detalhes_casa_basica,
    detalhes_casa_mediana,
    detalhes_casa_avancada
)

print('==================================================')
print('Bem-vindo à Agência de Habitação Sustentável 🌱')
nome = input('Digite seu nome: ')
cliente = cadastrar_cliente(nome)
print('==================================================')

while True:
    print('\nEscolha o tipo de casa sustentável:')
    print('1 - Básica')
    print('2 - Mediana')
    print('3 - Avançada')
    print('0 - Sair')

    escolha = input('Opção: ')
    if escolha == '0':
        print('Sistema Encerrado. Volte Sempre!')
        break

    categorias = {'1': 'Básica', '2': 'Mediana', '3': 'Avançada'}
    tipo = categorias.get(escolha)

    if not tipo:
        print('Opção inválida.')
        continue

    casas = obter_habitacoes_por_categoria(tipo)
    print(f'\nCasas sustentáveis ({tipo}):')
    for casa in casas:
        print('\n' + casa.resumo())

    escolha_id = input('\nDigite o ID da casa que deseja adquirir ou "V" para voltar: ')
    if escolha_id.lower() == 'v':
        continue

    selecionada = next((c for c in casas if str(c.id_habitacao) == escolha_id), None)
    if selecionada:
        print('\nDetalhes da casa selecionada:')
        print(selecionada.resumo())

        if selecionada.sustentabilidade == 'Básica':
            extras = detalhes_casa_basica(selecionada.tipo)
        elif selecionada.sustentabilidade == 'Mediana':
            extras = detalhes_casa_mediana(selecionada.tipo)
        elif selecionada.sustentabilidade == 'Avançada':
            extras = detalhes_casa_avancada(selecionada.tipo)
        else:
            extras = []

        if extras:
            print('\nCaracterísticas adicionais:')
            for item in extras:
                print(f'- {item}')

        confirmar = input('\nDeseja adquirir esta casa? (S/N): ')
        if confirmar.lower() == 's':
            print(f'\nParabéns, {cliente.nome}! Você escolheu a {selecionada.tipo} localizada em {selecionada.endereco}.')
            break
        else:
            print('Voltando ao menu...')
    else:
        print('ID inválido. Retornando ao menu.')