"""WhatsApp channel implementation."""

from .base import MessageChannel


class WhatsAppChannel(MessageChannel):
    """Placeholder implementation for WhatsApp messaging."""

    def send(self, recipient: str, message: str) -> None:
        print(f"[WhatsApp] Sending to {recipient}: {message}")

    def receive(self):
        print("[WhatsApp] Retrieving messages")
        return []
