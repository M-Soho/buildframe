"""Command-line interface for sending and receiving messages."""

import argparse
from typing import Dict

from channels.base import MessageChannel


def run(channels: Dict[str, MessageChannel]) -> None:
    """Run the CLI to interact with the messaging channels."""
    parser = argparse.ArgumentParser(description="Messaging CLI")
    parser.add_argument("channel", choices=channels.keys(), help="Channel to use")
    parser.add_argument("action", choices=["send", "receive"], help="Action to perform")
    parser.add_argument("recipient", nargs="?", help="Recipient identifier for sending")
    parser.add_argument("message", nargs="?", help="Message content for sending")

    args = parser.parse_args()
    channel = channels[args.channel]

    if args.action == "send":
        if not args.recipient or not args.message:
            parser.error("send action requires recipient and message")
        channel.send(args.recipient, args.message)
    else:
        messages = channel.receive()
        print(messages)
