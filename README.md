# 🌱 Agência de Habitação Sustentável

# Este projeto é um sistema interativo que ajuda clientes a encontrar e adquirir casas sustentáveis de acordo com seu orçamento e preferências de sustentabilidade. 
# Desenvolvido em Python com foco em modularidade, clareza e boas práticas de orientação a objetos.

---

## 📦 Estrutura do Projeto

```
├── cliente.py          # Classe Cliente
├── sistema.py          # Classe Habitacao + funções de sistema
├── main.py             # Interface interativa com o usuário
```

---

## 🧠 Funcionalidades

- Cadastro de cliente com nome e orçamento
- Listagem de casas sustentáveis por nível (Básica ou Avançada)
- Filtragem por tipo de sustentabilidade
- Exibição de detalhes da casa selecionada
- Confirmação de aquisição com mensagem personalizada

---

## 🧾 Requisitos

### Visíveis
- Interface de menu simples e intuitiva
- Escolha de casas por tipo de sustentabilidade
- Visualização de detalhes e confirmação de compra

### Invisíveis
- Organização modular em três arquivos
- Uso de classes e encapsulamento
- Separação entre lógica de negócio e apresentação

---

📘 Diagrama de Classes (Texto)

Classe Cliente
- Atributos:
- nome: string
- valor_disponivel: float

Classe Habitacao
- Atributos:
- id_habitacao: int
- endereco: string
- tipo: string
- sustentabilidade: string
- valor: float
- Métodos:
- resumo(): retorna uma string com os detalhes da habitação

Funções em sistema.py
- cadastrar_cliente(nome, valor): retorna um objeto Cliente
- filtrar_por_orcamento(valor): retorna lista de Habitacao com valor menor ou igual ao informado
---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/agencia-habitacao-sustentavel.git
   cd agencia-habitacao-sustentavel
   ```

2. Execute o programa:
   ```bash
   python main.py
   ```

## 🧑‍💻🧑‍💻 Autores

## Gustavo Lima https://github.com/gustavolima37  |  Marcia Jacó - https://github.com/marciaeujc-pixel
