import discord
from discord.ext import commands
import requests

# Replace with your Discord bot token
TOKEN = 'MTI4OTIzNDMyOTI2MzgwMDM4Mw.G-M2L-.s72D6CeH-AX3noosfDKUGCv2UQUEHvuxwPn8TQ'

# Replace with your API URL
API_URL = "https://ptero.pondfolk.org/api/client"

# Default Headers for all commands
HEADERS = {
            'Authorization': 'Bearer ptlc_1Ke0uY0kHAgfWPL83kK5fotJlWgbRjqymbaAyRUCoul',  # Replace with your actual Client API Key
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

# Create an instance of Intents with the message content intent enabled
intents = discord.Intents.default()
intents.message_content = True

# Define the bot's command prefix and set up a command bot instance
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def servers(ctx):
    try:
        # API request headers with your specific API key
        headers = HEADERS

        # Send a GET request to the API URL
        response = requests.get(API_URL, headers=headers)

        # Check for response status
        if response.status_code == 200:
            data = response.json()

            # Initialize a list to store server information
            server_info_list = []

            # Iterate through each item in the response data
            for item in data['data']:
                if item['object'] == 'server':
                    server_id = item['attributes']['identifier']
                    server_name = item['attributes']['name']
                    server_info_list.append(f"Server Name - {server_name}\nServer ID - {server_id}")

            # If no servers found, send a message
            if not server_info_list:
                await ctx.send("No servers found.")
            else:
                # Format the server information for output
                formatted_response = "\n\n".join([f"Server {index + 1}:\n{info}" for index, info in enumerate(server_info_list)])
                await ctx.send(formatted_response)

        else:
            await ctx.send(f"Failed to connect to the API. Status Code: {response.status_code}\nResponse: {response.text}")

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

@bot.command()
async def stop(ctx, server_id: str):
    try:
        # Headers including the client API key
        headers = HEADERS

        # Construct the API URL using the provided server_id
        api_url = f"https://ptero.pondfolk.org/api/client/servers/{server_id}/power"

        # Payload to send to the API for stopping the server
        payload = {
            "signal": "stop"
        }

        # Send a POST request to change the server power state
        response = requests.post(api_url, headers=headers, json=payload)

        # Check if the request was successful
        if response.status_code == 204:
            # If successful, fetch server details to get the name and other attributes
            server_info_url = f"https://ptero.pondfolk.org/api/client/servers/{server_id}"
            server_response = requests.get(server_info_url, headers=headers)

            if server_response.status_code == 200:
                server_data = server_response.json()
                server_name = server_data['attributes']['name']

                # Send a confirmation message to the Discord channel
                await ctx.send(f"Server Name: {server_name}\nServer ID: {server_id}\nA power status change has occurred, and the server has been stopped.")
            else:
                # In case we can't get the server details, notify the user
                await ctx.send(f"Server power status changed, but could not retrieve server details. Server ID: {server_id}")
        else:
            # If the power change request fails, display the error message
            await ctx.send(f"Failed to change power status for server ID: {server_id}. Status Code: {response.status_code}\nResponse: {response.text}")

    except Exception as e:
        # Catch and print any exceptions that occur
        await ctx.send(f"An error occurred: {str(e)}")

@bot.command()
async def start(ctx, server_id: str):
    try:
        # API headers with your client API key
        headers = HEADERS

        # Construct the API URL for starting the server using the provided server_id
        api_url = f"https://ptero.pondfolk.org/api/client/servers/{server_id}/power"

        # Payload to send to the API for starting the server
        payload = {
            "signal": "start"
        }

        # Send a POST request to the API to change the server power state to start
        response = requests.post(api_url, headers=headers, json=payload)

        # Check if the request was successful
        if response.status_code == 204:
            # If successful, fetch server details to get the name and other attributes
            server_info_url = f"https://ptero.pondfolk.org/api/client/servers/{server_id}"
            server_response = requests.get(server_info_url, headers=headers)

            if server_response.status_code == 200:
                server_data = server_response.json()
                server_name = server_data['attributes']['name']

                # Send a confirmation message to the Discord channel
                await ctx.send(f"Server Name: {server_name}\nServer ID: {server_id}\nA power status change has occurred and the server has started.")
            else:
                # In case we can't get the server details, notify the user
                await ctx.send(f"Server power status changed, but could not retrieve server details. Server ID: {server_id}")
        else:
            # If the power change request fails, display the error message
            await ctx.send(f"Failed to change power status for server ID: {server_id}. Status Code: {response.status_code}\nResponse: {response.text}")

    except Exception as e:
        # Catch and print any exceptions that occur
        await ctx.send(f"An error occurred: {str(e)}")

# Run the bot with the specified token
bot.run(TOKEN)
