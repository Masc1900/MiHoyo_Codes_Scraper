#!/bin/bash

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Build the executable using PyInstaller
pyinstaller --noconfirm --onefile --console --name "Mihoyo Code Scraper" --add-data "$PROJECT_DIR/src/functions.py:." --distpath "$PROJECT_DIR/dist" --workpath "$PROJECT_DIR/build" --specpath "$PROJECT_DIR/specs" "$PROJECT_DIR/src/main.py"
