# Connect Claude Code → Comfy Cloud (official MCP)

Comfy Cloud ships an **official Claude Code plugin / MCP server**, so a *local* Claude Code can
drive it directly (build workflows, run them, pull outputs). Source:
https://docs.comfy.org/development/cloud/mcp-server

> **Must be LOCAL Claude Code**, not the cloud/web session. The web session can't do the browser
> sign-in or reach the endpoint. Run the Claude Code CLI on your own computer.

## Prerequisites
- A **Comfy Cloud account** — https://cloud.comfy.org
- **Claude Code CLI installed locally** (`npm i -g @anthropic-ai/claude-code`, then `claude`)

## Step 1 — Get this repo locally
So local Claude Code has the prompts, refs, Soul ID set, workflow, and docs:
```bash
git clone https://github.com/benweiner14-source/lonnieai.git
cd lonnieai
git checkout claude/repo-setup-biy7uf
claude                      # start Claude Code in the repo
```

## Step 2 — Add the Comfy Cloud MCP
**Option A — plugin (recommended):** inside Claude Code, run:
```
/plugin marketplace add Comfy-Org/comfy-skills
/plugin install comfy-cloud@comfy-skills
```
**Option B — direct MCP (no plugin):**
```bash
claude mcp add --transport http comfy-cloud https://cloud.comfy.org/mcp
```

## Step 3 — Authenticate
Run `/mcp` → select **comfy-cloud** → **Authenticate**. Your browser opens for sign-in; tokens
refresh automatically after that.

## Step 4 — Verify
Ask Claude Code to call `get_server_info` (and `get_billing_status`). If they return, you're wired.

## What the MCP can do (tools)
- **Discovery:** `search_templates`, `get_template`, `search_models`, `search_nodes`, `get_node`, `cql`
- **Generation:** `run_template`, `submit_workflow`, `partner_generate`, `upload_file`
- **Jobs:** `get_job_status`, `wait_for_job`, `get_output`, `cancel_job`
- **Workflows:** `list_saved_workflows`, `save_workflow`, `run_saved_workflow`
- Plugin slash-commands: `/comfy-cloud:generate-image`, `…:upscale-image`, `…:search-models`, etc.

## Step 5 — First run (what to tell local Claude Code)
Point it at the plan we already wrote:
> Read `docs/comfyui-handoff.md` and `docs/comfyui-workflow.md`. Using the comfy-cloud MCP:
> `search_models` for an SDXL checkpoint + an IP-Adapter FaceID (or InstantID) + a game/3D-render
> LoRA. Build a workflow that locks Zion's identity from `creators/zion-clark/refs/soul-id/`,
> pushes the CGI style with the LoRA + prompt, and holds his pose with ControlNet. `upload_file`
> the refs, `submit_workflow`, `wait_for_job`, `get_output`. Respect the hard constraints:
> authentic representation (born without legs — no fabricated legs), SFW, 9:16.

## Notes on your LoRA-tier concern
Use `search_models` to see which checkpoints/LoRAs Comfy Cloud exposes on your plan, and
`get_billing_status` for credits/tier. If a specific game-render LoRA isn't available, we can fall
back to a stylized checkpoint + strong prompt, or import one.

## If you'd rather I (this web session) drive it
I can't — this cloud session can't do the browser OAuth or reach cloud.comfy.org. Driving Comfy
Cloud has to happen from your local Claude Code (or another Claude with the MCP authenticated).
