#!/bin/bash

# Set up a virtual environment
VENV_DIR="venv"

# Function to check if a Python module is installed
check_module() {
    python3 -c "import $1" 2>/dev/null
    return $?
}

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment!"
        read -p "Press any key to continue..."
        exit 1
    fi
fi

# Activate virtual environment
source $VENV_DIR/bin/activate

# Check for the PyYAML module and install if missing
if ! check_module yaml; then
    echo "Installing PyYAML module..."
    pip install pyyaml
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install PyYAML!"
        deactivate
        read -p "Press any key to continue..."
        exit 1
    fi
fi

# Check for the Pillow module and install if missing
if ! check_module PIL; then
    echo "Installing Pillow module..."
    pip install pillow
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install Pillow!"
        deactivate
        read -p "Press any key to continue..."
        exit 1
    fi
fi

rm -f zelda3_assets.dat 2>/dev/null
python3 assets/restool.py --extract-from-rom
if [ $? -ne 0 ]; then
  echo
  echo "ERROR: Asset extraction failed!"
  deactivate
  read -p "Press any key to continue..."
  exit 1
fi

if [ ! -f "zelda3_assets.dat" ]; then
  echo "ERROR: The python program didn't generate zelda3_assets.dat successfully."
  echo
  echo "ERROR: Asset extraction failed!"
  deactivate
  read -p "Press any key to continue..."
  exit 1
fi

echo "Complete!"
deactivate
read -p "Press any key to continue..."

