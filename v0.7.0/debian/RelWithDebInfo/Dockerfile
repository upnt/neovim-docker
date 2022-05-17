FROM <base-image> AS builder
LABEL maintainer="upnt <upnt.github@gmail.com>" \
      version="<version>"
RUN apk update && \
    apk add --no-cache \
        build-base cmake automake autoconf \
        libtool pkgconf coreutils curl unzip \
        gettext-tiny-dev git \
 && git clone --depth 1 -b <version> https://github.com/neovim/neovim.git \
 && cd neovim \
 && make CMAKE_BUILD_TYPE=<build-type> \
 && make install

FROM alpine:latest
RUN apk add --no-cache --update libgcc
WORKDIR /root/
COPY --from=builder /usr/local /usr/local
CMD nvim
