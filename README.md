���^�[�~�i�����Ђ炭

���ȉ��̃R�}���h�����s
�����̉�ʂł̓L�[�{�[�h�������Ă������\������܂��񂪁A�p�X���[�h����͂��AEnter�L�[�������Ă��������B
���C���X�g�[���̓r���ŁuEnter�L�[�v���������Ƃ����߂��܂�


/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


-----------------------------------------------------------
M1���ڂ�Mac�̏ꍇ�A����Ɉȉ���2�̃R�}���h�����s���Ă��������B
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
source ~/.zshrc
-----------------------------------------------------------


�����L�̂T�s���R�s�y���Ď��s
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

�����L�̂P�s���R�s�y���Ď��s
pyenv install 3.9.13
�����΂炭���Ԃ�������܂�

��
pyenv global 3.9.13

�����̃t�@�C���̂����Ă���f�B���N�g���i�t�H���_�j�̂P���ɂ���
cd src

�����s�ɕK�v�ȃ��W���[�����Z�b�g
pip3 install -r requirements.txt

�����s
python3 main.py

