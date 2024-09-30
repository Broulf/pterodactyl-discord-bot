# Discord Bot with API Integration

This Discord bot allows users to interact with an external server management API. It provides commands to list servers, start, stop, and fetch server information.

## Prerequisites

Before you begin, ensure you have the following:

1. [Python 3.8+](https://www.python.org/downloads/)
2. A [Discord Application & Bot Token](https://discord.com/developers/applications)
3. Your API URL and API Key for server management

## Installation

1. Clone this repository or download the script.
   
   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies:

   ```bash
   pip install requirements.txt
   ```

## Setup

1. Open the Python script (`ptero-discord-bot.py`).

2. Replace the following placeholders with your actual data:
   
   - `BOT_TOKEN`: Your Discord bot token.
   - `API_URL`: The base URL for your API (e.g., `https://example.com/api/client`).
   - `API_KEY`: Your API's authorization token.

3. Example:

   ```python
   TOKEN = 'BOT_TOKEN'
   API_URL = "https://example.com/api/client"
   HEADERS = {
       'Authorization': 'Bearer API_KEY',
       'Content-Type': 'application/json',
       'Accept': 'application/json'
   }
   ```

## Commands

### `/servers`
- **Description**: Fetch a list of all servers available to your API key.
- **Usage**: `/servers`
  
### `/start <server_id>`
- **Description**: Starts a server by its server ID.
- **Usage**: `/start <server_id>`

### `/stop <server_id>`
- **Description**: Stops a server by its server ID.
- **Usage**: `/stop <server_id>`

### `/info <server_id>`
- **Description**: Fetch information about a server.
- **Usage**: `/info <server_id>`

## Running the Bot

After setting up the bot, run the following command to start it:

```bash
python ptero-discord-bot.py
```

Once the bot is running, you should see the message:  
`<bot_name> has connected to Discord!`

## Notes

- Ensure your bot has the necessary permissions on the Discord server to read messages and send responses.
- Your API should support the requests made by the bot.

## License

This project is licensed under the MIT License.
```
