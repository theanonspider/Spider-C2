#!/usr/bin/env python3
"""
🕷️ Spider-C2 — Modular Command & Control Framework
Usage: python spiderc2.py --server
"""

import click
import json
import os
import sys
from datetime import datetime

try:
    from rich.console import Console
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

VERSION = "1.0.0"
CONFIG_FILE = "config.json"
TOKEN_FILE = "spiderc2.token"
BANNER = """
╔══════════════════════════════════════════════╗
║                                              ║
║   🕷️  SPIDER-C2 — Command & Control       ║
║                                              ║
║        Modular Framework v1.0               ║
║                                              ║
╚══════════════════════════════════════════════╝
"""

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"[!] Config file {CONFIG_FILE} not found.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def check_token():
    config = load_config()
    if not config.get("token_required", True):
        return True
    if not os.path.exists(TOKEN_FILE):
        print(f"[!] Authorization token required. Create {TOKEN_FILE}")
        return False
    with open(TOKEN_FILE, "r") as f:
        token = f.read().strip()
    if token != "SPIDER_C2_AUTHORIZED":
        print("[!] Invalid token.")
        return False
    return True

@click.group()
@click.version_option(version=VERSION, prog_name="Spider-C2")
def main():
    """🕷️ Spider-C2 — Modular Command & Control Framework"""
    pass

@main.command()
def server():
    """Start the C2 server"""
    if not check_token():
        sys.exit(1)
    
    config = load_config()
    print(BANNER)
    print(f"[*] Starting Spider-C2 server...")
    print(f"[*] Host: {config['server']['host']}")
    print(f"[*] Port: {config['server']['port']}")
    print(f"[*] Modules: {', '.join(config['modules'])}")
    print(f"[*] Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print("[i] Server module coming soon...")

@main.command()
@click.option("--type", "-t", default="windows", help="Agent type (windows/linux/macos)")
def generate(type):
    """Generate an agent"""
    if not check_token():
        sys.exit(1)
    
    print(f"[*] Generating {type} agent...")
    print(f"[i] Agent generation coming soon...")

@main.command()
def list():
    """List connected agents"""
    if not check_token():
        sys.exit(1)
    
    if RICH_AVAILABLE:
        console = Console()
        table = Table(title="Connected Agents")
        table.add_column("ID", style="cyan")
        table.add_column("Hostname", style="magenta")
        table.add_column("IP", style="green")
        table.add_column("OS", style="yellow")
        table.add_column("Last Seen", style="dim")
        console.print(table)
    else:
        print("[i] No agents connected yet.")

if __name__ == "__main__":
    main()
