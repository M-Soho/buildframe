"""Application entry point."""

from channels.facebook_marketplace import FacebookMarketplaceChannel
from channels.whatsapp import WhatsAppChannel
from channels.sms import SMSChannel
from channels.email import EmailChannel
from cli import run
from utils.config import load_config

CHANNEL_MAP = {
    "whatsapp": WhatsAppChannel,
    "facebook_marketplace": FacebookMarketplaceChannel,
    "sms": SMSChannel,
    "email": EmailChannel,
}


def build_channels(config):
    """Instantiate channel objects based on configuration."""
    channels = {}
    for name, conf in config.get("channels", {}).items():
        cls = CHANNEL_MAP.get(name)
        if cls:
            channels[name] = cls(conf)
    return channels


def main() -> None:
    """Load configuration and start the CLI."""
    config = load_config()
    channels = build_channels(config)
    run(channels)


if __name__ == "__main__":
    main()
