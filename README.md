# Messaging Integration Scaffold

This project provides a modular Python scaffold for integrating multiple
communication channels such as WhatsApp, Facebook Marketplace, SMS, and
email. Each channel implements a shared interface so new channels can be
added with minimal effort.

## Structure

```
.
├── channels            # Channel implementations
├── cli.py              # Command-line interface
├── config.yaml         # Configuration for API keys and settings
├── main.py             # Application entry point
├── requirements.txt    # Python dependencies
└── utils               # Helper utilities (configuration loader)
```

## Setup

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update `config.yaml` with your API keys and settings.

## Usage

Run the CLI via the entry point:

```bash
python main.py whatsapp send +123456 "Hello world"
```

This example sends a WhatsApp message. Replace the channel and action as
needed; `receive` will fetch messages for the chosen channel.

## Extending

To add a new channel:

1. Create a new module in `channels/` inheriting from `MessageChannel`.
2. Register the channel in `CHANNEL_MAP` inside `main.py`.
3. Add configuration details to `config.yaml`.

## License

Distributed under the MIT License.
