FROM alpine:latest AS builder
LABEL maintainer="upnt <upnt.github@gmail.com>" \
      version="stable"
RUN apk add --no-cache --update \
        build-base cmake automake autoconf \
        libtool pkgconf coreutils curl unzip \
        gettext-tiny-dev git \
 && git clone --depth 1 -b stable https://github.com/neovim/neovim.git \
 && cd neovim \
 && make CMAKE_BUILD_TYPE=Debug \
 && make install

FROM alpine:latest
RUN apk add --no-cache --update libgcc
WORKDIR /root/
COPY --from=builder /usr/local /usr/local
CMD nvim
