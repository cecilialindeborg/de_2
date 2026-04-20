#chmod +x setup.sh
#./setup.sh

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing Java..."
sudo apt install -y openjdk-17-jdk

echo "Installing Docker..."
sudo apt install -y docker.io

echo "Starting and enabling Docker..."
sudo systemctl start docker
sudo systemctl enable docker

echo "Adding user to docker group..."
sudo usermod -aG docker $USER

echo "Setup complete!"
echo "Log out and back in (or run 'newgrp docker') to use Docker without sudo."
