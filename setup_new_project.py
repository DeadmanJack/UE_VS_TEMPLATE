#!/usr/bin/env python3
"""
UE5 VS Code Template Setup Script

This script helps you set up a new UE5 project using this VS Code template.
It automatically replaces project-specific references and updates file paths.
"""

import os
import sys
import re
import json
import shutil
from pathlib import Path

def get_engine_path_from_uproject(uproject_path):
    """Extract engine path from .uproject file."""
    try:
        with open(uproject_path, 'r', encoding='utf-8') as f:
            project_data = json.load(f)
        
        engine_association = project_data.get('EngineAssociation', '')
        
        # Common UE5 engine association GUIDs and their typical paths
        engine_paths = {
            # UE5 Source Build
            "{48190AF0-4459-AFA2-500C-E2BF890C9712}": "D:\\UE5\\Engine",
            # UE5.4 from Epic Games Launcher
            "{E6B8C5C0-4C1A-4C1A-4C1A-4C1A4C1A4C1A}": "C:\\Program Files\\Epic Games\\UE_5.4\\Engine",
            # UE5.3 from Epic Games Launcher  
            "{D6B8C5C0-4C1A-4C1A-4C1A-4C1A4C1A4C1A}": "C:\\Program Files\\Epic Games\\UE_5.3\\Engine",
            # UE5.2 from Epic Games Launcher
            "{C6B8C5C0-4C1A-4C1A-4C1A-4C1A4C1A4C1A}": "C:\\Program Files\\Epic Games\\UE_5.2\\Engine",
            # UE5.1 from Epic Games Launcher
            "{B6B8C5C0-4C1A-4C1A-4C1A-4C1A4C1A4C1A}": "C:\\Program Files\\Epic Games\\UE_5.1\\Engine",
            # UE5.0 from Epic Games Launcher
            "{A6B8C5C0-4C1A-4C1A-4C1A-4C1A4C1A4C1A}": "C:\\Program Files\\Epic Games\\UE_5.0\\Engine",
        }
        
        # Try to get path from mapping
        if engine_association in engine_paths:
            engine_path = engine_paths[engine_association]
            # Verify the path exists
            if os.path.exists(engine_path):
                return engine_path
        
        # If not found in mapping, try to detect from project location
        # Look for common UE5 installation patterns
        project_dir = os.path.dirname(os.path.abspath(uproject_path))
        
        # Check if project is inside a UE5 source build
        for parent in Path(project_dir).parents:
            if (parent / "Engine" / "Binaries" / "Win64" / "UnrealEditor.exe").exists():
                return str(parent / "Engine")
        
        # Check common Epic Games Launcher locations
        epic_locations = [
            "C:\\Program Files\\Epic Games\\UE_5.4\\Engine",
            "C:\\Program Files\\Epic Games\\UE_5.3\\Engine", 
            "C:\\Program Files\\Epic Games\\UE_5.2\\Engine",
            "C:\\Program Files\\Epic Games\\UE_5.1\\Engine",
            "C:\\Program Files\\Epic Games\\UE_5.0\\Engine",
        ]
        
        for location in epic_locations:
            if os.path.exists(location):
                return location
        
        print(f"⚠ Warning: Could not detect UE5 engine path for association: {engine_association}")
        return None
        
    except Exception as e:
        print(f"✗ Error reading .uproject file: {e}")
        return None

def replace_in_file(file_path, old_project, new_project, old_engine_path=None, new_engine_path=None):
    """Replace project name and engine path references in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace project name references
        content = content.replace(old_project, new_project)
        
        # Replace engine path references if provided
        if old_engine_path and new_engine_path:
            # Handle different path formats (forward/backward slashes)
            old_engine_path_forward = old_engine_path.replace('\\', '/')
            new_engine_path_forward = new_engine_path.replace('\\', '/')
            old_engine_path_backward = old_engine_path.replace('/', '\\')
            new_engine_path_backward = new_engine_path.replace('/', '\\')
            
            content = content.replace(old_engine_path_forward, new_engine_path_forward)
            content = content.replace(old_engine_path_backward, new_engine_path_backward)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {file_path}")
    except Exception as e:
        print(f"✗ Error updating {file_path}: {e}")

def setup_new_project(new_project_name):
    """Set up a new UE5 project with the given name."""
    
    # Find the .uproject file
    uproject_file = None
    for file in os.listdir('.'):
        if file.endswith('.uproject'):
            uproject_file = file
            break
    
    if not uproject_file:
        print("✗ Error: No .uproject file found in current directory")
        return
    
    print(f"Found project file: {uproject_file}")
    
    # Detect engine path from .uproject
    engine_path = get_engine_path_from_uproject(uproject_file)
    if not engine_path:
        print("✗ Error: Could not detect UE5 engine path")
        return
    
    print(f"Detected UE5 engine path: {engine_path}")
    
    # Files that need project name updates
    files_to_update = [
        '.vscode/tasks.json',
        '.vscode/launch.json', 
        '.vscode/c_cpp_properties.json'
    ]
    
    old_project = "EvilForces"
    old_engine_path = "C:\\UE5\\UnrealEngine\\Engine"  # Default template path
    
    print(f"Setting up new UE5 project: {new_project_name}")
    print(f"Replacing '{old_project}' with '{new_project_name}' in configuration files...")
    print(f"Updating engine paths from '{old_engine_path}' to '{engine_path}'...")
    
    # Update each file
    for file_path in files_to_update:
        if os.path.exists(file_path):
            replace_in_file(file_path, old_project, new_project, old_engine_path, engine_path)
        else:
            print(f"⚠ Warning: {file_path} not found")
    
    print(f"\n✓ Project setup complete!")
    print(f"\nNext steps:")
    print(f"1. Reload VS Code/Cursor window to detect new configuration")
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
