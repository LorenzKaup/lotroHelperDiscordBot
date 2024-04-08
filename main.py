import os

from discord import Intents
from dotenvy import load_env, read_file
from discord.ext import commands
from discord.app_commands import Choice, choices
from datetime import datetime

load_env(read_file(".env"))
TOKEN = os.getenv("DISCORD_TOKEN")

malice_rotation = [["3", "Vile cloud -9% morale every 3s", "Mobs explode", "Low hp mobs deal more damage",
                    "High hp mobs take and deal less damage other way arround if low", "Reinforcement cast",
                    "Vile cloud -15% morale every 3s", "Mobs explode on death", "more ranged damage", "Epic Tempest",
                    "Mobs heal themselves", "High hp mobs take and deal less damage other way arround if low",
                    "On death spirit o vengeance spawns"],
                   ["4", "Poison puddle morale damage", "Disease reduces max morale by 30%", "On death heals near mobs",
                    "High morale mobs deal more damage", "Fear that lets you flee",
                    "poison puddles that deal morale damage", "Poison stunning you on expiration",
                    "Mob move faster and have shorter induction", "Orc Tunnels", "Puddle that buffs damage of mobs",
                    "Mos deal more damage while high morale", "Mobs explode into smaller mobs"],
                   ["5", "Vile cloud -9% morale every 3s", "Wound to cleanse", "Mobs heal until low hp",
                    "50 damage reduction until crit", "Induction healing nearby allies to full",
                    "puddle with light and beleriand mitigation",
                    "Fear with - incoming and outgoing heal removes 15% morale on removal", "more melee damage",
                    "Epic Fervour (very nice)", "Damage reduction puddle that stacks over time", "Saurons eye +3 Dread",
                    "Fungus explosion"],
                   ["6", "Slime puddle miss chance", "-60% crit chance on monster death", "healing corruption",
                    "-inc damage adaptation corruption", "Epic monster skill: more damage", "Slime puddle miss chance",
                    "nethe", "more tactical damage", "Epic Tempest", "morale heal", "-inc damage adaptation",
                    "monsters explode into weaker monsters"],
                   ["1", "-10% damage per mob close to you", "x0.75 damage when a mob dies",
                    "corruption for damage reduction", "flies -x% critical chance",
                    "Epic monster skill: -5% morale every 1 second", "-10% damage per mob close to you",
                    "Fear: -100% ogh and -15% morale on expiration", "Glass Cannon", "Epic Fervour (very nice)",
                    "Puddle that buffs damage reduction for mobs", "flies -x% critical chance",
                    "On monster death their spirit comes back to get vengeance"],
                   ["2", "fire puddle 8% morale damage 3s", "Wound to cleanse", "mobs take and deal less damage",
                    "reflect corruption", "Wound 20% morale damage every 3", "fire puddle 8% morale damage 3s",
                    "Fear that stuns after 10s", "More aggro range", "orc tunnels", "puddle that increases mob damage",
                    "reflect corruption", "Fungus explosion on death"]]

arena_bosses = ["Akhmâr, Bhastah & Shakfut easy t4 pain t5",
                "Hortion, Ulanor rating inc",
                "Nakrov, Bhastah & Shakfut good in t5",
                "Akhmâr, Shaidal easy t4 pain t5",
                "Hortion, Bhastah & Shakfut rating inc",
                "Nakrov, Shaidal okay in t5",
                "Akhmâr, Ulanor easy t4 pain t5",
                "Hortion, Shaidal rating inc",
                "Nakrov, Ulanor good in t5"]

intents = Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix=":", intents=intents, application_id=os.getenv('APPLICATION_ID'))


@bot.event
async def on_ready():
    await bot.tree.sync()


@bot.tree.command(name="rotation_delving", description="text")
@choices(
    tier=[
        Choice(name="1", value="1"), Choice(name="2", value="2"), Choice(name="3", value="3"),
        Choice(name="4", value="4"), Choice(name="5", value="5"), Choice(name="6", value="6"),
        Choice(name="7", value="7"), Choice(name="8", value="8"), Choice(name="9", value="9"),
        Choice(name="10", value="10"), Choice(name="11", value="11"), Choice(name="12", value="12")
    ]
)
async def rotation_delving(interaction, tier: Choice[str]):
    day = days_between_dates() % 6
    output = "Variant: " + malice_rotation[day][0] + ", active malices:\n"

    if tier.name == "1":
        # 1
        output = output + malice_rotation[day][1]
    if tier.name == "2":
        # 1 2
        output = output + + malice_rotation[day][1] + ",\n" + malice_rotation[day][2]
    if tier.name == "3":
        output = output + malice_rotation[day][1] + ",\n" + malice_rotation[day][2] + ",\n" + malice_rotation[day][3]
    if tier.name == "4":
        output = output + malice_rotation[day][1] + ",\n" + malice_rotation[day][2] \
                 + ",\n" + malice_rotation[day][3] + ",\n" + malice_rotation[day][4]
    if tier.name == "5":
        output = output + malice_rotation[day][1] + ",\n" + malice_rotation[day][2] + ",\n" \
                 + malice_rotation[day][3] + ",\n" + malice_rotation[day][4] + ",\n" + malice_rotation[day][5]
    if tier.name == "6":
        output = output + malice_rotation[day][2] + ",\n" + malice_rotation[day][3] + ",\n" \
                 + malice_rotation[day][4] + ",\n" + malice_rotation[day][5] + ",\n" + malice_rotation[day][6]
    if tier.name == "7":
        output = output + malice_rotation[day][3] + ",\n" + malice_rotation[day][4] + ",\n" \
                 + malice_rotation[day][5] + ",\n" + malice_rotation[day][6] + ",\n" + malice_rotation[day][7]
    if tier.name == "8":
        output = output + malice_rotation[day][4] + ",\n" + malice_rotation[day][5] + ",\n" \
                 + malice_rotation[day][6] + ",\n" + malice_rotation[day][7] + ",\n" + malice_rotation[day][8]
    if tier.name == "9":
        output = output + malice_rotation[day][5] + ",\n" + malice_rotation[day][6] + ",\n" \
                 + malice_rotation[day][7] + ",\n" + malice_rotation[day][8] + ",\n" + malice_rotation[day][9]
    if tier.name == "10":
        output = output + malice_rotation[day][5] + ",\n" + malice_rotation[day][6] + ",\n" \
                 + malice_rotation[day][7] + ",\n" + malice_rotation[day][8] + ",\n" + malice_rotation[day][9] \
                 + ",\n" + malice_rotation[day][10]
    if tier.name == "11":
        output = output + malice_rotation[day][5] + ",\n" + malice_rotation[day][6] + ",\n" \
                 + malice_rotation[day][7] + ",\n" + malice_rotation[day][8] + ",\n" + malice_rotation[day][9] \
                 + ",\n" + malice_rotation[day][10]
    if tier.name == "12":
        output = output + malice_rotation[day][5] + ",\n" + malice_rotation[day][6] + ",\n" \
                 + malice_rotation[day][7] + ",\n" + malice_rotation[day][8] + ",\n" + malice_rotation[day][9] \
                 + ",\n" + malice_rotation[day][10] + ",\n" + malice_rotation[day][12]
    await interaction.response.send_message(output)


@bot.tree.command(name="rotation_arena", description="text")
async def rotation_arena(interaction):
    await interaction.response.send_message(arena_bosses[days_between_dates() % 9])


def days_between_dates():
    return (datetime.now().date() - datetime(2024, 4, 1).date()).days


bot.run(TOKEN)