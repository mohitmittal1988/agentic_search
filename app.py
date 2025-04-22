#import libraries
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv




# Arxiv and Wikipedia tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)

arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper, name="Arxiv")
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper, name="Wikipedia")
search = DuckDuckGoSearchRun(name="Search")


tools=[search,arxiv,wiki]

st.title("🔎Agentic Search Assistant🔎")

"""
Ask anything, and let this intelligent agent fetch answers from the web, Wikipedia, and Arxiv in real-time using LLM-powered reasoning.
Built with LangChain + Groq, this app uses tools to think before it responds.
"""

##side bar for settings

st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
# Store the API key once entered
if api_key and "api_entered" not in st.session_state:
    st.session_state.api_entered = True

if prompt := st.chat_input(placeholder="What is machine learning?"):
    if not api_key or not st.session_state.get("api_entered", False):
        st.info("Please add your Groq API key to continue.")
        st.stop()

    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Initialize LLM and tools
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
    search_agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True,
    agent_kwargs={"max_iterations": 3}
    )


    # Get assistant reply
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(prompt, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
