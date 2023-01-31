#/bin/bash

SHELL_PATH=$(dirname $(readlink -f "$0"))

cd $SHELL_PATH

git add -A
git commit -m "default messages"
git pull
git push
