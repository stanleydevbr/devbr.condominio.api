# Escopo do Projeto de Software para Gestão de Condomínio

O objetivo deste projeto é desenvolver um software robusto e intuitivo para a gestão eficiente de um ou mais condomínios. O software será capaz de lidar com várias tarefas administrativas, financeiras e de comunicação, tornando a gestão do condomínio mais fácil e eficiente.

## Entidades Principais

O software irá gerenciar as seguintes entidades:

- **Condomínio**: Informações sobre o condomínio, incluindo localização, número de unidades, áreas comuns, etc.
- **Unidades**: Informações sobre cada unidade do condomínio, incluindo o proprietário, ocupantes, etc.
- **Condômino**: Informações sobre cada condômino, incluindo contato, unidade ocupada, status de pagamento das taxas do condomínio, etc.

## Funcionalidades Principais

O software irá fornecer as seguintes funcionalidades:

- Gestão de informações do condomínio
- Gestão de unidades e condôminos
- Gestão financeira, incluindo cobrança de taxas de condomínio, acompanhamento de pagamentos, etc.
- Comunicação entre os condôminos e a administração do condomínio
- Reserva de áreas comuns
- Registro e acompanhamento de ocorrências e solicitações dos condôminos

## Arquitetura do Projeto

### Front-End
O front-end do software será desenvolvido em Python, utilizando a biblioteca Flask para a criação da interface do usuário.

### Back-End
O back-end será desenvolvido considerando uma arquitetura em camadas, aplicando os conceitos de Arquitetura Limpa. Isso permitirá uma separação clara entre a lógica de negócios e a interface do usuário, facilitando a manutenção e a expansão futura do software.

A arquitetura será composta pelas seguintes camadas:

- devbr.condominio.sln
  - src
    - Api
      - Controllers  
    - Domain
      - Entities
      - Enums
      - Interfaces
      - ValueObjects
    - Application
      - Interfaces
      - Services
      - DTOs
      - Mappers
    - Infrastructure
      - Data
        - Context
        - Migrations
        - Repositories
      - IoC
  - test
    - Domain.UnitTests
    - Application.UnitTests
    - Infrastructure.IntegrationTests