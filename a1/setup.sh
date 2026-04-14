#bash setup.sh

echo "Updating system..."
sudo apt update -y && sudo apt upgrade -y

echo "Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

echo "Setting up Docker permissions..."
sudo groupadd docker || true
sudo usermod -aG docker $USER
newgrp docker

echo "Building Task 1 container..."
docker build -f Dockerfile.task1 -t mycontainer/first:v1 .

echo "Building Spark container..."
docker build -f Dockerfile.spark -t sparkaio/first:v0 .

echo "Starting Spark cluster with docker compose..."
docker compose up -d

echo "Done! Use 'docker ps' to check containers."