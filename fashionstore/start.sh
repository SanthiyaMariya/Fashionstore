#!/bin/bash
echo "===================================="
echo "  StyleHub - Fashion Store Setup"
echo "===================================="

echo ""
echo "[1/3] Installing Django..."
pip install -r requirements.txt

echo ""
echo "[2/3] Setting up database..."
python manage.py migrate

echo ""
echo "[3/3] Loading sample data..."
python seed_data.py

echo ""
echo "===================================="
echo "  Starting server at:"
echo "  http://127.0.0.1:8000"
echo ""
echo "  Login: demo / demo1234"
echo "  Admin: admin / admin123"
echo "===================================="
echo ""
python manage.py runserver
