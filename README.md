★ターミナルをひらく

★以下のコマンドを実行
※この画面ではキーボードを押しても何も表示されませんが、パスワードを入力し、Enterキーを押してください。
※インストールの途中で「Enterキー」を押すことを求められます


/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


-----------------------------------------------------------
M1搭載のMacの場合、さらに以下の2つのコマンドを実行してください。
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
source ~/.zshrc
-----------------------------------------------------------


★下記の５行をコピペして実行
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

★下記の１行をコピペして実行
pyenv install 3.9.13
※しばらく時間がかかります

★
pyenv global 3.9.13

★このファイルのおいてあるディレクトリ（フォルダ）の１つ下にする
cd src

★実行に必要なモジュールをセット
pip3 install -r requirements.txt

★実行
python3 main.py

