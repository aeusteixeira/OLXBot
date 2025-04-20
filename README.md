# 🤖 OLX Bot

Bot automatizado para busca e coleta de dados de anúncios na OLX Brasil.

```
░█████╗░██╗░░░░░██╗░░██╗  ██████╗░░█████╗░████████╗
██╔══██╗██║░░░░░╚██╗██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║██║░░░░░░╚███╔╝░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║██║░░░░░░██╔██╗░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝███████╗██╔╝╚██╗  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
```

## 📋 Descrição

Este bot foi desenvolvido para automatizar a busca de anúncios na OLX Brasil. Ele permite que você:

- Realize buscas por termos específicos
- Filtre por localização
- Colete dados dos anúncios automaticamente
- Salve os resultados em formato JSON

## 🚀 Funcionalidades

- Busca automatizada por termo
- Filtro por localização
- Ordenação por mais recentes
- Coleta de dados dos anúncios:
  - Título
  - Preço
  - Localização
  - Data de publicação
  - Link do anúncio
- Exportação dos dados em JSON

## 💻 Requisitos

- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/aeusteixeira/OLXBot.git
```

2. Instale as dependências:
```bash
pip install selenium
```

3. Certifique-se de ter o Chrome e ChromeDriver instalados

## 📦 Estrutura do Projeto

```
sabor-express/
├── app/
│   └── OLXBot.py      # Classe principal do bot
├── main.py            # Script principal
└── README.md          # Documentação
```

## 🎯 Como Usar

1. Execute o script principal:
```bash
python main.py
```

2. Digite o termo que deseja buscar quando solicitado

3. Digite a localização desejada

4. O bot irá:
   - Acessar a OLX
   - Realizar a busca
   - Coletar os dados
   - Salvar em um arquivo JSON

## 📄 Formato do JSON

Os dados são salvos no formato:
```json
{
  "data_hora_pesquisa": "YYYY-MM-DD HH:MM:SS",
  "anuncios": [
    {
      "titulo": "Título do anúncio",
      "preco": "R$ XX.XXX",
      "localizacao": "Cidade, Bairro",
      "data_publicacao": "Data da publicação",
      "link": "URL do anúncio"
    }
  ]
}
```

## 👨‍💻 Autor

Matheus Teixeira

## 📅 Data

19/04/2025

## ⚠️ Aviso Legal

Este bot foi desenvolvido apenas para fins educacionais. Certifique-se de seguir os Termos de Serviço da OLX ao utilizá-lo. 
