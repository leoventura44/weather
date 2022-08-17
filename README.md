# weather

Neste projeto iremos obter dados de APIs para criarmos um programa que irá retornar a previsão do tempo de acordo com o input do usuário.

Como foi codificado:
- A primeira coisa feita foi importar o módulo "request" que permite enviar solicitações HTTP usando o Python;
- Em seguida o modulo "pprint" para que os dados do nosso programa fique mais fácil de se ler, pois o formato "json" é um pouco complexo de se visualizar;
- Agora coloquei a chave da API necessária para puxar os dados do clima. Nesse projeto usei a https://lnkd.in/d4pCj_b6 e nele foi gerado uma KEY;
- Em seguida o input "cidade" solicitando que o usuário digite o nome da cidade em que ele deseja saber as informações;
- A variável base_url foi criada para que o Python faça as ligações de todas essas informações e gere um resultado;
- Em seguida a função request para o Python puxar essa solicitação HTTP;
- E por ultimo o comando pprint() para gerar o resultado. Neste exemplo eu quis que o programa mostrasse os dados da cidade de São Paulo.
