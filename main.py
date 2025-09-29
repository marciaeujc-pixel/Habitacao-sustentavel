from sistema import habitacoes, cadastrar_cliente

print('==================================================')
print('Bem-vindo à Agência de Habitação Sustentável 🌱')
nome = input('Digite seu nome: ')
cliente = cadastrar_cliente(nome, 0)  # valor não é mais usado
print('==================================================')

while True:
    print('\nEscolha o tipo de sustentabilidade desejada:')
    print('1 - Básica')
    print('2 - Avançada')
    print('0 - Sair')

    escolha = input('Opção: ')
    if escolha == '0':
        print('Até logo!')
        break

    tipo_sustentabilidade = 'Básica' if escolha == '1' else 'Avançada' if escolha == '2' else None
    if not tipo_sustentabilidade:
        print('Opção inválida.')
        continue

    casas_filtradas = [h for h in habitacoes if h.sustentabilidade == tipo_sustentabilidade]
    print(f'\nCasas com sustentabilidade {tipo_sustentabilidade}:')
    for casa in casas_filtradas:
        print(f'{casa.id_habitacao} - {casa.tipo}')

    escolha_id = input('\nDigite o ID da casa que deseja ver ou "V" para voltar: ')
    if escolha_id.lower() == 'v':
        continue

    selecionada = next((c for c in casas_filtradas if str(c.id_habitacao) == escolha_id), None)
    if selecionada:
        print('\nDetalhes da casa selecionada:')
        print(selecionada.resumo())
        confirmar = input('\nDeseja adquirir esta casa? (S/N): ')
        if confirmar.lower() == 's':
            print(f'\nParabéns, {cliente.nome}! Você escolheu a {selecionada.tipo} localizada em {selecionada.endereco}.')
            break
        else:
            print('Voltando ao menu...')
    else:
        print('ID inválido. Retornando ao menu.')