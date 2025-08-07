"""Facebook Marketplace channel implementation."""

from .base import MessageChannel


class FacebookMarketplaceChannel(MessageChannel):
    """Placeholder for Facebook Marketplace messaging."""

    def send(self, recipient: str, message: str) -> None:
        print(f"[Facebook Marketplace] Sending to {recipient}: {message}")

    def receive(self):
        print("[Facebook Marketplace] Retrieving messages")
        return []
