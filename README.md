# 💵💱💶 Conversor de Moeda

> Um programa que faz a conversão de valores de moedas através de uma API chamada AwesomeAPI por meio da biblioteca requests.

## 🚀 Tecnologias Utilizadas
- O projeto foi escrito em **Python** e utiliza as seguintes bibliotecas:
    
  - **customtkinter**: Biblioteca para criar a interface do projeto, utilizei ela ao invés do tkinter porque ela fornece uma UI mais bonita.
    
  - **requests**: Utiliza para pegar o conteúdo da URL da AwesomeAPI e transformar os dados em valores.
 
  - **re**: Utilizei para formatar os dados de uma lista que tinha caracteres que eu não precisava.
  
## 📦 Instalação e Uso

### Passos para rodar o projeto

1. Clone este repositório:
   ```sh
   git clone https://github.com/andre-fe-santana/ConversorDeMoedas
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd ConversorDeMoedas
   ```  
3. Instale as bibliotecas usadas no projeto
    ```sh
    pip install customtkinter
    ```
    ```sh
    pip install requests
    ```
    
3. Rode o programa através do seu editor de código
   

## 🛠 Funcionalidades

- ✅ Faz a conversão de valores sem necessidade de botões por conta do método dentro de StringVar()
- ✅ Mostra uma lista de moedas disponíveis para fazer a conversão através de web scraping (puxar dados dentro do HTML de um site) para mostrar dentro da interface
- ✅ Mostra o nome das moedas abaixo do valor de conversão para o usuário saber qual moeda ele está convertendo
- 🚧 Planejo adicionar outras conforme o projeto for evoluindo

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto.
2. Crie uma branch com sua feature: `git checkout -b minha-feature`
3. Commit suas alterações: `git commit -m 'Adicionando minha feature'`
4. Faça um push da branch: `git push origin minha-feature`
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

