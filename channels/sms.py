"""SMS channel implementation."""

from .base import MessageChannel


class SMSChannel(MessageChannel):
    """Placeholder for SMS messaging."""

    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS] Sending to {recipient}: {message}")

    def receive(self):
        print("[SMS] Retrieving messages")
        return []
