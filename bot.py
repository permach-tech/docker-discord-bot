import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

# Tarot deck data
TAROT_DECK = [
    {"name": "The Fool", "emoji": "🤹", "image": "https://i.imgur.com/jxI2zQC.png", "fortune": "A new journey begins—embrace the unknown with excitement and trust in the path ahead."},
    {"name": "The Magician", "emoji": "🧙", "image": "https://i.imgur.com/UwW51xp.png", "fortune": "You hold the power to shape your reality—focus your will and manifest your desires."},
    {"name": "The High Priestess", "emoji": "🔮", "image": "https://i.imgur.com/GAOdPr9.png", "fortune": "Trust your intuition—hidden knowledge and deeper truths await discovery."},
    {"name": "The Empress", "emoji": "👑", "image": "https://i.imgur.com/mwa90vF.png", "fortune": "Creativity and abundance flourish—nurture yourself and those around you."},
    {"name": "The Emperor", "emoji": "🏛️", "image": "https://i.imgur.com/pJgVxoO.png", "fortune": "Establish structure and discipline—lead with confidence and authority."},
    {"name": "The Hierophant", "emoji": "📜", "image": "https://i.imgur.com/UynAuCA.png", "fortune": "Seek guidance from tradition, spiritual mentors, or institutions—wisdom is within reach."},
    {"name": "The Lovers", "emoji": "❤️", "image": "https://i.imgur.com/ePzrQ5h.png", "fortune": "A deep connection, partnership, or life-changing decision—choose with your heart and mind."},
    {"name": "The Chariot", "emoji": "🏇", "image": "https://i.imgur.com/uAnJM8j.png", "fortune": "Self-discipline and determination will lead you to victory—stay in control of your path."},
    {"name": "Strength", "emoji": "🦁", "image": "https://i.imgur.com/F4fogs7.png", "fortune": "True power comes from patience, resilience, and inner courage—face challenges with grace."},
    {"name": "The Hermit", "emoji": "🧙", "image": "https://i.imgur.com/KJoAIBU.png", "fortune": "A time for introspection—seek solitude to find deeper wisdom and clarity."},
    {"name": "Wheel of Fortune", "emoji": "🎡", "image": "https://i.imgur.com/7AWo9NM.png", "fortune": "Cycles of change are in motion! Trust in fate and embrace new opportunities."},
    {"name": "Justice", "emoji": "⚖️", "image": "https://i.imgur.com/3ciq6BA.png", "fortune": "Truth, fairness, and accountability will guide you—seek balance and act with integrity."},
    {"name": "The Hanged Man", "emoji": "🪢", "image": "https://i.imgur.com/9c1nJA8.png", "fortune": "Surrender to a new perspective—pause and see things differently."},
    {"name": "Death", "emoji": "💀", "image": "https://i.imgur.com/n2O3qlM.png", "fortune": "Endings bring transformation—embrace change and the chance for a fresh start."},
    {"name": "Temperance", "emoji": "⚗️", "image": "https://i.imgur.com/gKc1zX1.png", "fortune": "Balance and moderation will bring healing and harmony into your life."},
    {"name": "The Devil", "emoji": "👹", "image": "https://i.imgur.com/LHlM6qF.png", "fortune": "Beware of toxic attachments or temptations—acknowledge unhealthy patterns and break free."},
    {"name": "The Tower", "emoji": "⚡", "image": "https://i.imgur.com/4hSNdKa.png", "fortune": "A sudden upheaval—destruction clears the way for transformation and growth."},
    {"name": "The Star", "emoji": "⭐", "image": "https://i.imgur.com/fmETCBx.png", "fortune": "Hope and inspiration will light your way—trust in the future and remain optimistic."},
    {"name": "The Moon", "emoji": "🌙", "image": "https://i.imgur.com/sKM2K4c.png", "fortune": "Things may not be as they seem—trust your instincts and uncover hidden truths."},
    {"name": "The Sun", "emoji": "🌞", "image": "https://i.imgur.com/lUnUQQ0.png", "fortune": "Happiness, vitality, and success shine upon you—embrace joy and confidence."},
    {"name": "Judgement", "emoji": "📯", "image": "https://i.imgur.com/6AsdeLB.png", "fortune": "A call to self-awareness and renewal—reflect and rise to a new chapter of life."},
    {"name": "The World", "emoji": "🌍", "image": "https://i.imgur.com/Xh9vYgG.png", "fortune": "Completion, achievement, and wholeness—you have reached an important milestone."},
    # Reverse Cards
    {"name": "The Fool (Reversed)", "emoji": "🙈", "image": "https://i.imgur.com/wHNh6Ub.png", "fortune": "Recklessness or hesitation—think carefully before leaping into the unknown."},
    {"name": "The Magician (Reversed)", "emoji": "🧙‍♂️", "image": "https://i.imgur.com/2GLidmg.png", "fortune": "Deception or untapped potential—be mindful of manipulation and self-doubt."},
    {"name": "The High Priestess (Reversed)", "emoji": "🔮", "image": "https://i.imgur.com/h5uXUuT.png", "fortune": "Blocked intuition or hidden secrets—trust yourself and look beyond illusions."},
    {"name": "The Empress (Reversed)", "emoji": "👑", "image": "https://i.imgur.com/m2T8eO3.png", "fortune": "Neglecting self-care or creative blocks—reconnect with your nurturing energy."},
    {"name": "The Emperor (Reversed)", "emoji": "🏛️", "image": "https://i.imgur.com/t7G3eCK.png","fortune": "Abuse of power or control issues—balance authority with flexibility"},
    {"name": "The Hierophant (Reversed)", "emoji": "📜", "image": "https://i.imgur.com/xheLgnu.png", "fortune": "Challenging traditions—seek your own truth outside of conventional beliefs."},
    {"name": "The Lovers (Reversed)", "emoji": "❤️", "image": "https://i.imgur.com/F339mDm.png", "fortune": "Disharmony in relationships or indecision—realign with your values and communicate."},
    {"name": "The Chariot (Reversed)", "emoji": "🏇", "image": "https://i.imgur.com/T1F0oSJ.png", "fortune": "Lack of direction or willpower—regain control before moving forward."},
    {"name": "Strength (Reversed)", "emoji": "🦁", "image": "https://i.imgur.com/nW3L7IT.png", "fortune": "Self-doubt and inner struggles—find confidence and courage within."},
    {"name": "The Hermit (Reversed)", "emoji": "🧙", "image": "https://i.imgur.com/OrqOWuK.png", "fortune": "Isolation or avoidance—step out and seek guidance when needed."},
    {"name": "Wheel of Fortune (Reversed)", "emoji": "🎡", "image": "https://i.imgur.com/KZZ1MRI.png", "fortune": "Unexpected setbacks—adapt to challenges and trust in life's cycles."},
    {"name": "Justice (Reversed)", "emoji": "⚖️", "image": "https://i.imgur.com/qIVBYoK.png", "fortune": "Dishonesty or unfairness—seek truth and take responsibility for your actions."},
    {"name": "The Hanged Man (Reversed)", "emoji": "🪢", "image": "https://i.imgur.com/pKGlyUv.png", "fortune": "Stagnation or resistance to change—let go of control and embrace a new perspective."},
    {"name": "Death (Reversed)", "emoji": "💀", "image": "https://i.imgur.com/q622mvq.png", "fortune": "Fear of transformation or change—release the past to make room for growth."},
    {"name": "Temperance (Reversed)", "emoji": "⚗️", "image": "https://i.imgur.com/qoTu5Gk.png", "fortune": "Imbalance or excess—seek moderation to restore harmony."},
    {"name": "The Devil (Reversed)", "emoji": "👹", "image": "https://i.imgur.com/ROJ18Mj.png", "fortune": "Breaking free from toxic influences—reclaim your power and independence."},
    {"name": "The Tower (Reversed)", "emoji": "⚡", "image": "https://i.imgur.com/CIxHyW9.png", "fortune": "Avoiding necessary change—face the inevitable and rebuild stronger."},
    {"name": "The Star (Reversed)", "emoji": "⭐", "image": "https://i.imgur.com/TUicPd3.png", "fortune": "Lack of faith or inspiration—reconnect with hope and purpose."},
    {"name": "The Moon (Reversed)", "emoji": "🌙", "image": "https://i.imgur.com/I3z8ZxF.png", "fortune": "Clarity emerging—illusions fade as the truth comes to light."},
    {"name": "The Sun (Reversed)", "emoji": "🌞", "image": "https://i.imgur.com/BRFXlbX.png", "fortune": "Temporary setbacks or delays—stay positive and keep moving forward."},
    {"name": "Judgement (Reversed)", "emoji": "📯", "image": "https://i.imgur.com/pFsSOMn.png", "fortune": "Self-doubt or lack of accountability—reflect on your actions and embrace transformation."},
    {"name": "The World (Reversed)", "emoji": "🌍",  "image": "https://i.imgur.com/83uy60L.png", "fortune": "Unfinished business—tie up loose ends before moving on to new opportunities."}
]

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Enable intents
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Command "tarot" for the tarot Card Reading
@bot.tree.command(name="tarot", description="Draw a random tarot card")
async def tarot(interaction: discord.Interaction):
    # Draw a random card
    card = random.choice(TAROT_DECK)
    
    # Create the embed
    embed = discord.Embed(
        title="🔮 Your Tarot Reading 🔮",
        description=f"You have drawn: **{card['emoji']} {card['name']}**\n*{card['fortune']}*",
        color=discord.Color.red()
    )
    
    # Add the card image
    embed.set_image(url=card['image'])
    
    # Add footer
    embed.set_footer(text=f"May fate guide your path, {interaction.user.display_name}. ✨")
    
    # Send the response
    await interaction.response.send_message(embed=embed)

