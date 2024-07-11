# Projeto_MISP

### NOTA IMPORTANTE
Para seguir o tutorial é recomendado o uso do Python3.11

## Instalação do MISP


O processo de instalação que será apresentado neste tutorial é baseado nas instruções disponíveis na página da plataforma do MISP (https://misp-project.org/). A instância do projeto HackInSDN usa a solução Docker containers, mas especificamente, imagens docker mantidas por Stefano Ortolani da VMware. As quais são regularmente enviadas para o registro do pacote MISP GitHub .


Acesse a documentação do MISP para ter acesso às opções de instalação disponibilizadas pela plataforma. Link: https://misp-project.org/download/


As instruções para a instalação usando as imagens mantidas por Stefano Ortolani da VMware podem ser acessadas em: https://github.com/misp/misp-docker 


Os requisitos mínimos para implementar uma instância MISP seguindo este tutorial são:

1 processador;

4GB de RAM;

80GB de disco;

Versão mais recente do Docker Desktop e/ou Docker Engine.


Em seguida você precisará executar os seguintes passos listados abaixo:

Passo 1: Clonar o repositório do misp-docker, para isso execute o seguinte comando no seu terminal:


````ruby
$ git clone https://github.com/MISP/misp-docker/ && cd docker-misp
````


Passo 2: Copiar o arquivo de ambiente e remover seu prefixo temporário.
````ruby
$ cp template.env .env			
````

Passo 3: Dentro do diretório criado, verifique se o arquivo docker-compose.yml foi baixado corretamente. Em caso positivo, você precisará extrair as imagens pré-construídas ou construir novas imagens, a segunda opção é mais recomendável. 


Para extrair as imagens pré-construídas:
````ruby
$ docker compose pull
````


Para construir novas imagens:
````ruby
$ docker compose build
````

Obs1: o processo de geração das imagens pode demorar um pouco, aguarde o processo ser finalizado para seguir para o próximo passo. 

Obs2: Em caso de erros, veja a seção Troubleshooting.


Passo 4: Agora será necessário carregar os containers, os quais são responsáveis habilitar os componentes necessários (misp, misp-modules, redis, database, and mail containers) para a execução do MISP.

````ruby
$ docker compose up
````

Para acessar a interface Web do MISP acesse https://localhost usando as credenciais:

````
E-mail: admin@admin.test
````
````
Senha: admin
````


## Configuração do MISP


Após a instalação do MISP será necessário efetuar algumas configurações como: troca de senha, criação de organização e novos usuários, etc.


Para alterar a senha do usuário padrão clique em Administration >> List Users >> Set password. Após inserir a nova senha, confirme a senha atual (admin) e submeter as alterações.


Para criar uma nova organização clique em Administration >> Add Organisations. E preencha os campos com o nome, UUID, descrição, nacionalidade, setor e outras informações pertinentes sobre a sua organização.


Para criar um novo usuário clique em Administration >> Add User. E preencha os campos com nome, email, senha, role e organização e outras informações pertinentes ao novo usuário da sua organização.


Para ter acesso aos eventos compartilhados por outras organizações será necessário habilitar os feeds. No exemplo abaixo, vamos apresentar o passo a passo de como habilitar os feeds públicos disponibilizados no MISP.

Passo 1: Verificar se os Workers estão ativados;

Passo 2: Habilitar os feeds públicos.

Passo 3: Fazer o download dos eventos.

## Acessando a API do MISP
Neste projeto, para acessar a plataforma MISP por meio de sua API REST usamos a biblioteca PyMISP. Para mais informações sobre a biblioteca, acesse: https://github.com/MISP/PyMISP.

A instalação do PyMISP pode ser feita executando esse comando:
````ruby
pip3 install pymisp
````

## Referências
- Documentação MISP
   - https://www.circl.lu/doc/misp/

- Repositório MISP
  - https://github.com/misp/misp-docker

-  Repositório PyMISP
    - https://github.com/MISP/PyMISP

- Outras Referências
  - https://github.com/brunoodon/misp/tree/main/automation

