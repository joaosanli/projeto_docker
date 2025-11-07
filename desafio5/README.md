# Desafio 5 — Microsserviços com API Gateway (docker-compose)

## Objetivo
Arquitetura com **API Gateway** centralizando acesso a 2 microsserviços:
- **users**: fornece dados de usuários
- **orders**: fornece pedidos
- **gateway**: expõe `/users` e `/orders` e encaminha para os serviços

## Como executar
```bash
docker compose up -d --build
# Testes:
curl http://localhost:5050/users
curl http://localhost:5050/orders
```
Encerrar:
```bash
docker compose down -v
```

## Decisões técnicas
- Gateway implementado em Flask para manter stack homogênea.
- Comunicação intra-rede do compose via DNS dos serviços.
