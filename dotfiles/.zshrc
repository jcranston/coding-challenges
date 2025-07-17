export ZSH="/root/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git)
source $ZSH/oh-my-zsh.sh

# Project-specific aliases
alias ll='ls -alF --color=auto'

# Pretty-print Python files with bat
alias catpy='bat --style=plain --language=python'
# Use bat for syntax-highlighted file viewing instead of cat
alias cat='bat --paging=never'
alias gs='git status' 