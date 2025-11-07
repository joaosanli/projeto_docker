# Desafio 1 — Containers em Rede (Flask + curl)

## Objetivo
Dois containers comunicando-se via **rede Docker customizada**:
- **server** (Flask) expõe a porta 8080 e responde com um JSON simples
- **client** executa `curl` periodicamente para o `server` e imprime logs

## Arquitetura
- Rede Docker: `d1-net`
- Containers: `d1-server` e `d1-client`
- Comunicação: HTTP (client -> server)

## Como executar
> Pré-requisitos: Docker instalado.

1. Criar a rede e construir as imagens:
   ```bash
   bash run.sh build
   ```

2. Subir o servidor e o cliente:
   ```bash
   bash run.sh up
   ```

3. Ver logs da comunicação (CTRL+C para sair do tail):
   ```bash
   docker logs -f d1-client
   ```

4. Encerrar e limpar (containers e rede):
   ```bash
   bash run.sh down
   ```

## Decisões técnicas
- Flask foi escolhido por simplicidade.
- O `client` usa `curl` em loop (busybox) para reduzir a imagem.

## Teste esperado
No log do `d1-client`, você verá respostas HTTP do `d1-server` a cada 2s com timestamp e contador.
