FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    emacs-nox \
    git \
    htop \
    curl \
    build-essential \
    python3-venv \
    python3-pip \
    zsh \
    bat \
    && rm -rf /var/lib/apt/lists/*

# Install Oh My Zsh (unattended)
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" --unattended

# Copy project-specific .zshrc
COPY dotfiles/.zshrc /root/.zshrc

# Set workdir
WORKDIR /workspace

# Copy only pyproject.toml and poetry.lock first for caching
COPY pyproject.toml poetry.lock* ./

# Install Poetry via pip and install dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

RUN ln -s /usr/bin/batcat /usr/local/bin/bat

# Copy the rest of the code
COPY . .

# Add scripts directory to PATH
ENV PATH="/workspace/scripts:$PATH"

# Set zsh as the default shell
SHELL ["/bin/zsh", "-c"]
CMD ["zsh"] 