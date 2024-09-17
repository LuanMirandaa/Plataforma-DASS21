Projeto DASS-21 com Interface de Agendamento e Desafios Diários

Descrição
Este projeto é uma aplicação voltada para a promoção da saúde mental, o qual fundamenta-se no teste DASS-21 (Depression, Anxiety, and Stress Scale) short version. Ele inclui uma interface de usuário desenvolvida em Tkinter para facilitar o uso e possui um sistema de desafios diários focados no bem-estar do usuário. O aplicativo também permite o cadastro e login de usuários e psicólogos, com validação de dados.

Funcionalidades

- Cadastro de Usuários e Psicólogos: O sistema valida dados como CPF e CRP, impedindo duplicidade no cadastro.
- Login: O usuário deve realizar login para acessar o teste DASS-21 e outras funcionalidades.
- Teste DASS-21: O teste é aplicado e os resultados são utilizados para categorizar o nível de estresse, ansiedade e depressão.
- Desafios Diários: O usuário recebe lembretes diários de desafios de bem-estar mental, como práticas de mindfulness.
- Sistema de Agendamento: Os usuários podem facilmente escolher o profissional (cadastrado no sistema) de sua preferência, o dia e o horário mais convenientes para a consulta.


Bibliotecas Utilizadas

1.Tkinter
- Tkinter foi escolhido para a criação da interface gráfica por ser uma biblioteca padrão do Python, de fácil uso e integração, o que a torna ideal para o desenvolvimento de interfaces simples e eficientes.
  
2.datetime
- Usada para a a criação dos deasfios diários.

3.os 
 Utilizada para manipular arquivos de forma segura no sistema operacional, facilitando o acesso e gerenciamento dos arquivos de agendamento e cadastro de usuários/psicólogos.

4.re
- A biblioteca re (expressões regulares) foi usada para validação de dados, como o formato de CPF e CRP, garantindo que os dados sejam inseridos corretamente.

Como Executar o Projeto

Pré-requisitos
- Python instalado

Salve o código Python em um arquivo com extensão .py (por exemplo, dass21.py).
Abra um terminal, navegue até o diretório onde salvou o arquivo e execute o comando python dass21.py.
