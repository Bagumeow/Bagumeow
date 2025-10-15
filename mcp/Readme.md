# MCP Setup Guide

## 1. Create Python Environment

```bash
# Create a new conda environment named 'mcp' with Python 3.12
python -m venv .mcp   

# Activate the environment
source .mcp/bin/activate
```

## 2. Install Required Packages

```bash
# Install MCP and CLI tools
pip install "mcp[cli]"
```

## 3. Verify Python Location

```bash
# This command will show the path to your Python environment
where python
```

## 4. Create Configuration File

Create a configuration file with the following content (replace `{location python}` with the Python path you found in step 3):

```json
{
  "mcpServers": {
    "mcp-server": {
      "command": "{location python}",
      "args": ["{path file mcp_server.py}"]
    }
  }
}
```

### Notes:

- Make sure you have Conda installed on your computer
- Always remember to activate the environment using `conda activate mcp` before working
- The configuration file should be placed in the correct location in your project
