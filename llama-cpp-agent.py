import requests

def get_ai_news():
    url = "https://newsapi.org/v2/everything"
    params = {"q": "Artificial Intelligence", "sortBy": "publishedAt", "pageSize": 5, "apiKey": "YOUR_NEWS_API_KEY"}
    resp = requests.get(url, params=params).json()
    return [f"{a['title']} — {a['source']['name']}" for a in resp.get("articles", [])]


from llama_cpp import Llama
from llama_cpp_agent import LlamaCppAgent, LlamaCppFunctionTool, MessagesFormatterType

# Load a local LLaMA model (replace path with your GGUF file)
llm = Llama("path/to/llama-13B.Q4_K.gguf", n_threads=8)

agent = LlamaCppAgent(
    llm, 
    system_prompt="You are an AI agent that fetches headlines via a tool and summarizes them.",
    predefined_messages_formatter_type=MessagesFormatterType.CHATML
)

# Register our news tool
tool = LlamaCppFunctionTool(
    func=get_ai_news,
    name="get_ai_news",
    description="Returns a list of top 5 AI news headlines"
)
agent.register_tool(tool)

response = agent.get_chat_response(
    "Please fetch the top AI news and give me a brief summary in bullet points."
)

print("Agent response:\n", response.strip())
