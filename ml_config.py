"""
Configuration for CommandPro ML (AI-powered error analysis)

Customize the behavior of the ML-based error processor here.
"""

# Ollama Configuration
OLLAMA_CONFIG = {
    "base_url": "http://localhost:11434",  # Default Ollama endpoint
    "model": "mistral",                     # Model to use (mistral, neural-chat, etc.)
    "timeout": 10,                          # Timeout for LLM response (seconds)
    "temperature": 0.7,                     # Creativity level (0.0-1.0)
    "num_ctx": 2048,                        # Context window size
}

# Feature Flags
FEATURES = {
    "use_ml": True,                         # Enable ML processing
    "use_fallback": True,                   # Fall back to rule-based if ML fails
    "stream_responses": True,               # Stream suggestions in real-time
    "show_thinking": False,                 # Show LLM thinking process
    "cache_results": True,                  # Cache similar error analyses
}

# Prompt Engineering
PROMPT_SETTINGS = {
    "system_prompt": """You are CommandPro, an expert command-line error fixer.
Your job is to analyze error messages and provide helpful, actionable fixes.
Be concise, practical, and focus on the most likely solution.
Provide commands the user can copy and run immediately.""",
    
    "error_prefix": "Error: ",
    "suggestion_prefix": "Fix: ",
    "max_suggestions": 3,
    "include_explanation": True,
    "include_examples": True,
}

# Real-time Processing
STREAM_CONFIG = {
    "buffer_size": 1024,                    # stderr buffer size in bytes
    "chunk_timeout": 0.5,                   # Time to wait before sending to LLM (seconds)
    "min_chunk_size": 50,                   # Minimum characters before processing
    "display_delay": 0.1,                   # Delay between printing characters (for effect)
}

# Fallback Behavior
FALLBACK_CONFIG = {
    "use_rule_based": True,                 # Use CommandPro patterns when ML unavailable
    "ollama_required": False,               # Require Ollama to be running
    "timeout_retry": 2,                     # Retry count if LLM times out
}

# Cache Settings
CACHE_CONFIG = {
    "enabled": True,
    "max_cache_size": 100,                  # Max errors to cache
    "cache_file": ".cmdpro_cache",
    "ttl": 3600,                            # Cache TTL in seconds (1 hour)
}

# Display Settings
DISPLAY_CONFIG = {
    "use_colors": True,
    "verbose": False,
    "show_confidence": True,                # Show confidence score for ML suggestions
    "max_output_lines": 50,                 # Max lines to display
}

# Debug Settings
DEBUG = {
    "verbose_logging": False,
    "log_file": None,                       # Set to file path to enable logging
    "save_queries": False,                  # Save all prompts/responses
    "benchmark": False,                     # Measure performance
}
