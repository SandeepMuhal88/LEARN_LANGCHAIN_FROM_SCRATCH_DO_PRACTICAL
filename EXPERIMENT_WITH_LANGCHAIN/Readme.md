Below is a **professional, clean, production-ready `README.md`** file for your **LangChain Full Module Cheat Sheet**.
You can directly copy–paste this into your GitHub repo.

---

# 📚 LangChain Full Module Cheat Sheet (v1.x)

A complete, developer-focused reference of all key modules in the **LangChain v1.x ecosystem** — including model imports, prompts, chains, memory, RAG components, tools, and modern LCEL pipeline structure.

---

## 🚀 Overview

LangChain v1.x introduced a **modular architecture**:

| Module                       | Purpose                              |
| ---------------------------- | ------------------------------------ |
| **langchain-core**           | Prompts, LCEL, messages, parsers     |
| **langchain**                | Convenience wrapper (legacy)         |
| **langchain-openai**         | OpenAI LLMs + Embeddings             |
| **langchain-community**      | Loaders, vectorstores, tools, memory |
| **langchain-text-splitters** | Advanced text chunking               |
| **langchainhub**             | Prebuilt prompts                     |
| **langchain-experimental**   | Experimental agents                  |
| **langgraph**                | StateGraph-based agent system        |

This README organizes everything into a quick reference you can use for real development.

---

# 🔥 1. langchain-core (Main Framework)

### **Imports**

```python
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.runnables import (
    RunnableSequence, RunnableMap, RunnablePassthrough
)
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
```

### **Contains**

* Prompt Templates
* LCEL (LangChain Expression Language)
* Message structures
* Output Parsers
* Runnable Pipelines

---

# 🔥 2. langchain (Legacy Convenience Layer)

```python
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI   # old style
```

> ⚠ Recommended for backwards compatibility only.

---

# 🔥 3. langchain-openai (Official OpenAI SDK for LangChain)

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
```

---

# 🔥 4. langchain-community (Integrations Package)

### **Document Loaders**

```python
from langchain_community.document_loaders import (
    PyPDFLoader, TextLoader, WebBaseLoader, DirectoryLoader
)
```

### **Vector Stores**

```python
from langchain_community.vectorstores import FAISS, Chroma
```

### **Embeddings**

```python
from langchain_community.embeddings import HuggingFaceEmbeddings
```

### **Memory**

```python
from langchain_community.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory,
)
```

### **Tools**

```python
from langchain_community.tools import DuckDuckGoSearchRun
```

---

# 🔥 5. langchain-text-splitters

```python
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    TokenTextSplitter,
    SentenceTextSplitter
)
```

---

# 🔥 6. langchainhub

```python
from langchainhub import hub
prompt = hub.pull("langchain-ai/generic-template")
```

---

# 🔥 7. langchain-experimental

```python
from langchain_experimental.agents import create_pandas_dataframe_agent
```

---

# 🔥 8. langgraph (Agent Graph System)

```python
from langgraph import StateGraph, END
```

---

# 📌 Full RAG Pipeline — Modern LCEL Implementation

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnableSequence, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load and split
loader = PyPDFLoader("data.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embeddings + vectorstore
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(chunks, embeddings)

# Retriever
retriever = db.as_retriever()

# Prompt
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="Context:\n{context}\n\nQuestion: {question}\nAnswer:",
)

# LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# RAG Pipeline (LCEL)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```

---

# 📝 Notes

* Always install **matching versions**:

```bash
pip install "langchain>=1.0,<2.0" langchain-openai langchain-community langchain-text-splitters
```

* Older tutorials (2023–2024) will not work without modification.
* Use `langchain-core` + LCEL for all new projects.

---



