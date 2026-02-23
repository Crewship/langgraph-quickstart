from typing import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    topic: str
    research: str
    report: str


llm = ChatOpenAI(model="gpt-4o-mini")


def research_node(state: State) -> dict:
    response = llm.invoke(
        f"Research this topic and give me 5 key bullet points: {state['topic']}"
    )
    return {"research": response.content}


def report_node(state: State) -> dict:
    response = llm.invoke(
        f"Write a short markdown report based on this research:\n{state['research']}"
    )
    return {"report": response.content}


graph = (
    StateGraph(State)
    .add_node("researcher", research_node)
    .add_node("reporter", report_node)
    .add_edge(START, "researcher")
    .add_edge("researcher", "reporter")
    .add_edge("reporter", END)
    .compile()
)
