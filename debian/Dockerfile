FROM debian:bookworm-slim AS builder
ARG NEOVIM_VERSION=stable \
    BUILD_TYPE=RelWithDebInfo
RUN <<EOF
    apt-get update
    apt-get install -y ninja-build gettext cmake unzip curl git
    git clone https://github.com/neovim/neovim -b ${NEOVIM_VERSION} --depth 1 --single-branch
    cd neovim
    make CMAKE_BUILD_TYPE=${BUILD_TYPE}
    make install
EOF


FROM debian:bookworm-slim
COPY --from=node:20-bookworm-slim /usr/local/ /usr/local
RUN <<EOF
    apt-get update
    apt-get install -y locales build-essential
    apt-get install -y libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libbz2-dev liblzma-dev zlib1g-dev uuid-dev libffi-dev libdb-dev
    apt-get clean -y
    rm -rf /var/lib/apt/lists/*
EOF
RUN <<EOF
    echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen
    locale-gen ja_JP.UTF-8
    npm install --location=global neovim
EOF
COPY --from=builder /usr/local/ /usr/local
ENV TERM=xterm-256color \
    LANG=ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8
