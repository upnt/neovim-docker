FROM debian:buster-slim AS builder
LABEL maintainer="upnt <upnt.github@gmail.com>" \
      version="nightly"
RUN apt update \
 && apt install -y \
    ninja-build ninja-build gettext libtool libtool-bin \
    autoconf automake cmake g++ pkg-config \
    unzip curl doxygen git \
 && git clone --depth 1 -b nightly https://github.com/neovim/neovim.git \
 && cd neovim \
 && make CMAKE_BUILD_TYPE=RelWithDebInfo \
 && make install

FROM debian:buster-slim
WORKDIR /root/
COPY --from=builder /usr/local/ /usr/local/
CMD nvim
