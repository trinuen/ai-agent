# 🤖 Gemini AI Coding Agent

A command-line AI agent powered by **Gemini 2.5 Flash** that can autonomously read, write, run, and inspect files in a working directory. Describe a task in plain English — the agent plans the steps, calls the right tools, and gets it done without manual intervention.

---

## ✨ Features

- 📂 **List files** — explore directory structure and understand project layout
- 📖 **Read files** — inspect file contents before making any changes
- ✏️ **Write files** — create or overwrite files with complete, correct content
- 🚀 **Run Python files** — execute scripts and verify results in real time
- 🔁 **Agentic loop** — automatically chains tool calls until the task is complete
- 🧠 **Gemini 2.5 Flash** — fast, capable model with native function calling

---

## 🛠 Installation

**Prerequisites:** Python 3.13+

### Option A — with `uv` (recommended)

[`uv`](https://github.com/astral-sh/uv) is a fast Python package manager that reads `pyproject.toml` directly.

```bash
# 1. Install uv (if you haven't already)
curl -Lsf https://astral.sh/uv/install.sh | sh

# 2. Clone the repo
git clone https://github.com/your-username/ai-agent.git
cd ai-agent

# 3. Install dependencies and create a virtual environment
uv sync
```

### Option B — with `pip`

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ai-agent.git
cd ai-agent

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Additional settings can be adjusted in `config.py`:

| Variable | Default | Description |
|---|---|---|
| `MAX_ITERS` | `20` | Maximum number of agentic iterations before the agent stops |
| `MAX_CHARS` | `10000` | Maximum characters read from a file in a single operation |

---

## 🚀 Usage

```bash
# With uv
uv run main.py "<your task>" [--verbose] [--workdir <path>]

# With pip / activated venv
python main.py "<your task>" [--verbose] [--workdir <path>]
```

### Arguments

| Argument | Description |
|---|---|
| `user_prompt` | The task you want the agent to perform *(required)* |
| `--verbose` | Print token counts, function calls, and tool responses |
| `--workdir` | Working directory the agent operates in *(default: `.`)* |

### Examples

**Fix a bug:**
```bash
uv run main.py "Fix the off-by-one error in utils.py"
```

**Add a new feature:**
```bash
uv run main.py "Add input validation to the login function in auth.py" --verbose
```

**Work in a specific project folder:**
```bash
uv run main.py "Refactor the database module to use context managers" --workdir ./my_project
```

**Explore and summarize a codebase:**
```bash
uv run main.py "List all files and summarize what this project does"
```

**Verbose output** shows the agent's internal tool calls and token usage as it works:
```
User prompt: Fix the off-by-one error in utils.py

 - Calling function: get_files_info
 - Calling function: get_file_content
 - Calling function: write_file
Prompt tokens: 1024
Response tokens: 312

Final response:
I found and fixed the off-by-one error on line 42 of utils.py ...
```

---

## 📁 Project Structure

```
ai-agent/
├── main.py              # Entry point — argument parsing and agentic loop
├── prompts.py           # System prompt defining agent behaviour
├── call_function.py     # Tool dispatcher and function registry
├── config.py            # Configuration (MAX_ITERS, MAX_CHARS)
├── pyproject.toml       # Project metadata and dependencies
├── functions/
│   ├── get_files_info.py    # List files in a directory
│   ├── get_file_content.py  # Read file contents
│   ├── write_file.py        # Write or overwrite a file
│   └── run_python_file.py   # Execute a Python script
└── .env                 # API key — never commit this file
```