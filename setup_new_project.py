#!/usr/bin/env python3
"""
UE5 VS Code Template Setup Script

This script helps you set up a new UE5 project using this VS Code template.
It automatically replaces project-specific references and updates file paths.
"""

import os
import sys
import re
import shutil
from pathlib import Path

def replace_in_file(file_path, old_project, new_project):
    """Replace project name references in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace project name references
        content = content.replace(old_project, new_project)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {file_path}")
    except Exception as e:
        print(f"✗ Error updating {file_path}: {e}")

def setup_new_project(new_project_name):
    """Set up a new UE5 project with the given name."""
    
    # Files that need project name updates
    files_to_update = [
        '.vscode/tasks.json',
        '.vscode/launch.json', 
        '.vscode/c_cpp_properties.json'
    ]
    
    old_project = "EvilForces"
    
    print(f"Setting up new UE5 project: {new_project_name}")
    print(f"Replacing '{old_project}' with '{new_project_name}' in configuration files...")
    
    # Update each file
    for file_path in files_to_update:
        if os.path.exists(file_path):
            replace_in_file(file_path, old_project, new_project_name)
        else:
            print(f"⚠ Warning: {file_path} not found")
    
    print(f"\n✓ Project setup complete!")
    print(f"\nNext steps:")
    print(f"1. Create your UE5 project: {new_project_name}.uproject")
    print(f"2. Run 'Generate Project Files' task in VS Code")
    print(f"3. Build your project using the build tasks")

def main():
    if len(sys.argv) != 2:
        print("Usage: python setup_new_project.py <new_project_name>")
        print("Example: python setup_new_project.py MyAwesomeGame")
        sys.exit(1)
    
    new_project_name = sys.argv[1]
    
    # Validate project name (UE5 naming conventions)
    if not re.match(r'^[A-Za-z][A-Za-z0-9_]*$', new_project_name):
        print("Error: Project name must start with a letter and contain only letters, numbers, and underscores")
        sys.exit(1)
    
    setup_new_project(new_project_name)

if __name__ == "__main__":
    main()
