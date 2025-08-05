"""Base classes and interfaces for communication channels."""

from abc import ABC, abstractmethod
from typing import Any, Dict


class MessageChannel(ABC):
    """Abstract base class defining a communication channel."""

    def __init__(self, config: Dict[str, Any]) -> None:
        """Store channel-specific configuration.

        Args:
            config: A dictionary of configuration values for the channel.
        """
        self.config = config

    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        """Send a message to the provided recipient."""

    @abstractmethod
    def receive(self) -> Any:
        """Retrieve pending messages for the channel."""
