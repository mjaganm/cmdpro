"""
Ollama integration module for CommandPro ML

Handles communication with local Ollama instances for AI-powered error analysis.
"""

import json
import requests
import subprocess
from typing import Generator, Optional, Dict, Any
from ml_config import OLLAMA_CONFIG, FEATURES, PROMPT_SETTINGS


class OllamaClient:
    """Client for interacting with Ollama local LLM"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize Ollama client with configuration"""
        self.config = config or OLLAMA_CONFIG
        self.base_url = self.config.get("base_url", "http://localhost:11434")
        self.model = self.config.get("model", "mistral")
        self.timeout = self.config.get("timeout", 10)
        self.temperature = self.config.get("temperature", 0.7)
        self._check_ollama_available()
    
    def _check_ollama_available(self) -> bool:
        """Check if Ollama is available and running"""
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=2
            )
            return response.status_code == 200
        except Exception:
            return False
    
    def is_available(self) -> bool:
        """Check if Ollama service is available"""
        try:
            requests.get(f"{self.base_url}/api/tags", timeout=2)
            return True
        except Exception:
            return False
    
    def list_models(self) -> list:
        """List available models in Ollama"""
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                models = data.get("models", [])
                return [m["name"] for m in models]
            return []
        except Exception:
            return []
    
    def analyze_error(self, error_message: str, context: str = "") -> Optional[str]:
        """
        Analyze an error message using Ollama and return suggestions.
        
        Args:
            error_message: The stderr output to analyze
            context: Optional context (command that was run)
            
        Returns:
            Suggested fix from LLM
        """
        if not self.is_available():
            return None
        
        # Build prompt
        system_prompt = PROMPT_SETTINGS.get("system_prompt", "")
        user_prompt = self._build_prompt(error_message, context)
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": user_prompt,
                    "system": system_prompt,
                    "stream": False,
                    "temperature": self.temperature,
                    "num_ctx": self.config.get("num_ctx", 2048),
                },
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get("response", "").strip()
            return None
        except requests.Timeout:
            return None
        except Exception as e:
            if FEATURES.get("verbose"):
                print(f"Error calling Ollama: {e}")
            return None
    
    def analyze_error_stream(
        self, 
        error_message: str, 
        context: str = ""
    ) -> Generator[str, None, None]:
        """
        Analyze error and stream responses back (real-time suggestions).
        
        Args:
            error_message: The stderr to analyze
            context: Optional command context
            
        Yields:
            Chunks of the LLM response
        """
        if not self.is_available():
            return
        
        system_prompt = PROMPT_SETTINGS.get("system_prompt", "")
        user_prompt = self._build_prompt(error_message, context)
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": user_prompt,
                    "system": system_prompt,
                    "stream": True,
                    "temperature": self.temperature,
                    "num_ctx": self.config.get("num_ctx", 2048),
                },
                timeout=self.timeout,
                stream=True
            )
            
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line)
                        chunk = data.get("response", "")
                        if chunk:
                            yield chunk
        except Exception:
            pass
    
    def _build_prompt(self, error_message: str, context: str = "") -> str:
        """Build a well-structured prompt for error analysis"""
        prompt = f"""Analyze this command-line error and provide a fix:

Error Output:
```
{error_message}
```"""
        
        if context:
            prompt += f"\n\nCommand Context: {context}"
        
        prompt += f"""

Provide a brief, actionable fix that the user can execute immediately.
Focus on the most likely solution. Be concise."""
        
        return prompt
    
    def pull_model(self, model_name: str) -> bool:
        """Download/pull a model from Ollama"""
        try:
            response = requests.post(
                f"{self.base_url}/api/pull",
                json={"name": model_name},
                timeout=300  # Long timeout for download
            )
            return response.status_code == 200
        except Exception:
            return False


class OllamaManager:
    """Manages Ollama lifecycle and operations"""
    
    @staticmethod
    def is_running() -> bool:
        """Check if Ollama is running"""
        client = OllamaClient()
        return client.is_available()
    
    @staticmethod
    def ensure_model(model_name: str) -> bool:
        """Ensure a specific model is available, download if needed"""
        client = OllamaClient()
        available_models = client.list_models()
        
        if model_name in available_models:
            return True
        
        print(f"Model '{model_name}' not found. Downloading...")
        return client.pull_model(model_name)
    
    @staticmethod
    def get_client() -> OllamaClient:
        """Get a configured Ollama client"""
        return OllamaClient()
