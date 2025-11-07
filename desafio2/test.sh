#!/usr/bin/env bash
set -e
VOL=d2-sqlite-vol

case "$1" in
  run)
    docker rm -f d2-sqlite 2>/dev/null || true
    docker volume create $VOL >/dev/null || true
    docker run --name d2-sqlite --rm -v $VOL:/data d2-sqlite
    ;;
  rerun)
    docker run --name d2-sqlite --rm -v $VOL:/data d2-sqlite
    ;;
  clean)
    docker volume rm $VOL 2>/dev/null || true
    echo "Volume $VOL removido."
    ;;
  *)
    echo "Uso: bash test.sh [run|rerun|clean]"
    ;;
esac
