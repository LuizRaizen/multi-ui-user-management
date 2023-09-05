# Projeto de Cadastro e Login de Usuários Multiinterface

Este projeto é uma demonstração de um sistema de cadastro e login de usuários que oferece três interfaces gráficas distintas, permitindo que o usuário selecione a interface de sua preferência. Todas as interfaces compartilham o mesmo banco de dados, proporcionando uma experiência unificada para os usuários.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- cadastro_login: Pasta raiz do projeto.
    - ui: Pasta contendo os módulos relacionados à interface do usuário.
        - kv: Pasta com o módulo de interface gráfica utilizando Kivy.
            - app.py: Módulo principal da interface Kivy.
        - qt: Pasta com o módulo de interface gráfica utilizando PySide6.
            - app.py: Módulo principal da interface PySide6.
            - screens.py: Módulo com definições das telas da interface PySide6.
        - tk: Pasta com o módulo de interface gráfica utilizando Tkinter.
            - app.py: Módulo principal da interface Tkinter.
            - login.py: Módulo com a tela de login Tkinter.
            - register.py: Módulo com a tela de cadastro Tkinter.
            - tk_utils.py: Módulo com funções utilitárias para a interface Tkinter.
    - __main__.py: Ponto de entrada principal do programa.
    - .gitignore: Arquivo de configuração do Git para ignorar arquivos específicos.
    - constants.py: Arquivo com constantes utilizadas no projeto.
    - controller.py: Módulo que contém a lógica de controle do programa.
    - database.py: Módulo para interação com o banco de dados SQLite.
    - main.kv: Arquivo de layout Kivy utilizado pela interface Kivy.
    - usuarios.db: Arquivo do banco de dados SQLite contendo os dados dos usuários.
    - utils.py: Módulo com funções utilitárias genéricas.

## Estrutura e Funcionalidade

O arquivo *__main__.py* começa por importar as diferentes interfaces e criar uma janela para a interface de seleção. Essa interface exibe opções para os frameworks disponíveis: **Kivy**, **PySide6** e **Tkinter**. O usuário pode escolher qual framework deseja usar e clicar no botão correspondente.

Quando o usuário seleciona um framework e clica no botão correspondente, a função associada ao botão é chamada. Essa função é responsável por iniciar a interface gráfica específica do framework escolhido.

## Exibindo as Interfaces

As interfaces gráficas de cada framework estão organizadas em subdiretórios dentro do diretório ui. Cada subdiretório contém os arquivos necessários para a interface específica do framework, incluindo telas de cadastro, login e utilitários.

Ao selecionar um framework, a função correspondente exibe a interface associada. Por exemplo, se o usuário escolher o framework **Kivy**, a interface **Kivy** será exibida com suas telas de cadastro e login. Da mesma forma, as interfaces para os frameworks **PySide6** e **Tkinter** também serão exibidas quando selecionadas.

## Flexibilidade e Escolha do Usuário

A estrutura do arquivo *__main__.py* e a interface de seleção oferecem aos usuários a flexibilidade de escolher qual framework eles preferem usar. Isso é particularmente útil, pois diferentes desenvolvedores podem ter preferências pessoais ou requisitos específicos para escolher um framework em relação aos outros.

O arquivo *__main__.py* é um elemento essencial do projeto, permitindo a escolha do framework e orquestrando a exibição das interfaces gráficas. Ele oferece uma maneira intuitiva para que os usuários selecionem e utilizem a interface gráfica que melhor atenda às suas necessidades.

## Interfaces Gráficas

O projeto oferece três interfaces gráficas diferentes para os usuários escolherem:

1. **Kivy Interface (ui/kv/app.py):** Utiliza o framework **Kivy** para criar uma interface gráfica moderna e interativa. As telas são definidas no arquivo *main.kv*.

2. **PySide6 Interface (ui/qt/app.py):** Utiliza o framework **PySide6** para criar uma interface gráfica baseada em widgets. As telas são definidas no módulo *screens.py*.

3. **Tkinter Interface (ui/tk/app.py):** Utiliza o framework **Tkinter** para criar uma interface gráfica clássica. As telas de login e cadastro são definidas nos módulos *login.py* e *register.py*.

### Kivy (KV)

A interface **Kivy** é construída utilizando a biblioteca **Kivy**, que é uma estrutura de desenvolvimento de aplicativos **Python** de código aberto para criar interfaces de usuário multitouch. Para executar a interface **Kivy**, navegue até a pasta *ui/kv* e execute o seguinte comando:

