#!/usr/bin/env python
from dotenv import load_dotenv

load_dotenv()

from graph import graph  # noqa: E402


def run():
    result = graph.invoke({"topic": "AI agents in production"})
    print(result["report"])


if __name__ == "__main__":
    run()