# Command "number" for a lucky number
@bot.tree.command(name="number", description="Get your lucky number for today")
async def number(interaction: discord.Interaction):
    # Generate lucky number (1-99)
    lucky_number = random.randint(1, 99)
   
    # Create the embed
    embed = discord.Embed(
        title="🔢 Your Lucky Number 🔢",
        description=f"Your lucky number for today is: **{lucky_number}**",
        color=discord.Color.gold()
    )
    
    # Send the response
    await interaction.response.send_message(embed=embed)

# Command "flip" for flipping a coin
@bot.tree.command(name="flip", description="Flip a coin")
async def flip(interaction: discord.Interaction):
    # Flip a coin
    result = random.choice(["Heads", "Tails"])
    emoji = "🌕" if result == "Heads" else "🌑"
    
    # Create the embed
    embed = discord.Embed(
        title=f"🪙 Coin Flip 🪙",
        description=f"The coin landed on: **{result}** {emoji}",
        color=discord.Color.blue()
    )
    
    # Send the response
    await interaction.response.send_message(embed=embed)

#command "roll" for rolling a die
@bot.tree.command(name="roll", description="Roll a six-sided die")
async def roll(interaction: discord.Interaction):
    # Roll the die
    result = random.randint(1, 6)
    
    # Dice emoji mapping
    dice_emojis = {
        1: "1️⃣",
        2: "2️⃣",
        3: "3️⃣",
        4: "4️⃣",
        5: "5️⃣",
        6: "6️⃣"
    }
    
    # Create the embed
    embed = discord.Embed(
        title="🎲 Dice Roll 🎲",
        description=f"You rolled a: **{result}** {dice_emojis[result]}",
        color=discord.Color.green()
    )
    
    # Add footer
    embed.set_footer(text="Roll again?")
    
    # Send the response
    await interaction.response.send_message(embed=embed)

bot.run(TOKEN)