'python app.py'

A interface **Kivy** oferece uma experiência moderna e intuitiva, com controles de toque e suporte a gestos. A tela inicial apresenta opções claras para fazer login ou se cadastrar. Os campos de entrada são facilmente acessíveis e o sistema de lembrete de usuário é integrado para maior comodidade. No entanto, vale ressaltar que está opção se encontra desabilitada no momento.

### PySide6 (QT)

A interface **PySide6** é implementada utilizando a biblioteca **PySide6**, que é uma interface de usuário gráfica em **Python** baseada na biblioteca **Qt**. Para executar a interface **PySide6**, navegue até a pasta *ui/qt* e execute o seguinte comando:

'python app.py'

A interface **PySide6** oferece uma aparência moderna e flexível, seguindo as diretrizes de design do **Qt**. Ela apresenta uma tela de login e uma tela de cadastro claramente separadas. Os campos de entrada são organizados de maneira elegante e a interface responde bem a diferentes tamanhos de tela.

### Tkinter (TK)

A interface **Tkinter** é construída utilizando a biblioteca **Tkinter** padrão do **Python**, que oferece uma maneira simples de criar interfaces gráficas. Para executar a interface **Tkinter**, navegue até a pasta *ui/tk* e execute o seguinte comando:

'python app.py'

A interface **Tkinter** apresenta uma abordagem tradicional de interface gráfica com campos de entrada e botões em um layout organizado. A tela de login e a tela de cadastro são facilmente acessíveis, e a interface se integra bem com o ambiente desktop padrão.

Os usuários têm a liberdade de escolher a interface gráfica que melhor se adapte às suas preferências e necessidades. Cada interface oferece uma experiência de usuário única, enquanto todas estão conectadas ao mesmo banco de dados para manter a consistência dos dados.
	
## Composição e estrutura das Interfaces Gráficas

O projeto de *Cadastro e Login de Usuários Multiinterface* apresenta três interfaces gráficas implementadas usando diferentes frameworks: **Kivy**, **PySide6** e **Tkinter**. Cada interface oferece uma experiência de usuário única, mas todas têm acesso ao mesmo banco de dados compartilhado.

### Kivy (KV)

O módulo *app.py* na pasta *ui/kv* implementa a interface gráfica **Kivy**. O Kivy é um framework de interface de usuário de código aberto e multiplataforma, adequado para a criação de aplicativos móveis e de desktop com uma interface atraente e responsiva. A interface **Kivy** possui as seguintes funcionalidades:

- **Tela de Cadastro:**
  Permite aos usuários inserir um nome de usuário, e-mail e senha para criar uma nova conta no sistema.
- **Tela de Login:**
  Oferece a opção de fazer login com nome de usuário ou e-mail, juntamente com a senha correspondente.
- **Opção "Lembrar de Mim":**
  Os usuários podem optar por lembrar suas credenciais para facilitar o acesso posterior.

O arquivo *main.kv* é um arquivo de estilo Kivy que define a aparência e o comportamento da interface principal do aplicativo. Ele especifica a estrutura de tela, os elementos de interface e as transições entre as telas. O arquivo é usado pela interface **Kivy** para renderizar a interface gráfica de acordo com as especificações do arquivo.

### PySide6 (QT)

A pasta *ui/qt* contém os módulos *app.py* e *screens.py*, que implementam a interface gráfica **PySide6**. O **PySide6** é uma biblioteca que permite a criação de interfaces gráficas usando o toolkit **Qt**. A interface **PySide6** possui funcionalidades semelhantes às do **Kivy**:

- **Tela de Cadastro:**
  Os usuários podem fornecer um nome de usuário, e-mail e senha para se cadastrar no sistema.
- **Tela de Login:**
  Os usuários podem fazer login usando nome de usuário ou e-mail e inserindo a senha correspondente.
- **Opção "Lembrar de Mim":**
  Os usuários podem optar por lembrar suas credenciais para uma experiência de login mais rápida.

### Tkinter (TK)

Na pasta *ui/tk*, os módulos *app.py*, *login.py*, *register.py* e *tk_utils.py* implementam a interface gráfica **Tkinter**. O **Tkinter** é um framework de interface gráfica padrão para o **Python** e é amplamente utilizado para criar aplicativos de desktop. A interface **Tkinter** oferece funcionalidades semelhantes às outras interfaces:

- **Tela de Cadastro:**
  Permite aos usuários inserir um nome de usuário, e-mail e senha para se cadastrar no sistema.
