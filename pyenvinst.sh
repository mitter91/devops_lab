#!/bin/bash

BASHRC=$HOME'/.bashrc'

yum -y install epel-release
yum install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel

curl -L -s https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

cat >> $BASHRC << 'EOF'
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
EOF

source $BASHRC

pyenv install 2.7.17
pyenv install 3.7.6

pyenv global 3.7.6

pyenv virtualenv 2.7.17 cromwell-p2
pyenv virtualenv 3.7.6 cromwell-p3
