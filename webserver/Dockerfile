# Pull the minimal Ubuntu image
FROM ubuntu:22.04

# Install Nginx
RUN apt update -y && apt upgrade -y
RUN apt-get -y install nginx
RUN apt install -y nodejs

# Expose the port for access
EXPOSE 80/tcp

COPY ./src/index.html /var/www/html

# Run the Nginx server
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]