- **Tela de Login:**
  Oferece a opção de fazer login com nome de usuário ou e-mail, juntamente com a senha correspondente.
- **Opção "Lembrar de Mim":**
  Os usuários podem optar por lembrar suas credenciais para facilitar o acesso posterior.

## Funcionalidades Principais
    
- **Cadastro de novos usuários com validação de dados**
- **Login de usuários existentes com autenticação segura**
- **Compartilhamento de banco de dados entre todas as interfaces**
- **Opção de lembrar de usuários para facilitar o login**

## Padrões Arquiteturais e de Projeto

O projeto segue os princípios da arquitetura **MVC (Model-View-Controller)**, separando a lógica de controle, a interface do usuário e o acesso ao banco de dados. Além disso, utiliza padrões de projeto como **Factory**, **Singleton** e **Observer** para garantir uma estrutura organizada e modular.

## Requisitos e Execução

O projeto requer **Python 3.x** e as bibliotecas especificadas no arquivo *requirements.txt*. Para executar o projeto, execute o seguinte comando:

`python -m cadastro_login`

## Dependências do Projeto

Para executar o projeto de *Cadastro e Login de Usuários Multiinterface*, é necessário garantir que você tenha as dependências corretas instaladas. O projeto foi desenvolvido utilizando **Python 3.x** e faz uso de bibliotecas específicas para cada uma das interfaces gráficas. Você pode instalar as dependências usando o arquivo *requirements.txt* fornecido.

## Instalação das Dependências

Abra um terminal e navegue até a pasta raiz do projeto *cadastro_login*, onde o arquivo *requirements.txt* está localizado. Em seguida, execute o seguinte comando para instalar as dependências:

`pip install -r requirements.txt`

Isso instalará as bibliotecas necessárias para cada uma das interfaces gráficas, bem como quaisquer outras dependências do projeto. Certifique-se de ter um ambiente virtual configurado, se desejar isolar as dependências do projeto das demais bibliotecas do Python em seu sistema. Depois de instalar as dependências, você estará pronto para executar o projeto em qualquer uma das interfaces disponíveis.

## Banco de Dados e Controlador

O sistema de *Cadastro e Login de Usuários Multiinterface* utiliza um banco de dados **SQLite** para armazenar informações de usuário, como nome de usuário, email e senha. O arquivo de banco de dados é denominado *usuarios.db* e está localizado no diretório raiz do projeto. O módulo *database.py* contém as funcionalidades relacionadas ao banco de dados, como a criação da tabela de usuários, inserção de novos usuários e realização de consultas.

### Banco de Dados SQLite

O banco de dados **SQLite** é uma escolha adequada para um projeto desse tipo, pois é uma solução leve e incorporada que não requer um servidor separado. Ele permite que os dados sejam armazenados de forma estruturada e eficiente, enquanto oferece suporte à linguagem **SQL** para consultas e manipulações de dados.

### Controlador (controller.py)

O módulo *controller.py* atua como um intermediário entre as interfaces gráficas e o banco de dados. Ele fornece uma camada de abstração para o acesso aos dados do banco de dados e implementa as funcionalidades principais do sistema, como cadastro de novos usuários, autenticação de login e lembrança de usuário.

O controlador gerencia a lógica de negócios do sistema, garantindo que as interfaces gráficas estejam desacopladas das operações de banco de dados subjacentes. Ele é responsável por validar os dados inseridos pelo usuário, verificar a autenticidade das credenciais de login e implementar a funcionalidade de lembrar o usuário para uma experiência mais conveniente.

O controlador oferece os seguintes métodos:

- **cadastrar_usuario(nome_usuario, email, senha):**
  Recebe os dados de um novo usuário e os passa para o banco de dados para inserção.

- **fazer_login(nome_usuario_email, senha):**
  Recebe as credenciais de login, verifica sua validade por meio do banco de dados e retorna *True* se o login for bem-sucedido.

- **verificar_existencia_nome_usuario(nome_usuario):**
  Verifica se um nome de usuário já está em uso no banco de dados.

- **verificar_existencia_email(email):**
  Verifica se um endereço de e-mail já está em uso no banco de dados.

## Executando o Projeto

Navegue até o diretório da interface desejada (kv, qt ou tk) e execute o arquivo *app.py* correspondente. Por exemplo, para executar a interface **Kivy**:

```python

cd ui/kv
python app.py

```

O aplicativo será iniciado com a interface selecionada e você poderá explorar as funcionalidades de cadastro e login de usuários.
Para alternar entre as interfaces, utilize os botões ou opções fornecidos na interface gráfica para selecionar a tela desejada.

