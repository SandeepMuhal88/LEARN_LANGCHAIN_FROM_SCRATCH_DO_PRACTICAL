### Open Source HuggingFace Model

1. Serverless API (Easiest)
```
from langchain_huggingface
import HuggingFaceEndpoint
``` 
Runs on Hugging Face servers (Free tier available). No powerful GPU needed locally.
2. Local Execution (Private)
```
from langchain_huggingface 
import HuggingFacePipeline
```
Downloads the model and runs it on your machine (RAM/GPU heavy).

3. Chat Models
```
from langchain_huggingface 
import ChatHuggingFace
```