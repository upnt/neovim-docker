FROM alpine:latest
LABEL maintainer="upnt <upnt.github@gmail.com>" \
      version="1.0"
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:ja \
    LC_ALL=en_US.UTF-8

RUN apk update && \
    apk add --no-cache --virtual .builddeps \
            build-base cmake automake autoconf \
            libtool pkgconf coreutils curl unzip \
            gettext-tiny-dev git && \
    git clone https://github.com/neovim/neovim.git && \
    cd neovim && \
    git checkout stable && \
    make && \
    make install && \
    cd ../ && \
    rm -rf neovim && \
    apk del --purge .builddeps && \
    apk add libgcc
