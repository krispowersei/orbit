#!/usr/bin/env python3
"""Call one Orbit (Reco) MCP tool from a plain shell, no Claude/Codex needed.
Runs on the Mac where Orbit.app is installed and open.
Usage: orbit_mcp.py list | orbit_mcp.py <tool> '<json args>'
"""
import glob, json, subprocess, sys
cands = glob.glob("/Applications/Orbit.app/Contents/MacOS/*") + glob.glob("/Applications/Reco.app/Contents/MacOS/*")
if not cands: sys.exit("Orbit.app not found in /Applications; install the DMG from github.com/diip3sh/orbit/releases")
p = subprocess.Popen([cands[0], "--mcp"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
def rpc(i, method, params=None):
    msg = {"jsonrpc": "2.0", "method": method}
    if i is not None: msg["id"] = i
    if params is not None: msg["params"] = params
    p.stdin.write(json.dumps(msg) + "\n"); p.stdin.flush()
    if i is None: return None
    while True:
        line = p.stdout.readline()
        if not line: sys.exit("Orbit MCP closed; is Orbit running?")
        r = json.loads(line)
        if r.get("id") == i: return r
rpc(1, "initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "grokbot", "version": "1"}})
rpc(None, "notifications/initialized")
if sys.argv[1] == "list": out = rpc(2, "tools/list")
else: out = rpc(2, "tools/call", {"name": sys.argv[1], "arguments": json.loads(sys.argv[2] if len(sys.argv) > 2 else "{}")})
print(json.dumps(out.get("result", out), indent=2)); p.terminate()
