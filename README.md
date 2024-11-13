## &nbsp; Microservice-vs-Monolith

Vamos imaginar um sistema simples de gerenciamento de estoque. Em um modelo monolítico, todas as funcionalidades estariam em um único programa.
Instruções do Programa:
- Adicionar um novo produto ao estoque (nome, quantidade, preço).
- Listar todos os produtos em estoque.
- Buscar um produto pelo nome.
- Atualizar a quantidade de um produto em estoque.
- Remover um produto do estoque.


Divida as funcionalidades em microsserviços separados. Cada um terá sua própria responsabilidade.
Instrução:
- Crie microsserviços para:
- Gerenciar produtos (adicionar, listar, buscar).
- Gerenciar estoque (atualizar quantidade, remover).

Desafio: 
Utilize uma biblioteca como Flask ou FastAPI ou Django ou outra que preferir para criar as APIs de cada microsserviço.
Pense em como os microsserviços se comunicariam (por exemplo, através de chamadas HTTP).



---

## Arquiteturas: Monolítica vs. Microsserviços

## &nbsp;Monolitico

Na arquitetura monolítica, todo o sistema é construído como um único bloco de código, onde todas as funcionalidades (como lógica de negócios, interface de usuário e acesso ao banco de dados) estão interligadas em uma única aplicação. Esse modelo é comum em sistemas mais antigos ou pequenos, pois é mais fácil de configurar, testar e implantar inicialmente. No entanto, à medida que o sistema cresce, o monólito pode se tornar difícil de manter, testar e escalar, já que qualquer modificação exige o redimensionamento e a implantação de toda a aplicação.

**Vantagens da Arquitetura Monolítica:**
- Simplicidade inicial, com menos infraestrutura para gerenciar.
- Facilidade de desenvolvimento e teste no início do projeto.
- Implantação unificada, o que simplifica a entrega de novas versões.

**Desvantagens da Arquitetura Monolítica:**
- Escalabilidade limitada, pois toda a aplicação precisa ser escalada mesmo se apenas uma parte dela estiver com alta demanda.
- Manutenção complexa à medida que o código cresce.
- Dependência elevada entre as funcionalidades, aumentando o risco de impacto em várias áreas ao realizar mudanças.

## &nbsp;Microserviços

A arquitetura de microsserviços divide a aplicação em serviços independentes, onde cada serviço é responsável por uma funcionalidade específica e pode ser desenvolvido, testado e implantado de forma autônoma. Cada microsserviço se comunica com os demais, geralmente via APIs, o que permite a construção de sistemas mais flexíveis e escaláveis. Esse modelo é ideal para projetos complexos e de grande escala, pois facilita o gerenciamento de serviços independentes e a escalabilidade específica de funcionalidades.

**Vantagens da Arquitetura de Microsserviços:**
- Independência e autonomia de cada serviço, facilitando o desenvolvimento, a escalabilidade e o gerenciamento.
- Maior flexibilidade na escolha de tecnologias, já que cada microsserviço pode ter sua própria stack tecnológica.
- Escalabilidade focada, pois é possível escalar apenas os serviços que necessitam.

**Desvantagens da Arquitetura de Microsserviços:**
- Complexidade adicional na comunicação entre serviços e no gerenciamento da infraestrutura.
- Necessidade de ferramentas para monitoramento, versionamento e controle de APIs.
- Dependência de integração contínua e entrega contínua (CI/CD) para facilitar o desenvolvimento.

---

## &nbsp;Projeto

Este projeto é um sistema de gerenciamento de estoque dividido em microsserviços, desenvolvido com **FastAPI**. A estrutura modularizada permite maior escalabilidade, flexibilidade e facilidade de manutenção, diferenciando-se do modelo monolítico tradicional. Cada microsserviço é responsável por uma parte específica do sistema, o que melhora a organização e facilita o desenvolvimento e a implantação.

### Estrutura do Projeto

1. **Microsserviço de Produtos (`produto_service`)**
   - Responsável por gerenciar informações de produtos, incluindo:
     - Adicionar novos produtos (com nome, quantidade inicial e preço).
     - Listar todos os produtos em estoque.
     - Buscar produtos específicos pelo nome.
   - Funciona de maneira independente, mas pode ser consultado pelo microsserviço de estoque para verificar a existência dos produtos.

2. **Microsserviço de Estoque (`estoque_service`)**
   - Gerencia o controle de quantidade dos produtos no estoque, incluindo:
     - Atualizar a quantidade de produtos no estoque.
     - Remover produtos do estoque quando necessário.
   - Consulta o microsserviço de produtos via chamadas HTTP para verificar a existência de um produto antes de realizar operações de atualização ou remoção.

### Comunicação entre Microsserviços

Os dois microsserviços se comunicam por meio de **chamadas HTTP**. Por exemplo, o microsserviço de estoque realiza uma requisição ao microsserviço de produtos para verificar a existência de um produto antes de atualizar sua quantidade ou removê-lo do estoque. Esse modelo de comunicação garante que cada serviço se mantenha independente e focado em suas responsabilidades.

### Tecnologias Utilizadas

- **FastAPI**: Para a criação das APIs de cada microsserviço.
- **Uvicorn**: Servidor ASGI para execução das APIs do FastAPI.
- **Pydantic**: Para validação e serialização de dados de entrada.

### Benefícios da Arquitetura de Microsserviços no Projeto

- **Escalabilidade**: Cada serviço pode ser escalado individualmente conforme a demanda.
- **Facilidade de Manutenção**: Permite atualizações e manutenção focadas em cada funcionalidade específica.
- **Flexibilidade e Evolução**: Novos serviços podem ser adicionados sem impactar os serviços existentes, facilitando a evolução do sistema.


![planttext](https://github.com/user-attachments/assets/55cb7cb5-a21a-44a8-84f4-b9326457aec7)
