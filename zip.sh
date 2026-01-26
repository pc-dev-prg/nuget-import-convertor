#!/bin/bash

# Name of the output ZIP file
ZIP_NAME="nuget-payroll-transformer.zip"
# Name of the folder inside the ZIP
FOLDER_NAME="nuget-payroll-transformer"

# Remove existing zip if it exists
rm -f "$ZIP_NAME"

# Create a temporary directory
mkdir -p "$FOLDER_NAME"

# Copy required files (excluding Manual.md as requested)
cp main.py "$FOLDER_NAME/"
cp transformer.py "$FOLDER_NAME/"
cp schemas.py "$FOLDER_NAME/"
cp requirements.txt "$FOLDER_NAME/"
cp run.bat "$FOLDER_NAME/"
cp Manual.pdf "$FOLDER_NAME/"

# Create the ZIP archive
zip -r "$ZIP_NAME" "$FOLDER_NAME"

# Clean up temporary directory
rm -rf "$FOLDER_NAME"

echo "Archive $ZIP_NAME has been created successfully."
