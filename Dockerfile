# Use Qdrant as the base image
FROM qdrant/qdrant:latest

# Set the working directory
WORKDIR /app

# Install system dependencies for Python and Streamlit
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code into the container
COPY . /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="/root/.local/bin:$PATH" && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Expose ports for Qdrant and Streamlit
EXPOSE 6333 8501

# Command to start Qdrant and Streamlit
CMD ["sh", "-c", "/qdrant run & streamlit run vdb3170/app.py"]
