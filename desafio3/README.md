# Desafio 3 — Docker Compose (web + db + cache)

## Objetivo
Orquestrar 3 serviços com `docker-compose`:
- **web**: Flask
- **db**: PostgreSQL
- **cache**: Redis

## Como executar
1. Criar arquivo `.env` (opcional; valores padrão já são definidos no compose).
2. Subir tudo:
   ```bash
   docker compose up -d --build
   ```
3. Testes:
   - Saúde: `curl http://localhost:5000/health`
   - Cache (incremento): `curl http://localhost:5000/hit`
   - DB (listar usuários): `curl http://localhost:5000/users`
4. Encerrar:
   ```bash
   docker compose down -v
   ```

## Decisões técnicas
- `depends_on` garante ordem básica, mas a app também faz retry para DB/Redis.
- Variáveis de ambiente parametrizam host/porta/credenciais.
