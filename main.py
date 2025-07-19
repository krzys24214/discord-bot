import discord
from discord import app_commands
from discord.ext import commands
import os

# --- CONFIG ---
GUILD_ID = 1197175759878488234  # ID twojego serwera
UPRAWNIENIA_ROLE_ID = 1197180404407468113  # Rola która może używać komend

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree


# Sprawdzenie, czy użytkownik ma wymaganą rolę
def has_permission_role(interaction: discord.Interaction) -> bool:
    return any(role.id == UPRAWNIENIA_ROLE_ID for role in interaction.user.roles)


# /awans
@tree.command(name="awans", description="Zgłoś awans użytkownika", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(
    kto="Wybierz osobę do awansu",
    obecny_stopien="Obecna rola",
    nowy_stopien="Nowa rola",
    powod="Powód awansu"
)
async def awans(
    interaction: discord.Interaction,
    kto: discord.Member,
    obecny_stopien: discord.Role,
    nowy_stopien: discord.Role,
    powod: str
):
    if not has_permission_role(interaction):
        await interaction.response.send_message("Brak wymaganej roli do użycia tej komendy.", ephemeral=True)
        return

    embed = discord.Embed(title="📈 Awans", color=discord.Color.green())
    embed.add_field(name="Użytkownik", value=kto.mention, inline=False)
    embed.add_field(name="Obecny stopień", value=obecny_stopien.mention, inline=True)
    embed.add_field(name="Nowy stopień", value=nowy_stopien.mention, inline=True)
    embed.add_field(name="Powód", value=powod, inline=False)
    embed.set_footer(text=f"Przez: {interaction.user.name}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed)


# /degrad
@tree.command(name="degrad", description="Zgłoś degradację użytkownika", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(
    kto="Wybierz osobę do degradacji",
    obecny_stopien="Obecna rola",
    nowy_stopien="Nowa rola",
    powod="Powód degradacji"
)
async def degrad(
    interaction: discord.Interaction,
    kto: discord.Member,
    obecny_stopien: discord.Role,
    nowy_stopien: discord.Role,
    powod: str
):
    if not has_permission_role(interaction):
        await interaction.response.send_message("Brak wymaganej roli do użycia tej komendy.", ephemeral=True)
        return

    embed = discord.Embed(title="📉 Degradacja", color=discord.Color.red())
    embed.add_field(name="Użytkownik", value=kto.mention, inline=False)
    embed.add_field(name="Obecny stopień", value=obecny_stopien.mention, inline=True)
    embed.add_field(name="Nowy stopień", value=nowy_stopien.mention, inline=True)
    embed.add_field(name="Powód", value=powod, inline=False)
    embed.set_footer(text=f"Przez: {interaction.user.name}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed)


# /zawieszenie
@tree.command(name="zawieszenie", description="Zgłoś zawieszenie użytkownika", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(
    kto="Wybierz osobę do zawieszenia",
    data_rozpoczecia="Data rozpoczęcia zawieszenia",
    data_zakonczenia="Data zakończenia zawieszenia",
    powod="Powód zawieszenia"
)
async def zawieszenie(
    interaction: discord.Interaction,
    kto: discord.Member,
    data_rozpoczecia: str,
    data_zakonczenia: str,
    powod: str
):
    if not has_permission_role(interaction):
        await interaction.response.send_message("Brak wymaganej roli do użycia tej komendy.", ephemeral=True)
        return

    embed = discord.Embed(title="⏸️ Zawieszenie", color=discord.Color.orange())
    embed.add_field(name="Użytkownik", value=kto.mention, inline=False)
    embed.add_field(name="Od", value=data_rozpoczecia, inline=True)
    embed.add_field(name="Do", value=data_zakonczenia, inline=True)
    embed.add_field(name="Powód", value=powod, inline=False)
    embed.set_footer(text=f"Przez: {interaction.user.name}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed)


# Syncowanie komend
@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"Zalogowano jako: {bot.user}")


# Uruchomienie bota
bot.run(os.environ["BOT_TOKEN"])
