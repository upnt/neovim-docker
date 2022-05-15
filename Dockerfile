FROM alpine:latest AS builder
LABEL maintainer="upnt <upnt.github@gmail.com>" \
      version="1.0"
RUN apk update && \
    apk add --no-cache \
        build-base cmake automake autoconf \
        libtool pkgconf coreutils curl unzip \
        gettext-tiny-dev git \
 && git clone --depth 1 -b v0.7.0 https://github.com/neovim/neovim.git \
 && cd neovim \
 && make CMAKE_BUILD_TYPE=RelWithDebInfo \
 && make install

FROM alpine:latest
RUN apk add --no-cache libgcc
WORKDIR /root/
COPY --from=builder /usr/local /usr/local
CMD nvim