FROM python:3.11-bullseye

ARG DEBIAN_FRONTEND=noninteractive

ENV container docker
ENV ZSH_CUSTOM /root/.oh-my-zsh/custom
ENV WORKDIR "/workspace/project-a"

USER root

RUN apt-get update --allow-insecure-repositories\
    && apt-get install\
        build-essential\
        curl\
        git-all\
        graphviz\
        htop\
        nano\
        wget\
        zsh\
        -y --no-install-recommends\
    && apt-get upgrade -y\
    && apt-get full-upgrade -y\
    && apt-get autoremove -y\
    && apt-get autoclean -y\
    && apt-get clean\
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade --no-cache-dir wheel pip poetry==1.8.0

COPY poetry.lock* pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --all-extras --no-root

RUN yes Y | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
RUN ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="spaceship"/g' ~/.zshrc

RUN echo 'plugins=(git git-flow)' >> ~/.zshrc
