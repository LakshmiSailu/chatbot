
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDERS = {
    "nvidia": {
        "base_url": "https://integrate.api.nvidia.com/v1",
        "key_env": "NVIDIA_API_KEY",
        "fast": "deepseek-ai/deepseek-v4.1-flash",
        "strong": "nvidia/nemotron-3-super-120b-a12b",
    },
    "openrouter": {
        "base_url": "https://openrouter.ai/api/v1",
    	"key_env": "OPENROUTER_API_KEY",
   	"fast": "nvidia/nemotron-3.5-lightning:free",
	"strong": "nvidia/nemotron-3-ultra-550b-a55b:free",
    },
    "claude": {
        "base_url": "https://api.anthropic.com/v1/",
        "key_env": "ANTHROPIC_API_KEY",
        "fast": "claude-haiku-5-5",
        "strong": "claude-sonnet-5-5",
    },
    "ollama": {
        "base_url": "http://localhost:11434/v1",
        "key_env": None,
        "fast": "qwen3:8b",
        "strong": "qwen3:8b",
    },
}

PROVIDER = os.environ.get("LLM_PROVIDER", "openrouter")
_cfg = PROVIDERS[PROVIDER]

api_key = (
    os.environ.get(_cfg["key_env"])
    if _cfg["key_env"]
    else "not-needed"
)

if not api_key:
    raise ValueError(
        f"Missing API key: {_cfg['key_env']}. Check your .env file."
    )

client = OpenAI(
    base_url=_cfg["base_url"],
    api_key=api_key,
)

MODEL = _cfg["fast"]
STRONG_MODEL = _cfg["strong"]

