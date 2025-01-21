FROM nginx:latest

# Install CA certificates
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

# Copy custom configuration files
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

# Create a directory for logs
RUN mkdir -p /var/log/nginx/custom_logs && \
    chmod -R 777 /var/log/nginx/custom_logs

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

