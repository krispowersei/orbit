# Grok Bot adaptations (branch `grokbot`)
Upstream code untouched. Changes:
- `SKILL.md` (new): Grok Bot skill; maps to Shell/CopyFromBox/CopyToBox/Read with the Mac's machineId.
- `SKILL.upstream.md`: moved from `docs/skills/product-walkthrough/SKILL.md` (the recording method; unchanged).
- `grokbot/orbit_mcp.py`: stdlib MCP stdio client so the app's MCP server (`<Orbit.app binary> --mcp`, Unix socket in Application Support) is callable from plain shell. Replaces Orbit's "Agents" settings pane, which writes Claude Code/Codex/Cursor/Gemini MCP configs (`AgentKind.swift`, `AgentTOMLConfig.swift`) — not needed for Grok Bot.
- `.claude/skills`, `.qwen/skills`, `.agents/skills` (apple-design) are dev-time design skills for contributors; left as-is, unused.
## Not adaptable
Orbit is Swift + ScreenCaptureKit/AVFoundation/SwiftUI/WKWebView (macOS 15.2+, Apple silicon). No Linux build is possible; it must run on Kris's Mac.
