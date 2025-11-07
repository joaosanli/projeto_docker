#!/usr/bin/env bash
set -e

NET=d1-net

case "$1" in
  build|"")
    docker build -t d1-server -f Dockerfile.server .
    docker build -t d1-client -f Dockerfile.client .
    docker network create $NET || true
    echo "Build ok. Rede $NET pronta."
    ;;
  up)
    docker rm -f d1-server d1-client 2>/dev/null || true
    docker run -d --name d1-server --network $NET -p 8080:8080 d1-server
    docker run -d --name d1-client --network $NET -e TARGET_URL=http://d1-server:8080/ d1-client
    echo "Containers iniciados. d1-server em localhost:8080"
    ;;
  down)
    docker rm -f d1-server d1-client 2>/dev/null || true
    docker network rm $NET 2>/dev/null || true
    echo "Tudo limpo."
    ;;
  *)
    echo "Uso: bash run.sh [build|up|down]"
    ;;
esac
