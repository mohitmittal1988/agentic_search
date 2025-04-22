# 🔎 Agentic Search Assistant with LangChain, Groq & Streamlit

This project showcases a LangChain-powered **agentic search assistant** that uses Groq's Llama3 LLM to answer natural language questions by reasoning and dynamically querying the internet through:
- 🌍 Web Search (via DuckDuckGo)
- 📚 Wikipedia
- 📄 Arxiv (research articles)

The agent **decides** which tool to use, how many queries to make, and synthesizes an answer — just like a digital research assistant!

---

## 🚀 Features

- 🧠 **Autonomous Agentic Reasoning** with tool selection via LangChain
- 🔍 **Web-Augmented Search** with DuckDuckGo, Wikipedia, and Arxiv APIs
- ⚡ **Real-time Streaming Responses** powered by Groq's blazing-fast `Llama3-8b-8192`
- 🤖 **Interactive Chat UI** using Streamlit for seamless Q&A
- 🔐 **Secure API Key Entry** with state tracking
- 🧩 **Tool Execution Cap Control** via `max_iterations` to prevent infinite loops
- 🪄 **Verbose Output for Debugging Agent Thought Process**

---

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq](https://console.groq.com/)
- [DuckDuckGo](https://duckduckgo.com/)
- [Wikipedia API](https://en.wikipedia.org/w/api.php)
- [Arxiv API](https://arxiv.org/help/api/)
- Python 3.10+

---

## 📦 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mohitmittal1988/langchain-agentic-search.git
cd langchain-agentic-search
