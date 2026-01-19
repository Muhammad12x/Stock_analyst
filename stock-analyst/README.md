# Stock Analyst Phase 0

Local-first Python MVP to extract structured stock profiles from a single markdown report and build a stocks list output.

## Setup (macOS)

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Ollama and pull a model:
   ```bash
   brew install ollama
   ollama pull llama3.1
   ```
4. Add your report at `data/reports/SHOP.md`.
5. Run the CLI:
   ```bash
   python -m app.cli build SHOP
   ```

## Outputs

The CLI writes the following files:

- `data/outputs/profiles/SHOP.profile.json`
- `data/outputs/stocks_list.json`
- `data/outputs/stocks_list.csv`
- `data/logs/events.jsonl`

## Configuration

You can override defaults using environment variables:

- `OLLAMA_URL` (default: `http://localhost:11434/api/generate`)
- `OLLAMA_MODEL` (default: `llama3.1`)
