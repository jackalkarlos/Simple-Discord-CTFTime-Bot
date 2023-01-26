import discord
import requests
from bs4 import BeautifulSoup
import asyncio
import base64
import random

global prefix
prefix = "!"

intents = discord.Intents.default()
intents.message_content = True

bot= discord.Client(intents=intents)

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("DiscordBot is in " + str(guild_count) + " guilds.")
@bot.event
async def on_message(message):
	global prefix
	if message.content[0] == prefix:
		icerik = message.content[1:]
		if icerik == "ctfcheck":
			ctfs = []
			ctflist=""
			url = "https://ctftime.org/event/list/upcoming"
			headers= {
        	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
			}
			response = requests.get(url,headers=headers)
			soup = BeautifulSoup(response.content, "html.parser")
			rows = soup.find_all("tr")
			for row in rows:
				cells = row.find_all("td")
				if len(cells) >= 1:
					ctf_name = cells[0].find("a").text
					ctf_date = cells[1].text
					ctfs.append({"name": ctf_name, "date": ctf_date})
			for i,ctf in enumerate(ctfs):
				if i<5:
					ctflist = ctflist + "CTF Name: " + ctf["name"] + "\n" + "CTF Date: " + ctf["date"] + "\n\n"
				else:
					break
			await message.channel.send(ctflist)
		elif icerik == "baslat":
			await gunluk(message)
		elif icerik == "durdur":
			await message.channel.send("Bu sunucu için günlük mesaj gönderimini durdurdum.")
			global calistirildi
			calistirildi = False
		elif icerik == "ctfmemegenerator":
			await message.channel.send(file=discord.File(random.choice(('memes/1.JPG', 'memes/2.JPG', 'memes/3.JPG', 'memes/4.PNG', 'memes/5.png', 'memes/6.jpg','memes/7.png','memes/8.png','memes/9.jpg','memes/10.jpg','memes/11.jpg','memes/12.jpg','memes/13.jpg','memes/14.png','memes/15.jpg','memes/16.png','memes/17.jpg','memes/18.jpg'))))
		elif icerik.split()[0] == "base64decode":
			try:
				b64und = icerik.split()
				b64 = b64und[1]
				decodedstring = base64.b64decode(b64)
				s = decodedstring.decode()
				await message.channel.send(s)
			except:
				await message.channel.send("İşlem başarısız oldu, gönderdiğiniz mesajı kontrol edin!")
		elif icerik.split()[0] == "changeprefix":
			try:
				prefix=(' '.join(icerik.split()[1:]))
				await message.channel.send("Prefix " + prefix + " ile değiştirilmiştir.")
			except:
				await message.channel.send("Acayip bi hata oluştu???")
		elif icerik.split()[0] == "base64encode":
			try:
				decodedstring = (' '.join(icerik.split()[1:]))
				base64_bytes = base64.b64encode(decodedstring.encode())
				base642 = base64_bytes.decode()
				await message.channel.send(base642)
			except:
				await message.channel.send("İşlem başarısız oldu, gönderdiğiniz mesajı kontrol edin!")
		else:
			await message.channel.send("Sanırsam tanımsız bir komut çalıştırdın, tekrar dener misin?")
@bot.event
async def gunluk(message):
	global calistirildi
	calistirildi = True
	while calistirildi == True:
		ctfs = []
		ctflist = ""
		url = "https://ctftime.org/event/list/upcoming"
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
		}
		response = requests.get(url, headers=headers)
		soup = BeautifulSoup(response.content, "html.parser")
		rows = soup.find_all("tr")
		for row in rows:
			cells = row.find_all("td")
			if len(cells) >= 1:
				ctf_name = cells[0].find("a").text
				ctf_date = cells[1].text
				ctfs.append({"name": ctf_name, "date": ctf_date})
		for i, ctf in enumerate(ctfs):
			if i < 5:
				ctflist = ctflist + "CTF Name: " + ctf["name"] + "\n" + "CTF Date: " + ctf["date"] + "\n\n"
			else:
				break
		await message.channel.send(ctflist)
		await asyncio.sleep(86400)

bot.run("")
