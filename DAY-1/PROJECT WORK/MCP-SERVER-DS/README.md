# Build Your First MCP Server: Leave Management
This AI tool helps an HR with leave management related tasks. The codebase here 
is for MCP server that interacts with mock leave database and responds to MCP client queries

# Setup steps
1. Install Claude Desktop
2. You can use docker container for Ubuntu Linux
3. Commands are given below

      IMAGE_NAME="ke5haav/claude-desktop-builder:latest"
      DEB_FILE="claude-desktop_0.12.55_amd64.deb"      
      docker pull $IMAGE_NAME && \
      docker create --name claude-temp $IMAGE_NAME && \
      docker cp claude-temp:/home/appuser/claude-desktop-debian/$DEB_FILE . && \
      sudo dpkg -i $DEB_FILE && \
      sudo apt-get -f install -y && \
      rm $DEB_FILE && \
      echo "Done. Run: claude-desktop"
5. install mcp using `pip install mcp`
6. Install uv by running `pip install uv`
7. Run `uv init my-first-mcp-server` to create a project directory
8. Run `uv add "mcp[cli]"` to add mcp cli in your project
9. Few folks may get type errors for which you can run `pip install --upgrade typer` to upgrade typer library to its latest version
10. Write code in main.py for leave management server
11. Install this server inside Claude desktop by running `uv run mcp install main.py` in the project directory
12. Kill any running instance of Claude from Task Manager. Restart Claude Desktop
13. In Claude desktop, now you will see tools from this server

@All rights reserved. Codebasics Inc. LearnerX Pvt Ltd. 




