# BASE IMAGE with an alias #
#FROM harbor-repo.vmware.com/dockerhub-proxy-cache/library/node:14.15.0 as build
FROM node:14.15.0 as build
WORKDIR /app

# Install Angular CLI to run Build #
RUN npm install -g @angular/cli@13.3.11
