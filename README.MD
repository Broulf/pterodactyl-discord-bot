# Pterodactyl Discord Bot

This Discord bot allows users to interact with an external server management API. It provides commands to list servers, start, stop, and fetch server information.

## Prerequisites

Before you begin, ensure you have the following:

1. [Python 3.8+](https://www.python.org/downloads/)
2. A [Discord Application & Bot Token](https://discord.com/developers/applications)
3. Your API URL and API Key for server management

## Installation

1. Clone this repository or download the script.
   
   ```bash
   git clone https://github.com/Broulf/pterodactyl-discord-bot.git
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

## Running the Bot

After setting up the bot, run the following command to start it:

```bash
python ptero-discord-bot.py
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

Once the bot is running, you should see the message:  
`<bot_name> has connected to Discord!`

## Pterodactyl Egg Installation

If you are installing the bot via a Pterodactyl Egg, follow the instructions below:

1. **Egg Configuration:**
   - **Git Repo Address**: Do not change this.
   - **Git Branch**: Do not change this.
   - **Auto Update**: Set this as per your preference:
     - `0` = false (default)
     - `1` = true
   - **App py file**: Do not change this.
   - **Requirements file**: Do not change this.

2. **Port Allocation**: Assign any available port.

3. **Resource Limits**:
   - **CPU Limit**: 100%
   - **Memory**: 512MB
   - **Disk Space**: 512MB

4. **Important Note**: After installing the egg, the application will crash three times during the initial installation. This is normal. After the crashes:
   - Go to the `Files` tab in the Pterodactyl panel.
   - Locate and edit the `pterodactyl-discord-bot.py` file.
   - Replace the placeholder values (such as `BOT_TOKEN`, `API_URL`, and `API_KEY`) with your actual values.

## Notes

- Ensure your bot has the necessary permissions on the Discord server to read messages and send responses.
- Your API should support the requests made by the bot. This API key should be a personal one from the user settings and NOT an application key.

## License

This project is licensed under the MIT License.
