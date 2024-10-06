FROM lscr.io/linuxserver/code-server:4.23.1-ls207

ARG DEBIAN_FRONTEND=noninteractive

#or ~/.nvm , depending
ENV NVM_DIR /usr/local/.nvm

ENV NODE_VERSION v20.15.0

# replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN mkdir $NVM_DIR && PROFILE=/root/.bashrc curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
RUN . $NVM_DIR/nvm.sh \
    && nvm alias default $NODE_VERSION \
    && nvm use default && cp /root/.bashrc /$home/.bashrc

ENV NODE_PATH $NVM_DIR/$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/$NODE_VERSION/bin:$PATH
