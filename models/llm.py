from abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import getpass


'''
    LLM class to create and manage LLMs.
'''

#TODO: Add support for other LLM providers

class BaseLLM(ABC):
    """Abstract base class for LLM implementations."""
    
    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name
        self.config = kwargs
        self.client = self.create_llm()
    
    @abstractmethod
    def create_llm(self):
        """Create and return the LLM client."""
        pass
    
    def create_chat(self):
        """Return the chat client."""
        return self.client

class ChatOpenAILLM(BaseLLM):
    """ChatOpenAI implementation."""
    
    def __init__(self, model_name: str, api_key: str = None, **kwargs):
        self.api_key = api_key
        super().__init__(model_name, **kwargs)

    def create_llm(self):
        return ChatOpenAI(
            base_url=self.config['base_url'] if 'base_url' in self.config else "https://api.together.xyz/v1",
            model=self.model_name,
            api_key=self.api_key,
            **{k: v for k, v in self.config.items() if k != 'model'}
        )

class GoogleGenerativeAILLM(BaseLLM):
    """GoogleGenerativeAI implementation."""
    
    def __init__(self, model_name: str, api_key: str = None, **kwargs):
        self.api_key = api_key
        super().__init__(model_name, **kwargs)
    
    def create_llm(self):
        return ChatGoogleGenerativeAI(
            google_api_key=self.api_key,
            model=self.model_name,
            **{k: v for k, v in self.config.items() if k != 'model'}
        )


class LLMFactory:
    """Factory class to create different LLM implementations."""
    
    _implementations = {
        'chatopenai': ChatOpenAILLM,
        'google_genai': GoogleGenerativeAILLM,
    }
    
    @classmethod
    def create_llm(cls, provider: str, model_name: str, **kwargs) -> BaseLLM:
        """
        Create an LLM instance based on the provider.
        
        Args:
            provider (str): The LLM provider ('openai', 'openrouter', 'huggingface_pipeline', 'huggingface_endpoint')
            model_name (str): The model identifier
            **kwargs: Additional configuration parameters
            
        Returns:
            BaseLLM: An instance of the specified LLM implementation
            
        Raises:
            ValueError: If the provider is not supported
        """
        if provider not in cls._implementations:
            raise ValueError(f"Unsupported provider: {provider}. Available: {list(cls._implementations.keys())}")
        
        llm_class = cls._implementations[provider]
        return llm_class(model_name, **kwargs)
    
    @classmethod
    def register_implementation(cls, name: str, implementation_class):
        """Register a new LLM implementation."""
        cls._implementations[name] = implementation_class


# Convenience wrapper class that maintains your original interface
class LLM:
    """Wrapper class that provides a unified interface for different LLM providers."""
    
    def __init__(self, provider: str, model_name: str, **kwargs):
        """
        Initialize the LLM with a specific provider.
        
        Args:
            provider (str): The LLM provider ('openai', 'openrouter', 'huggingface_pipeline', 'huggingface_endpoint', 'mistralai', 'chatopenai')
            model_name (str): The model identifier
            **kwargs: Additional configuration parameters specific to the provider
        """
        self.provider = provider
        self.model_name = model_name
        
        self.llm = LLMFactory.create_llm(provider, model_name, **kwargs)
    
    def create_chat(self):
        """Return the chat client."""
        return self.llm.create_chat()
    
    def switch_provider(self, new_provider: str, **kwargs):
        """Switch to a different provider while keeping the same model name."""
        self.provider = new_provider
        self.llm = LLMFactory.create_llm(new_provider, self.model_name, **kwargs)