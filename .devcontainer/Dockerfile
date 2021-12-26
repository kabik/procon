FROM pypy:3.8-7.3.7-slim

RUN apt update
RUN apt install -y \
        fish \
        fonts-powerline \
        git \
        curl

RUN curl https://git.io/fisher --create-dirs -sLo ~/.config/fish/functions/fisher.fish
RUN curl -L https://get.oh-my.fish | fish

ENTRYPOINT [ "/usr/bin/fish" ]
