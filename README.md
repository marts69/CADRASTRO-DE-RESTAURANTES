# Projeto Python

## Descrição
Este projeto foi desenvolvido para fins de estudo e prática em Python. Ele contém scripts e exemplos para aprendizado da linguagem.

## Requisitos
- Python 3.x instalado

## Instalação
1. Clone este repositório ou copie os arquivos para sua máquina.
2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Instale as dependências, se houver:
   ```bash
   pip install -r requirements.txt
   ```

## Como usar
Execute o script principal:
```bash
python app.py
```

## Licença
Este projeto está sob a licença MIT.


## Como o código funciona
O projeto simula um sistema simples de restaurante, com cadastro de restaurantes, pratos e bebidas. Veja como cada parte funciona:

### Estrutura principal
- O arquivo `app.py` é o ponto de entrada. Ele cria um restaurante, adiciona um prato e uma bebida ao cardápio e exibe o cardápio.

### Classes principais
- **Restaurante** (`modelo/restaurante.py`):
   - Gerencia restaurantes, avaliações e o cardápio.
   - Permite adicionar itens ao cardápio e exibir os itens cadastrados.
   - Calcula a média das avaliações recebidas.

- **Prato** (`modelo/Cardapio/Prato.py`):
   - Representa um prato do cardápio, com nome, preço e descrição.
   - Possui método para aplicar desconto ao preço.

- **Bebida** (`modelo/Cardapio/Bebida.py`):
   - Representa uma bebida do cardápio, com nome, preço e tamanho.
   - Possui método para aplicar desconto ao preço.

### Fluxo do código
1. Cria um restaurante.
2. Cria uma bebida e um prato, aplicando descontos.
3. Adiciona esses itens ao cardápio do restaurante.
4. Exibe o cardápio com nome, preço e detalhes de cada item.

### Observações
- O projeto pode ser expandido para incluir mais funcionalidades, como avaliações de clientes, ativação/desativação de restaurantes e mais tipos de itens no cardápio.
