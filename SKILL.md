---
name: orbit
description: Make polished screen-recorded product demos with Orbit (macOS Screen Studio alternative): auto zooms, smooth cursor, styled backgrounds, and scripted web-page recordings via its MCP tools. Use for Kris's demo/walkthrough videos. Runs on Kris's Mac (MacBook-Pro.local), not the Linux box.
---
# Orbit for Grok Bot
Orbit is a native Swift/ScreenCaptureKit app: macOS 15.2+, Apple silicon only. It cannot run on the Linux box. Grok Bot drives it on Kris's Mac via `Shell` with `machineId` (ListMachines → MacBook-Pro.local).

## One-time setup (needs Kris's OK — installs an app on his Mac)
1. Download latest DMG (`gh release download -R diip3sh/orbit -p '*.dmg'`), copy Orbit.app to /Applications, `xattr -dr com.apple.quarantine /Applications/Orbit.app && open /Applications/Orbit.app`.
2. Kris grants Screen Recording in System Settings (one click, his own), then relaunch.
3. Copy `grokbot/orbit_mcp.py` to the Mac (CopyFromBox) e.g. `~/grokbot/orbit_mcp.py`.

## A. Scripted web recording (public or logged-in web pages, e.g. Trello web)
Tools over MCP (`python3 orbit_mcp.py <tool> '<json>'`):
- `inspect_page {url, selectors}` → element boxes/selectors. Also `open_page`, `look`, `read_page`, `click`, `hover`, `type`.
- `record_page {url, viewport, scale, steps:[{action:hover|click|type|scroll, selector, show, start, duration, text}]}` → render_id/movie.
- `render_status {render_id}` → movie path when done.
- `export_recording {movie, format:hevc|gif|prores…, resolution, frame_rate}` → MP4/MOV path.
- `edit_motion`, `preview_motion`, `capture_ui` for motion-design films (see Reco/AgentRecording/Skills/reco-*.md).
Method: SKILL.upstream.md (research → 4–6 beat shot list → every step has a `show` → re-record at most once on warnings).

## B. Real-app recording (Discord desktop etc.)
Record with Orbit's recorder via URL scheme on the Mac: `open 'reco://toggle'` start/stop, `reco://pause`, `reco://cancel`, `reco://edit-last` opens the editor (auto zooms on clicks/typing, smooth cursor, background). Drive the app between toggles (Kris or computer actions on the Mac). Export from the editor or `export_recording`.

## Outputs
Orbit saves to its Library; `CopyToBox` the exported file to `/workspace/demo-studio/<name>.mp4`, then check with `ffprobe` and an `ffmpeg -ss 3 -frames:v 1` frame + `Read`. Narration (optional) is added on the box with edge-tts + ffmpeg (see product-walkthrough-video-skill fork).
