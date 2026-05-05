#!/bin/bash
# Setup script for WSL environment with Odoo

set -e  # Exit on error

echo "=== Setting up Odoo To-Do Module in WSL ==="
echo ""

# Navigate to project directory
cd /mnt/e/to_do_odoo_task

# Create virtual environment
echo "Step 1: Creating Python virtual environment..."
python3 -m venv .venv
echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "Step 2: Activating virtual environment..."
source .venv/bin/activate
echo "✓ Environment activated"
echo ""

# Install dependencies
echo "Step 3: Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Create logs directory
echo "Step 4: Creating logs directory..."
mkdir -p logs
echo "✓ Logs directory created"
echo ""

# Create PostgreSQL note
echo "Step 5: PostgreSQL Setup (IMPORTANT):"
echo "  Option A: Use Docker with PostgreSQL"
echo "    Run: docker run -d -e POSTGRES_PASSWORD=odoo -e POSTGRES_USER=odoo -p 5432:5432 postgres:15"
echo ""
echo "  Option B: Install PostgreSQL locally"
echo "    sudo apt-get install postgresql postgresql-contrib"
echo "    sudo service postgresql start"
echo ""

echo "=== Setup Complete ==="
echo ""
echo "Next Steps:"
echo "1. Ensure PostgreSQL is running (use Option A or B above)"
echo ""
echo "2. Install Odoo from GitHub (first time only):"
echo "   mkdir ~/odoo-src && cd ~/odoo-src"
echo "   git clone https://github.com/odoo/odoo.git --depth 1 --branch 16.0 odoo"
echo "   cd odoo && pip install -e ."
echo ""
echo "3. Run Odoo with this module:"
echo "   cd /mnt/e/to_do_odoo_task"
echo "   source .venv/bin/activate"
echo "   odoo -c odoo.conf"
echo ""
echo "4. Access Odoo at: http://localhost:8069"
echo ""
