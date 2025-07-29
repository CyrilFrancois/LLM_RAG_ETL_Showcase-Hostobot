import os

from chains.hospital_cypher_chain import hospital_cypher_chain
from chains.hospital_review_chain import reviews_vector_chain
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from tools.wait_times import (
    get_current_wait_times,
    get_most_available_hospital,
)

HOSPITAL_AGENT_MODEL = os.getenv("HOSPITAL_AGENT_MODEL")

hospital_agent_prompt = hub.pull("hwchase17/openai-functions-agent")

tools = [
    Tool(
        name="Experiences",
        func=reviews_vector_chain.invoke,
        description="""
        Use this tool when addressing questions about patient experiences, emotions, or other qualitative aspects that can be answered through semantic search.
        It is not appropriate for objective questions involving counts, percentages, aggregations, or factual listings.
        Always provide the entire prompt as the input: for example, if the question is "Are patients satisfied with their care?", then the input should be exactly: "Are patients satisfied with their care?"
        """,
    ),
    Tool(
        name="Graph",
        func=hospital_cypher_chain.invoke,
        description="""
        Best suited for answering questions related to patients, physicians, hospitals, insurance payers, patient review metrics, and hospital visit details.
        Always provide the full prompt as input : for example, if the question is "How many visits have there been?", then the input should be exactly: "How many visits have there been?
        """,
    ),
    Tool(
        name="Waits",
        func=get_current_wait_times,
        description="""
        Use this tool for questions about the current wait time at a specific hospital.
        It only provides real-time wait times and does not support historical or aggregated data.
        Do not include the word “hospital” in the input—only pass the hospital's name.
        For example, if the question is "What is the current wait time at Jordan Inc Hospital?", the input should be: "Jordan Inc".
        """,
    ),
    Tool(
        name="Availability",
        func=get_most_available_hospital,
        description="""
        Use this tool to identify the hospital with the shortest current wait time.
        It does not provide historical or aggregated wait time data.
        The tool returns a dictionary where each key is a hospital name and the value is its current wait time in minutes.
        """,
    ),
]

chat_model = ChatOpenAI(
    model=HOSPITAL_AGENT_MODEL,
    temperature=0,
)

hospital_rag_agent = create_openai_functions_agent(
    llm=chat_model,
    prompt=hospital_agent_prompt,
    tools=tools,
)

hospital_rag_agent_executor = AgentExecutor(
    agent=hospital_rag_agent,
    tools=tools,
    return_intermediate_steps=True,
    verbose=True,
)
