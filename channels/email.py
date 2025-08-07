"""Email channel implementation."""

from .base import MessageChannel


class EmailChannel(MessageChannel):
    """Placeholder for email messaging."""

    def send(self, recipient: str, message: str) -> None:
        print(f"[Email] Sending to {recipient}: {message}")

    def receive(self):
        print("[Email] Retrieving messages")
        return []
