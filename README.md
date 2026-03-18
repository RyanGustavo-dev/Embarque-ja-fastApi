# Sistema de Gerenciamento de Excursões - EmbarqueJá

## Descrição do Projeto

Sistema desenvolvido para automatizar o gerenciamento de excursões, substituindo o controle manual em pranchetas por uma solução digital completa. O sistema permite o cadastro de clientes, controle de assentos, gerenciamento de ônibus e roteiros, proporcionando maior eficiência e organização para agências de turismo.

## Problema e Solução

**Problema:** Agências de excursão que ainda utilizam controle manual em pranchetas enfrentam dificuldades na organização, reserva de assentos e podem ter erros operacionais.

**Solução:** Sistema web intuitivo que digitaliza todo o processo de gestão de excursões, desde o cadastro de clientes até o controle de assentos em tempo real.

## Tecnologias Utilizadas

- **Backend:** Python / FastAPI
- **Database:** PostgreSQL

## Personas

### Marcinho - Dono da Agência
- **Idade:** 35 anos
- **Objetivo:** Sistema para cadastro de clientes e controle de assentos vendidos
- **Frustrações:** Problemas com reserva de assentos usando modelo físico em pranchetas
- **Necessidades:** 
  - Gerenciamento digital de excursões
  - Cadastro e controle de clientes
  - Reserva de assentos digital
  - Gerenciamento de ônibus e roteiros

## Histórias de Usuário

| Como | Quero | Para |
|------|-------|------|
| Dono da agência | Gerenciar clientes (cadastro e histórico) | Evitar repetição de coleta de dados e manter informações no banco |
| Dono da agência | Gerenciar ônibus (cadastro e disponibilidade) | Ter maior controle sobre a frota disponível |
| Dono da agência | Gerenciar roteiros (destinos e paradas) | Manter informações organizadas sobre embarques e itinerários |
| Dono da agência | Marcar e liberar assentos digitalmente | Manter controle preciso da disponibilidade em viagens |

## Requisitos Funcionais

| ID | Título | Descrição | Prioridade |
|----|--------|-----------|------------|
| RF-01 | Gerenciamento de Cliente | CRUD completo de clientes | ALTA |
| RF-02 | Gerenciamento de Ônibus | CRUD completo de ônibus | ALTA |
| RF-03 | Gerenciamento de Roteiro | CRUD completo de roteiros | ALTA |
| RF-04 | Gerenciamento de Excursão | CRUD completo de excursões | ALTA |
| RF-05 | Gerenciamento de Assentos | Reserva e liberação de assentos | ALTA |
| RF-06 | Busca de Cliente | Busca por diversos critérios | BAIXA |
| RF-07 | Busca de Excursão | Busca por código, destino e hotel | BAIXA |
| RF-08 | Filtro por Data | Filtragem por data de saída/retorno | BAIXA |

## Requisitos Não Funcionais

| ID | Título | Descrição | Prioridade |
|----|--------|-----------|------------|
| RNF-01 | Desempenho | Suporte a 10 acessos simultâneos | ALTA |
| RNF-02 | Escalabilidade | Crescimento sem perda de performance | ALTA |
| RNF-03 | Usabilidade | Interface intuitiva e fácil navegação | MÉDIA |
| RNF-04 | Disponibilidade | 99% de uptime (24/7) | ALTA |
| RNF-05 | Compatibilidade | Principais navegadores web | ALTA |
| RNF-06 | Backup e Recuperação | Backups regulares e recuperação rápida | ALTA |

## Licença

Este projeto está sob a licença [LICENSE]. Veja o arquivo `LICENSE` para mais detalhes.


## Documentação Adicional

## Alembic com autogenerate

O projeto agora está preparado para gerar migrations automaticamente a partir dos models SQLAlchemy.

### Como funciona

- O Alembic usa `Base.metadata` definido em `app/database/session.py`.
- O arquivo `alembic/env.py` importa o pacote `model` para registrar todos os models antes do `autogenerate`.
- A URL do banco é lida da variável `database_url` no `.env`.

### Comandos

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Garanta que o `.env` tenha `database_url` apontando para o PostgreSQL.

3. Gere uma migration automática:

```bash
alembic revision --autogenerate -m "create tables"
```

4. Aplique as migrations:

```bash
alembic upgrade head
```

### Se o autogenerate não encontrar mudanças

Verifique se:

- o model novo foi importado em `app/model/__init__.py`;
- ele herda de `ModelBase` ou `BaseNoId`;
- a variável `target_metadata` em `alembic/env.py` está como `Base.metadata`.


⭐ **Gostou do projeto? Deixe uma estrela!**



