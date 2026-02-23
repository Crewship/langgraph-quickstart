# LangGraph Quickstart

A minimal LangGraph research graph. Clone, set your key, run.

## Run in 3 steps

### 1. Clone & install

```bash
git clone https://github.com/vhalasi/langgraph-quickstart.git
cd langgraph-quickstart
pip install -e .
```

### 2. Set your API key

```bash
cp .env.example .env   # add your OPENAI_API_KEY
```

> **Using a different provider?** Swap the `ChatOpenAI` import in `graph.py` and set the matching key — e.g. `ANTHROPIC_API_KEY` for Claude, `GROQ_API_KEY` for Groq (free tier).

### 3. Run

```bash
python main.py
```

---

## What's inside

A two-node graph powered by GPT-4o mini:

- **researcher** — finds 5 key points about a topic
- **reporter** — turns them into a short markdown report

Change the topic in `main.py`.

## Customise

- **Graph logic** → `graph.py`
- **Entry point** → `main.py`

## Learn more

- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain docs](https://python.langchain.com)
