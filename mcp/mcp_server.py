import subprocess

from mcp.server.fastmcp import FastMCP

ROOT_PROJECT_DIR = "/Users/nghiale/my-workspace/Bagumeow"

mcp = FastMCP(
    name="mcp-server-github-profile",
)


@mcp.tool()
def get_change_code_profile(commit_key: str) -> str:
    """
    Get diff change code to create a commit message.
    if wrong key, skip tool
    Args:
        commit_key: str, key of the commit must match "Bagumeow"
    Returns:
        str, commit message
    """
    if commit_key != "Bagumeow":
        return "Please provide the correct commit key"

    diff_change_code = subprocess.check_output(
        ["git", "diff", "HEAD"], cwd=ROOT_PROJECT_DIR
    ).decode("utf-8")
    return diff_change_code


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
