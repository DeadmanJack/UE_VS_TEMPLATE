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

## Usage

1. **For New Projects**: Copy this entire template to your new UE5 project directory
2. **Update Project Name**: Edit `.vscode/c_cpp_properties.json` and change the `compileCommands` path:
   ```json
   "compileCommands": "${workspaceFolder}/.vscode/compileCommands_YourProjectName.json"
   ```
3. **Update Launch Configurations**: If your project name differs from "EvilForces", update the executable paths in `.vscode/launch.json`

## Build Tasks Available

- **Build Project** - Compile your UE5 project
- **Build Project (Debug)** - Compile with debug symbols
- **Clean Project** - Clean build artifacts
- **Generate Project Files** - Regenerate VS Code project files

## Debug Configurations

- **Launch Editor** - Start UE5 Editor with your project
- **Launch Game** - Start your game directly
- **Attach to Process** - Attach debugger to running UE5 process

## Requirements

- Unreal Engine 5.6+ installed
- Visual Studio Code with C/C++ extension
- Windows 10/11 (paths configured for Windows)

## Customization

The template uses standard UE5 paths. If you have UE5 installed in a custom location, update the paths in:
- `.vscode/tasks.json` (UnrealBuildTool path)
- `.vscode/launch.json` (UE5 Editor path)

## Python Script Integration

This template is designed to work with automated setup scripts that can:
- Clone this template repository
- Rename project-specific references
- Initialize new UE5 projects with proper VS Code configuration

---

*Template created for streamlined UE5 development workflow*
