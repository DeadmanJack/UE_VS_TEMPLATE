# Unreal Engine 5 VS Code Template

This template provides a complete VS Code configuration for Unreal Engine 5 development, including build tasks, debug configurations, and IntelliSense setup.

## What's Included

- **VS Code Configuration** (`.vscode/` folder):
  - `tasks.json` - Build tasks for compiling UE5 projects
  - `launch.json` - Debug configurations for editor and game launch
  - `c_cpp_properties.json` - IntelliSense configuration with UE5 include paths

- **Git Configuration**:
  - `.gitignore` - Comprehensive UE5 gitignore with VS Code support
  - `.gitattributes` - Git attributes for UE5 projects

- **Visual Studio Configuration**:
  - `.vsconfig` - VS configuration for UE5 development components

## Usage

1. **For New Projects**: Copy this template to your new UE5 project directory, **excluding the `.git` folder** (which contains this template's repository history):
   ```bash
   # Option 1: Clone without git history
   git clone --depth 1 <template-repo-url> <your-project-name>
   cd <your-project-name>
   rm -rf .git
   git init
   
   # Option 2: Download and extract template files manually
   # Copy all files except .git/ directory
   
   # Option 3: Use GitHub's "Use this template" button
   # This automatically creates a new repo without the template's git history
   ```

2. **Update Project Name**: Edit the following files to replace "EvilForces" with your project name:
   - `.vscode/tasks.json` - Update all task labels and project references
   - `.vscode/launch.json` - Update configuration names and executable paths
   - `.vscode/c_cpp_properties.json` - Update configuration names and compileCommands path:
     ```json
     "compileCommands": "${workspaceFolder}/.vscode/compileCommands_YourProjectName.json"
     ```

3. **Generate Project Files**: Run the "Generate Project Files" task in VS Code to create the missing `compileCommands_*.json` files

## Quick Setup (Optional)

Use the included Python script to automatically update project names:
```bash
python setup_new_project.py YourProjectName
```

This will replace all "EvilForces" references with your project name in the configuration files.

## Build Tasks Available

- **Build Project** - Compile your UE5 project
- **Rebuild Project** - Clean and compile your UE5 project  
- **Generate Project Files** - Regenerate VS Code project files

## Debug Configurations

- **Launch Editor** - Start UE5 Editor with your project
- **Launch Game** - Start your game directly

## Requirements

- Unreal Engine 5.6+ installed
- Visual Studio Code with C/C++ extension
- Windows 10/11 (paths configured for Windows)

## Customization

The template uses standard UE5 paths. If you have UE5 installed in a custom location, update the paths in:
- `.vscode/tasks.json` (UnrealBuildTool path)
- `.vscode/launch.json` (UE5 Editor path)
- `.vscode/c_cpp_properties.json` (UE5 Engine directory)

## Python Script Integration

This template is designed to work with automated setup scripts that can:
- Clone this template repository (without .git history)
- Rename project-specific references
- Initialize new UE5 projects with proper VS Code configuration

---

*Template created for streamlined UE5 development workflow*