### Arquivo Main (main.py)

O arquivo *__main__.py* é o ponto de entrada do projeto e é responsável por iniciar o aplicativo. Ele importa as interfaces gráficas implementadas em cada framework e inicia a interface escolhida pelo usuário. Além disso, ele lida com a seleção e troca de interfaces, permitindo que o usuário escolha entre **Kivy**, **PySide6** e **Tkinter**.

Você ainda pode executar o gerenciador de interfaces. Para isso, vá até o diretório raiz do projeto e execute o seguinte comando:

#### No Windows:
`python __main__.py`

#### Em distribuições Linux/Mac OS:
`python3 __main__.py`

Um programa em linha de comando será aberto, e você poderá selecionar uma das 3 pções de interface gráfica através de um dos comandos disponíveis.

## Padrões Arquiteturais e Padrões de Projeto

O projeto de *Cadastro e Login de Usuários Multiinterface* foi desenvolvido seguindo princípios de design e padrões arquiteturais que visam a modularização, reutilização de código e manutenibilidade. Além disso, padrões de projeto foram aplicados para resolver problemas comuns de design e garantir uma estrutura coesa e flexível.

### Padrão Arquitetural MVC (Model-View-Controller)

O projeto utiliza o padrão arquitetural **MVC** para organizar a separação de preocupações em três componentes principais: **Model (Modelo)**, **View (Visão)** e **Controller (Controlador)**.

- **Model (Modelo):**
Representa a camada de dados e lida com a manipulação e persistência dos dados do sistema. Neste projeto, a classe *BancoDeDados* do módulo *database.py* atua como o modelo, lidando com: a criação da tabela de usuários; a tabela de usuários relembrados para cada interface; persistÇencia dos dados e consultas ao banco de dados.

- **View (Visão):**
Representa a camada de interface gráfica que interage com o usuário. As interfaces **Kivy**, **PySide6** e **Tkinter** implementam a camada de visualização, apresentando formulários de cadastro, login e elementos de interação para o usuário.

- **Controller (Controlador):**
Atua como intermediário entre o modelo e a visão, gerenciando a lógica de negócios e as operações do sistema. O módulo *controller.py* implementa o controlador, garantindo que as interfaces gráficas estejam desacopladas das operações de banco de dados. O controlador do projeto ainda lida com as rotinas de requisição dos dados do Modelo, realizando tarefas como a criação de novos usuários e registrando usuários á serem relembrados para login no sistema.

### Padrões de Projeto Utilizados

Além do padrão arquitetural **MVC**, alguns padrões de projeto foram utilizados para garantir a modularização, reutilização e manutenibilidade do código.

- **Factory Method (Método de Fábrica):**
O padrão Factory Method foi utilizado para criar instâncias de interfaces gráficas sem especificar explicitamente a classe concreta. Isso permite que o código cliente (no arquivo *__main__.py*) crie instâncias das interfaces de acordo com a escolha do usuário, sem depender diretamente das implementações específicas.

- **Singleton:**
O padrão **Singleton** foi aplicado para garantir que apenas uma única instância da classe *BancoDeDados* (modelo) seja criada e utilizada em todo o sistema. Isso evita problemas de concorrência e garante que todos os componentes do sistema acessem os mesmos dados.

- **Strategy (Estratégia):**
O padrão *Strategy* foi utilizado para implementar diferentes estratégias de lembrança de usuário. Cada interface gráfica tem sua própria implementação de lembrança, que é selecionada com base na interface escolhida pelo usuário. Isso permite a adição fácil de novas estratégias de lembrança no futuro.

### Outros Padrões

Além dos padrões mencionados, o código do projeto adere a boas práticas de programação, como encapsulamento, coesão e baixo acoplamento entre os componentes. Esses princípios contribuem para um código mais legível, organizado e facilmente manutenível.

O projeto de *Cadastro e Login de Usuários Multiinterface* demonstra a aplicação eficaz desses padrões arquiteturais e de projeto para criar um sistema robusto e flexível que pode ser facilmente estendido e adaptado no futuro.

## Banco de Dados e Controlador

O projeto utiliza um banco de dados **SQLite** para armazenar informações de usuário. A classe *BancoDeDados* no módulo *database.py* é responsável pela criação da tabela de usuários, inserção de novos registros e consultas ao banco de dados. O controlador, implementado no módulo *controller.py*, gerencia a lógica de negócios e a interação entre as interfaces gráficas e o banco de dados.

