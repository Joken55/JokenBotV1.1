import discord
from discord.ext import commands
import asyncio
import os
import random
import PIL
from PIL import Image
from dotenv import load_dotenv
import configparser


config = configparser.ConfigParser()
TOKEN = os.getenv('DISCORD_TOKEN')
config.read('C:/Users/Joken55/OneDrive/Bureau/Jokenbotv2/config.ini')
TOKEN = config.get('Discord', 'Token')



intents = discord.Intents().all()

Jokenbot = commands.Bot(command_prefix='!jk', description='Discordgg/Joken55', intents=intents)

# Initialiser la variable globale pour stocker le nom du fichier audio
current_audio_file = None


############################# TAS R6s ###################################


# définition des chemins d'accès aux images
agents1 = {
    "Sledge": os.path.abspath("agents1/sledge.png"),
    "Thatcher": os.path.abspath("agents1/thatcher.png"),
    "Ash": os.path.abspath("agents1/ash.png"),
    "Thermite": os.path.abspath("agents1/thermite.png"),
    "Twitch": os.path.abspath("agents1/twitch.png"),
    "Montagne": os.path.abspath("agents1/montagne.png"),
    "Glaz": os.path.abspath("agents1/glaz.png"),
    "Fuze": os.path.abspath("agents1/fuze.png"),
    "Blitz": os.path.abspath("agents1/blitz.png"),
    "IQ": os.path.abspath("agents1/iq.png"),
    "Buck": os.path.abspath("agents1/buck.png"),
    "Blackbeard": os.path.abspath("agents1/blackbeard.png"),
    "Capitão": os.path.abspath("agents1/capitao.png"),
    "Hibana": os.path.abspath("agents1/hibana.png"),
    "Jackal": os.path.abspath("agents1/jackal.png"),
    "Ying": os.path.abspath("agents1/ying.png"),
    "Zofia": os.path.abspath("agents1/zofia.png"),
    "Dokkaebi": os.path.abspath("agents1/dokkaebi.png"),
    "Lion": os.path.abspath("agents1/lion.png"),
    "Finka": os.path.abspath("agents1/finka.png"),
    "Maverick": os.path.abspath("agents1/maverick.png"),
    "Nomad": os.path.abspath("agents1/nomad.png"),
    "Gridlock": os.path.abspath("agents1/gridlock.png"),
    "Nokk": os.path.abspath("agents1/nokk.png"),
    "Amaru": os.path.abspath("agents1/amaru.png"),
    "Kali": os.path.abspath("agents1/kali.png"),
    "Iana": os.path.abspath("agents1/iana.png"),
    "Ace": os.path.abspath("agents1/ace.png"),
    "Zero": os.path.abspath("agents1/zero.png"),
    "Flores": os.path.abspath("agents1/flores.png"),
    "Osa": os.path.abspath("agents1/osa.png"),
    "Sens": os.path.abspath("agents1/sens.png"),
    "Grim": os.path.abspath("agents1/grim.png"),
}

agents2 = {
    "Smoke": os.path.abspath("agents2/Smoke.png"),
    "Mute": os.path.abspath("agents2/Mute.png"),
    "Pulse": os.path.abspath("agents2/Pulse.png"),
    "Castle": os.path.abspath("agents2/Castle.png"),
    "Doc": os.path.abspath("agents2/Doc.png"),
    "Rook": os.path.abspath("agents2/Rook.png"),
    "Tachanka": os.path.abspath("agents2/Tachanka.png"),
    "Kapkan": os.path.abspath("agents2/Kapkan.png"),
    "Jäger": os.path.abspath("agents2/Jager.png"),
    "Bandit": os.path.abspath("agents2/Bandit.png"),
    "Frost": os.path.abspath("agents2/Frost.png"),
    "Valkyrie": os.path.abspath("agents2/Valkyrie.png"),
    "Caveira": os.path.abspath("agents2/Caveira.png"),
    "Echo": os.path.abspath("agents2/Echo.png"),
    "Mira": os.path.abspath("agents2/Mira.png"),
    "Lesion": os.path.abspath("agents2/Lesion.png"),
    "Ela": os.path.abspath("agents2/Ela.png"),
    "Vigil": os.path.abspath("agents2/Vigil.png"),
    "Alibi": os.path.abspath("agents2/Alibi.png"),
    "Maestro": os.path.abspath("agents2/Maestro.png"),
    "Clash": os.path.abspath("agents2/Clash.png"),
    "Kaid": os.path.abspath("agents2/Kaid.png"),
    "Mozzie": os.path.abspath("agents2/Mozzie.png"),
    "Warden": os.path.abspath("agents2/Warden.png"),
    "Goyo": os.path.abspath("agents2/Goyo.png"),
    "Wamai": os.path.abspath("agents2/Wamai.png"),
    "Oryx": os.path.abspath("agents2/Oryx.png"),
    "Melusi": os.path.abspath("agents2/Melusi.png"),
    "Aruni": os.path.abspath("agents2/Aruni.png"),
    "Thunderbird": os.path.abspath("agents2/Thunderbird.png"),
    "Thorn": os.path.abspath("agents2/Thorn.png"),
    "Azami": os.path.abspath("agents2/Azami.png"),
    "Solis": os.path.abspath("agents2/Solis.png"),
}

# fonction pour envoyer un fichier sur le chat Discord
async def send_file(ctx, file_path):
    with open(file_path, "rb") as file:
        await ctx.send(file=discord.File(file, file_path))

# fonction pour tirer un nom au hasard et récupérer le chemin d'accès de l'image correspondante
def get_random_agent_image(agents):
    agent_name = random.choice(list(agents.keys()))
    image_path = agents[agent_name]
    return agent_name, image_path

# fonction pour tirer un nom de chaque liste et envoyer les images correspondantes sur le chat Discord
@Jokenbot.command(aliases=['RDM', 'rdm'])
async def tirage_au_sort(ctx):
    nom1, image_path1 = get_random_agent_image(agents1)
    nom2, image_path2 = get_random_agent_image(agents2)
    await ctx.send(f"L'agent que tu devras jouer est {nom1} ou {nom2} {ctx.author.mention}")
    combined_image_path = await combine_images(ctx, image_path1, image_path2)
    await send_file(ctx, combined_image_path)

async def combine_images(ctx, image_path1, image_path2):
    image1 = Image.open(image_path1).resize((100, 100), Image.LANCZOS)
    image2 = Image.open(image_path2).resize((100, 100), Image.LANCZOS)


    # combiner les deux images
    combined_image = Image.new("RGB", (2 * image1.width, image1.height), (173, 216, 230))
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (image1.width, 0))
    combined_image_path = "combined_image.png"
    combined_image.save(combined_image_path)

    return combined_image_path




############################# OnReady ####################################

@Jokenbot.event
async def on_ready():
    print(f'Connecté en tant que Jokenbot')


Jokenbot.run(TOKEN)