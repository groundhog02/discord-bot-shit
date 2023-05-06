import discord
# from discord.ext import commands

# with open('settings.json',mode='r',encoding = 'utf8') as jfile:
#     settings = json.load(jfile)

intents = discord.Intents.all()
# token = settings['token']
Client = discord.Client(intents=intents)
# client = commands.Bot(command_prefix = "$",intents=intents)

# for Filename in os.listdir('./cmds'):
#     if Filename.endswith('.py'):
#         client.load_extension(f'cmds.{Filename[:-3]}')
# for Filename in os.listdir('./events'):
#     if Filename.endswith('.py'):
#         client.load_extension(f'events.{Filename[:-3]}')
# keep_alive.keep_alive()
Client.run("MTEwNDA1ODUzMjE3ODk2MDQ3Ng.Gw_jdt.q4_V1eeZ9-_XOb0ECvTWoXqbUmFyb75LHML-po")