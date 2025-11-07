# Desafio 4 — Microsserviços Independentes (HTTP)

## Objetivo
Criar 2 microsserviços que se comunicam via HTTP:
- **servicoA**: `/users` retorna JSON com lista de usuários.
- **servicoB**: chama `servicoA` e expõe `/report` com texto agregado.

## Execução rápida
Em dois terminais (ou usando duas janelas):

1. Build e run do A:
   ```bash
   cd servicoA
   docker build -t d4-a .
   docker run --rm -p 5100:5000 --name d4-a d4-a
   ```

2. Build e run do B (que consome A):
   ```bash
   cd servicoB
   docker build -t d4-b .
   docker run --rm -p 5200:5000 -e A_URL=http://host.docker.internal:5100 d4-b
   ```

Testes:
- `curl http://localhost:5100/users`
- `curl http://localhost:5200/report`

> Em Linux sem `host.docker.internal`, substitua por IP do host/redes customizadas.