O projeto utiliza um banco de dados para armazenar informações dos usuários, como nome de usuário, e-mail e senha. O banco de dados é essencial para garantir a persistência dos dados e permitir que os usuários façam login e se cadastrem com segurança.

### Estrutura do Banco de Dados

O banco de dados possui uma tabela chamada *usuarios*, onde os registros dos usuários são armazenados. 

A estrutura da tabela é a seguinte:

|Coluna			|Tipo		|Descrição
|---------------|-----------|-------------------------------|
|id				|INTEGER	|Chave primária autoincremental |
|nome_usuario	|TEXT		|Nome de usuário				|
|email			|TEXT		|Endereço de e-mail				|
|senha			|TEXT		|Senha criptografada			|

### Operações do Banco de Dados

O módulo *database.py* contém a classe *BancoDeDados*, que encapsula as operações de banco de dados necessárias para o funcionamento do sistema:

- **criar_tabela_usuarios():**
Cria a tabela usuarios se ainda não existir.

- **inserir_usuario(nome_usuario, email, senha):**
  Insere um novo usuário na tabela, fornecendo um nome de usuário, e-mail e senha. A senha é armazenada de forma criptografada.

- **obter_usuario_por_nome(nome_usuario):**
  Retorna um usuário com base no nome de usuário fornecido.

- **obter_usuario_por_email(email):**
  Retorna um usuário com base no endereço de e-mail fornecido.

- **fazer_login(nome_usuario_email, senha):**
  Verifica as credenciais de login (nome de usuário ou e-mail e senha) e retorna True se as credenciais forem válidas.

## Conclusão

O projeto de *Cadastro e Login de Usuários Multiinterface* demonstra a aplicação de padrões arquiteturais e de projeto para criar um sistema flexível e modular. Com interfaces gráficas implementadas em **Kivy**, **PySide6** e **Tkinter**, os usuários podem escolher a interface que melhor se adapte às suas preferências. O uso de um banco de dados compartilhado e um controlador centralizado garante a consistência e a segurança dos dados do usuário. O projeto exemplifica boas práticas de design de software e oferece uma base sólida para expansão futura.

## Considerações do Autor

Iniciei este projeto com o intuito de integrar em meu portfólio um software que englobasse algumas das principais práticas de programação e conhecimentos necessários para a criação de um software do tipo **CRUD (Create, Read, Update, Delete)**.

Por se tratar de uma pequena aplicação de estudo, comecei a escrever o código de maneira despretenciosa, ignorando a convenção de utilizar nomes em inglês para as variáveis e componentes do programa. Apesar de não ser uma boa prática, decidi manter o código assim, pois creio que isso facilitará o aprendizado de iniciantes em programação que sejam falantes do português (como eu). O programa não possui uma finalidade objetiva para usuários comuns, por isso, não me preocupei em desenvolver interfaces com apelo visual.

Sua estrutura modular o torna um bom ponto de partida para ser usado como template em projetos maiores por outros desenvolvedores (eu certamente irei reaproveitá-lo em projetos futuros). Desenvolver um sistema completo de autenticação de usuários pode ser mais complexo do que parece! Inicialmente, a proposta do projeto era ser apenas um sistema de CRUD comum, com uma interface gráfica simples desenvolvida em Tkinter com acesso a um banco de dados. Mas como ainda não tinha nenhum exemplo de programas desenvolvidos com os outros dois frameworks (**PySide6**, **Kivy**), achei que seria interessante e desafiador desenvolver uma aplicação que integrasse três interfaces diferentes á um mesmo banco de dados. No decorrer do desenvolvimento, o projeto acabou se expandindo, quando me dei conta, estava aprendendo sobre criptografia e princípios de segurança indispensáveis para qualquer sistema informatizado.
	
Sinta-se á vontade para clonar este repositório e reaproveitar seu conteúdo. O sistema não está completo, o CheckBox *"Lembrar de mim"* da tela do **Kivy** ainda não foi implementado, se você mantê-lo marcado ao tentar fazer login, verá que uma caixa de diálogo informativa alertará que a funcionalidade está desabilitada. Para tornar o projeto mais relevante e completo, seria interessante a criação de um sistema de envio de e-mails para ativação das contas e uma opção para alterar senhas esquecidas.
	
Se você tiver conhecimentos em alguma das técnologias utilizadas para implementar este sistema e gostaria de contribuir com o projeto, entre em contato comigo pelo meu [e-mail](luizrdererita@gmail.com).
