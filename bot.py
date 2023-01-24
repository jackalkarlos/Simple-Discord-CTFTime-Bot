import discord
import requests
from bs4 import BeautifulSoup
import asyncio
import base64

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
	if message.content[0] == "!":
		icerik = message.content[1:]
		if icerik == "ctfcheck":
			ctfs = []
			ozyazim=""
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
					ozyazim = ozyazim + "CTF Name: " + ctf["name"] + "\n" + "CTF Date: " + ctf["date"] + "\n\n"
				else:
					break
			await message.channel.send(ozyazim)
		elif icerik == "baslat":
			await gunluk(message)
		elif icerik == "durdur":
			await message.channel.send("Bu sunucu için günlük mesaj gönderimini durdurdum.")
			global calistirildi
			calistirildi = False
		elif icerik.split()[0] == "base64decode":
			try:
				b64und = icerik.split()
				b64 = b64und[1]
				decodedstring = base64.b64decode(b64)
				s = decodedstring.decode()
				await message.channel.send(s)
			except:
				await message.channel.send("İşlem başarısız oldu, gönderdiğiniz mesajı kontrol edin!")
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
		ozyazim = ""
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
				ozyazim = ozyazim + "CTF Name: " + ctf["name"] + "\n" + "CTF Date: " + ctf["date"] + "\n\n"
			else:
				break
		await message.channel.send(ozyazim)
		await asyncio.sleep(86400)

bot.run("")
