FROM debian:buster-slim AS builder
LABEL maintainer="upnt <upnt.github@gmail.com>" \
      version="v0.7.0-debian-debug"
RUN apt update && \
    apt install -y \
        ninja-build gettext libtool libtool-bin \
        autoconf automake cmake g++ pkg-config \
        unzip curl doxygen git \
 && git clone --depth 1 -b v0.7.0 https://github.com/neovim/neovim.git \
 && cd neovim \
 && make CMAKE_BUILD_TYPE=Debug \
 && make install

FROM debian:buster-slim
RUN apt-get update \
 && apt-get install -y locales \
 && locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LC_CTYPE=en_US.UTF-8
WORKDIR /root/
COPY --from=builder /usr/local /usr/local
CMD nvim
