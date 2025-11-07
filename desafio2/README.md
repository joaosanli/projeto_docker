# Desafio 2 — Volumes e Persistência (SQLite)

## Objetivo
Demonstrar persistência de dados com **volumes Docker** usando SQLite.

## Arquitetura
- Container Python escreve em `/data/app.db` (montado como volume).
- Ao remover o container e recriá-lo, os dados permanecem no volume.

## Como executar
1. Construir a imagem:
   ```bash
   docker build -t d2-sqlite .
   ```

2. Rodar a primeira vez (cria/atualiza DB e imprime registros):
   ```bash
   bash test.sh run
   ```

3. Remover o container e rodar novamente (sem apagar o volume):
   ```bash
   bash test.sh rerun
   ```
   Você verá que os registros **persistem**.

4. Limpar (remove container e volume):
   ```bash
   bash test.sh clean
   ```

## Decisões técnicas
- SQLite facilita a demonstração, pois não requer outro serviço.
- A aplicação insere um registro de timestamp a cada execução, provando a persistência.
