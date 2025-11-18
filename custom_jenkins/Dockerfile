# Base Jenkins image (Debian trixie, arm64 on Mac M2)
FROM jenkins/jenkins:lts

# Become root to install packages
USER root

# Install Docker CLI from Debian repo
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg docker.io && \
    apt-get clean

# Add Jenkins user to docker group so it can run `docker` without sudo
RUN groupadd -f docker && \
    usermod -aG docker jenkins && \
    mkdir -p /var/lib/docker

VOLUME /var/lib/docker

# Go back to Jenkins user
USER jenkins