# VULNERABILITY: Using a massive base image (includes compilers, shells, and tools)
FROM python:3.11

# VULNERABILITY: Running as root by default
WORKDIR /app

# VULNERABILITY: Copying sensitive local files (like .env or .git) into the image
COPY app/ .

# VULNERABILITY: No caching optimization for layers
RUN pip install flask redis rq

# VULNERABILITY: Exposing a privileged port
EXPOSE 80

# VULNERABILITY: Using a shell-based entrypoint which is susceptible to shell injection
CMD python app.py