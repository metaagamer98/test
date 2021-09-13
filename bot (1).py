import discord
from discord.ext import commands
import mysql.connector
from mysql.connector import Error
import string    
import random
client = commands.Bot(command_prefix = "!")

Database = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "tokens")
Function = Database.cursor()

@client.command()
@commands.has_role(870715971701178418)
async def atoken(ctx, ip):
    sql = "INSERT INTO tokens (token, ip) VALUES (%s, %s)"
    token = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
    val = (token, ip)
    Function.execute(sql, val)
    Database.commit()
    Embed = discord.Embed(
        title = 'License Key Successfully Created',
        description = 'License Key: ```'+token+'```'
    )
    await ctx.send(embed = Embed)

@client.command()
@commands.has_role(870715971701178418)
async def dtoken(ctx, token):
    sql = "DELETE FROM tokens WHERE token = '"+token+"'"
    Function.execute(sql)
    Database.commit()
    Embed = discord.Embed(
        title = 'License Key Successfully Deleted',
        description = 'License Key: ```'+token+'```'
    )
    await ctx.send(embed = Embed)

@client.command()
@commands.has_role(870715971701178418)
async def etoken(ctx, token, ip):
    sql = "UPDATE tokens SET ip = '"+ip+"' WHERE token = '"+token+"'"
    Function.execute(sql)
    Database.commit()
    Embed = discord.Embed(
        title = 'License Key Successfully Edited',
        description = 'License Key: ```'+token+'```\n IP: ```'+ip+'```'
    )
    await ctx.send(embed = Embed)

@client.command()
@commands.has_role(870715971701178418)
async def itoken(ctx, token):
    sql = "SELECT ip FROM tokens WHERE token = '"+token+"'"
    Function.execute(sql)
    result = Function.fetchone()
    for x in result:
        IP = x
    Embed = discord.Embed(
        title = 'License Key Info',
        description = 'License Key: ```'+token+'```\n IP: ```'+IP+'```'
    )
    await ctx.send(embed = Embed)

client.run("BOT TOKEN")