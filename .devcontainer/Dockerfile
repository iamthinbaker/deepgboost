FROM python:3.12-slim

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @anthropic-ai/claude-code

RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && apt-get update && apt-get install -y sudo \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

USER ${USERNAME}

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
