# How to use this Docker Development Environment

This is a step by step guide in how to create a docker image and do remote development in a docker container.

1. [Install VSCODE](https://code.visualstudio.com/download)
2. [Install Remote-Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. [Install Docker](https://www.docker.com/products/docker-desktop)
4. [Create a repository from this repo template](https://help.github.com/en/articles/creating-a-repository-from-a-template)
5. Clone that repo onto your local desktop: `git clone YOUR-URL`
6. Open the local desktop repo workspace in vscode
7. Follow the prompts in the lower right-hand corner to reopen the repo in a container
8. Wait for the image and container to launch
9. BAM! You're ready to start remote Docker development with full vscode features

Note: Files are mounted onto the container vs. being copied into the container. If you launch the container by itself without vscode, it should be empty.
