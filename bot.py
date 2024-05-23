import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='H!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def Help(ctx):
    await ctx.send(f'Hava kirliliği ile ilgili bir haber almak istiyorsan "(H!)bir" yaz ve yolla.')

@bot.command()
async def bir(ctx):
    await ctx.send("https://static.euronews.com/articles/stories/05/71/28/76/1200x675_cmsv2_3f10e8c6-02d5-5de2-b446-e90d3811ed70-5712876.jpg Hava kirliliği 2020'de Avrupa Birliği genelinde 238 bin kişinin erken ölümüne yol açtı.")

@bot.command()
async def Help2(ctx):
    await ctx.send(f'Hava kirliliği ile ilgili bir haber almak istiyorsan "(H!)iki" yaz ve yolla.')

@bot.command()
async def Help3(ctx):
    await ctx.send(f'Hava kirliliği ile ilgili bir haber almak istiyorsan "(H!)üç" yaz ve yolla.')

@bot.command()
async def iki(ctx):
    await ctx.send(f"https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2106000/endonezya-yangin-a-2107431.jpg Endonezya'da, Sumatra Adası'nda 300'den fazla noktada çıkan yangınların yol açtığı hava kirliliği nedeniyle vatandaşların evden çalışması gerektiği çağrısı yapılarak, okulların uzaktan eğitime geçmesi kararı alındı.")

@bot.command()
async def üç(ctx):
    await ctx.send(f"https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2026000/space-x-ap-2026673.jpg NASA, uzaydan hava kirliliği kontrolü yapacak. Bunun için uzaya bir cihaz fırlatıldı. Cihaz yörüngeye yerleştikten sonra Porto Riko'dan Kanada'ya kadar saat başı hava kalitesini ölçecek.")

bot.run("Gizli Token buraya")
