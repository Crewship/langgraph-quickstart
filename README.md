# LangGraph Quickstart

A minimal LangGraph research graph. Clone, set your key, deploy — done.

## Deploy in 3 steps

### 1. Clone & install

```bash
git clone https://github.com/Crewship/langgraph-quickstart.git
cd langgraph-quickstart
pip install crewship
pip install -e .
```

### 2. Set your API key

```bash
crewship env set OPENAI_API_KEY=sk-...
```

> **Using a different provider?** Swap the `ChatOpenAI` import in `graph.py` and set the matching key — e.g. `ANTHROPIC_API_KEY` for Claude, `GROQ_API_KEY` for Groq (free tier).

### 3. Deploy

```bash
crewship deploy
```

That's it. Your research graph is live.

## Run locally (optional)

```bash
cp .env.example .env   # add your OPENAI_API_KEY
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
