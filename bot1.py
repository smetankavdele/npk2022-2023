#импорты 
import math
import aiosqlite
import asyncio
import sqlite3
import discord
import json
from discord.ext import commands
from discord import utils
from discord.utils import get
from asyncio import sleep as s
from Cybernator import Paginator
from discord.ui import Select, Button, View
from datetime import datetime

#команды для установки необходимых библиотек
#pip install discord.py
#pip install py-cord
#pip install aiosqlite
#pip install asyncio
#pip install sqlite3
#pip install Cybernator

#префикс бота
prefix = '$'

bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())
bot.remove_command('help')


#язык/language
#  1 = RU
#  2 = EN
#  3 = UA
#  4 = BY
language = 1
#канал для отправки логов
logschannel = 888164664012328991
#канал для отправки логов бана
banlogchannel = None
#канал для отправки логов мут
mutelogchannel = None
#канал для отправки логов варнов
warnlogchannel = None
#роль редактора
Krole = 988375789814820934
#роль пользователя
Prole = 821361329771642902
#руководящая роль для "$команды"
Rrole = 902582249051017258
#администраторская роль для "$команды"
Arole = 930825712624082964
#id бота
idbota = 712744787186417734
idtestbota = 1015998739325911190
#количество варнов до перманентного бана
count_warns_to_permban = 10
#количество варнов до бана
count_warns_to_ban = 999
#количество варнов до мута
count_warns_to_mute = 4
count_warns_to_mute1 = 4
count_warns_to_mute2 = 5
count_warns_to_mute3 = 6
count_warns_to_mute4 = 7
count_warns_to_mute5 = 8
count_warns_to_mute6 = 9
#время бана за варны(в минутах)
time_to_warnban = 0
# время мута за варны(в минутах)
time_to_warnmute = 600
time_to_warnmute1 = 4320
time_to_warnmute2 = 8640
time_to_warnmute3 = 14400
time_to_warnmute4 = 18720
time_to_warnmute5 = 23040
time_to_warnmute6 = 36000
token = "NzEyNzQ0Nzg3MTg2NDE3NzM0.GReljR.rD0EU6TnlwHMhaEcuq5P9qW_L7kpJHY7aGWrGQ"
tokentest = "MTAxNTk5ODczOTMyNTkxMTE5MA.GGWznV.Q2Hea9z72JRFfpE1i5HCVDYWmKgOnhvfsFUwr0"
temp = []


if language == None:
	language = 1

if banlogchannel == None:
	banlogchannel = logschannel
if mutelogchannel == None:
	mutelogchannel = logschannel
if warnlogchannel == None:
	warnlogchannel = logschannel

#создание таблицы
with sqlite3.connect('statistika.db') as db:
	sql = db.cursor()


#создание таблицы
with sqlite3.connect('statistika.db') as db:
	sql = db.cursor()
#стобики
tablici = """
CREATE TABLE IF NOT EXISTS stats(
	ivtuserid VARCHAR,
	ivtusername TEXT,
	iventname TEXT,
	gradeivent BIGINT(2) NOT NULL  ,
	ivtcomment TEXT NOT NULL,
	admuserid VARCHAR,
	admusername TEXT,
	administratorname TEXT,
	gradework BIGINT(2) NOT NULL,
	admcomment TEXT NOT NULL 
);
CREATE TABLE IF NOT EXISTS warns(
	userid INT,
	username TEXT,
	adminname TEXT,
	adminid TEXT,
	sluchai TEXT,
	sluchai1 BIGINT,
	kolichestvo TEXT,
	comment TEXT
)"""
sql.executescript(tablici)
db.commit()

sql.executescript(tablici)
db.commit()

#пасхальная команда
@bot.command()
async def Neon(ctx):
	await ctx.channel.purge( limit =1 )
	await ctx.send('Мой ручной маленький тестер неанус =)')

#пасхальная команда
@bot.command()
async def ПЕЧЕНЕГР(ctx):
	await ctx.channel.purge( limit =1 )
	await ctx.send('Хрустящий 2-ой тестер с приятным привкусом =)')

#пасхальная команда
@bot.command()
async def BreadCat(ctx):
	await ctx.channel.purge( limit =1 )
	await ctx.send('хлебкоткренднльспидранерсупергеймербравлстарсprogamerhaosnotpidorgeometrydasherтераристнонесмертниквыпилагушускамер9000станокдлясваркиплиткимальвина314иэльфистингвscpsosatфанатхелдораручнойолегсметаны3тестер')

#пасхальная команда
@bot.command()
async def OmerX(ctx):
	await ctx.channel.purge( limit =1 )
	await ctx.send("https://cdn.discordapp.com/attachments/787411365647089676/1027572779647762472/unknown.png")


#сообщение в консоль о запуске бота, статус бота, статус активности (обычно это в какую игру играет пользователь. В нашем случае указана "SCP secret labaratory")

if language == 1:
	print('подключение...')
if language == 2:
	print('connecting...')
if language == 3:
	print('підключення...')
if language == 4:
	print('cпадключэнне...')

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Устанавливает майнер на твой пк'))
	if language == 1:
		print("Я подключен, милорд!")
	if language == 2:
		print("I am connected, my lord!")
	if language == 3:
		print("Я підключений, мілорде!")
	if language == 4:
		print("Я падключаны, мілорд!")

	if language == 1:
		print('Введите: $обстав для акцивации цикла обновления статистики')
	if language == 2:
		print('Enter: $obstav to trigger the stats update cycle')
	if language == 3:
		print('Введіть: $онстаф щоб запустити цикл оновлення статистики.')
	if language == 4:
		print('Увядзіце: $абстаў для акцывацыі цыклу абнаўлення статыстыкі')
	#обновление 
	for sa1 in sql.execute("SELECT AVG(gradeivent) FROM stats WHERE admuserid == 0"):
		sa11 = str(sa1)
		if language == 1:
			print(f"КИ {sa11[1:-2]}")
		if language == 2:
			print(f"EQ {sa11[1:-2]}")
		if language == 3:
			print(f"ЯІ {sa11[1:-2]}")
		if language == 4:
			print(f"ЯІ {sa11[1:-2]}")
		db.commit()

		with open('DStats.json') as react_file:
			data = json.load(react_file)
			for x in data:
				ki = x['ki']

		channel4 = bot.get_channel(ki)
		if language == 1:
			new_name4 = f'🥏К/И: {sa11[1:-2]}/10'
		if language == 2:
			new_name4 = f'🥏E/Q: {sa11[1:-2]}/10'
		if language == 3:
			new_name4 = f'🥏Я/І: {sa11[1:-2]}/10'
		if language == 4:
			new_name4 = f'🥏Я/І: {sa11[1:-2]}/10'
	for sa2 in sql.execute("SELECT AVG(gradework) FROM stats WHERE ivtuserid == 0"):
		sa22 = str(sa2)
		if language == 1:
			print(f"РА {sa22[1:-2]}")
		if language == 2:
			print(f"AW {sa22[1:-2]}")
		if language == 3:
			print(f"РП {sa22[1:-2]}")
		if language == 4:
			print(f"ПА {sa22[1:-2]}")
		db.commit()

		with open('DStats.json') as react_file:
			data = json.load(react_file)
			for x in data:
				ra = x['ra']

		channel5 = bot.get_channel(ra)
		if language == 1:
			new_name5 = f'🔩Р/А: {sa22[1:-2]}/10'
		if language == 2:
			new_name5 = f'🔩A/W: {sa22[1:-2]}/10'
		if language == 3:
			new_name5 = f'🔩Р/П: {sa22[1:-2]}/10'
		if language == 4:
			new_name5 = f'🔩П/А: {sa22[1:-2]}/10'
		while True:
			await s(60*5)
			if channel4 != None:
				await channel4.edit(name = new_name4)
				if language == 1:
					print('"К/И" обновлено')
				if language == 2:
					print('"E/Q" updated')
				if language == 3:
					print('"Я/І" оновлено')
				if language == 4:
					print('"Я/І" абноўлена')
			else:
				if language == 1:
					print('"К/И" не существует')
				if language == 2:
					print('"E/Q" does not exist')
				if language == 3:
					print('"Я/І" не існує')
				if language == 4:
					print('"Я/І" не існуе')
			if channel5 != None:
				await channel5.edit(name = new_name5)
				if language == 1:
					print('"Р/А" обновлено')
				if language == 2:
					print('"A/W" updated')
				if language == 3:
					print('"Р/П" оновлено')
				if language == 4:
					print('"П/А" абноўлена')
			else:
				if language == 1:
					print('"Р/А" не существует')
				if language == 2:
					print('"Р/А" does not exist')
				if language == 3:
					print('"Р/А" не існує')
				if language == 4:
					print('"Р/А" не існує')


#@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		if language == 1:
			title_error_two = 'Введенная вами команда не существует'
			desc_error_two = 'Используйте **$команды**, чтобы просмотреть список всех доступных команд'
		if language == 2:
			title_error_two = 'The command you entered does not exist'
			desc_error_two = 'Use **$commands** to list all available commands'
		if language == 3:
			title_error_two = 'Введена вами команда не існує'
			desc_error_two = 'Використовуйте **$команди**, щоб переглянути список усіх доступних команд'
		if language == 4:
			title_error_two = 'Уведзеная вамі каманда не існуе'
			desc_error_two = 'Выкарыстоўвайце **$каманды**, каб прагледзець спіс усіх даступных каманд'
		embed_var_two = discord.Embed(title=title_error_two, description=desc_error_two, color=0xFF0000)
		await ctx.reply(embed=embed_var_two)

	elif isinstance(error, commands.MissingPermissions):
		if language == 1:
			title_error_two = 'У вас недостаточно прав для использования данной команды'
			desc_error_two = 'Используйте **$команды**, чтобы просмотреть список всех доступных команд'
		if language == 2:
			title_error_two = "You do not have sufficient rights to use this command"
			desc_error_two =  'Use **$commands** to list all available commands'
		if language == 3:
			title_error_two = "У вас недостатньо прав для використання цієї команди"
			desc_error_two =  'Використовуйте **$команди**, щоб переглянути список усіх доступних команд'
		if language == 4:
			title_error_two = "У вас недастаткова правоў для выкарыстання дадзенай каманды"
			desc_error_two =  'Выкарыстоўвайце **$каманды**, каб прагледзець спіс усіх даступных каманд'
		embed_var_two = discord.Embed(title=title_error_two, description=desc_error_two, color=0xFF0000)
		await ctx.reply(embed=embed_var_two)

	elif isinstance(error, commands.MissingRequiredArgument):
		if language == 1:
			title_error_two = 'Вы не указали все необходимые аргументы'
			desc_error_two = 'Используйте **$хелп [название_команды]**, чтобы получить информацию о команде'
		if language == 2:
			title_error_two = "You didn't provide all required arguments"
			desc_error_two = 'Use **$help [commandname]** to get information about the command'
		if language == 3:
			title_error_two = 'Ви не вказали всі необхідні аргументи'
			desc_error_two = 'Використовуйте **$хелп [назва_команди]**, щоб отримати інформацію про команду'
		if language == 4:
			title_error_two = 'Вы не ўказалі ўсе неабходныя аргументы'
			desc_error_two = 'Выкарыстоўвайце **$хэлп [назва_каманды]**, каб атрымаць інфармацыю аб камандзе'
		embed_var_two = discord.Embed(title=title_error_two, description=desc_error_two, color=0xFF0000)
		await ctx.reply(embed=embed_var_two)

	elif isinstance(error, commands.MemberNotFound):
		if language == 1:
			title_error_two = 'Вы указали несуществующего пользователя'
			desc_error_two = 'Указать пользователя можно через: `Упоминание`, `Никнейм`, `ID`. \n Убедитесь, что пользователь существует'
		if language == 2:
			title_error_two = 'You specified a non-existent user'
			desc_error_two =  'You can specify a user through: `Mention`, `Nickname`, `ID`. \n Make sure the user exists'
		if language == 3:
			title_error_two = 'Ви вказали неіснуючого користувача'
			desc_error_two = 'Вказати користувача можна через: `Згадування`, `Нікнейм`, `ID`. \n Переконайтеся, що користувач існує'
		if language == 4:
			title_error_two = 'Вы паказалі неіснуючага карыстальніка'
			desc_error_two = 'Указаць карыстальніка можна праз: `Упамінанне`, `Нікнейм`, `ID`. \n Упэўніцеся, што карыстальнік існуе'
		embed_var_two = discord.Embed(title=title_error_two, description=desc_error_two, color=0xFF0000)
		await ctx.reply(embed=embed_var_two)

#автоматическая выдача определённой роли новым пользователям при входе на сервер
#лог входа на сервер (последняя строчка) 
@bot.event
async def on_member_join( member ):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel( logschannel )

	role = discord.utils.get( member.guild.roles, id = Prole )

	await member.add_roles( role )
	if language == 1:
		await channel.send( embed = discord.Embed( title = f'[{dt_string}] Пользователь: **{member.name}**, присоеденился к нам', description = f'\n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xffb90f ))
		await member.send(f"Приветствуем на нашем сервере **{member.guild.name}**, надеюсь тебе понравится у нас :cookie: ")
	if language == 2:
		await channel.send( embed = discord.Embed( title = f'{dt_string}] User: **{member.name}**, joined us', description = f'\n \n Username: {member} \n User ID: {member.id}', color = 0xffb90f ))
		await member.send(f"Welcome to our server **{member.guild.name}**, hope you enjoy our :cookie: ")
	if language == 3:
		await channel.send( embed = discord.Embed( title = f'[{dt_string}] Користувач: **{member.name}**, приєднався до нас', description = f'\n \n Ім\'я користувача: {member} \n ID користувача: {member.id}', color = 0xffb90f ))
		await member.send(f"Вітаємо на нашому сервері **{member.guild.name}**, сподіваюся тобі сподобається у нас :cookie: ")
	if language == 4:
		await channel.send( embed = discord.Embed( title = f'[{dt_string}] Карыстальнік: **{member.name}**, далучыўся да нас', description = f'\n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}', color = 0xffb90f ))
		await member.send(f"Вітаю на нашым серверы **{member.guild.name}**, спадзяюся табе спадабаецца ў нас :cookie: ")

#лог выхода с сервера
@bot.event
async def on_member_remove( member ):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel( logschannel )
	if language == 1:
		await channel.send( embed = discord.Embed( title = f'[{dt_string}] Пользователь: **{ member.name}**, покинул нас', description= f'\n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0x00ced1 ))
	if language == 2:
		await channel.send( embed = discord.Embed( title = f'[{dt_string}] User: **{ member.name}**, left us', description= f'\n \n Username: {member} \n User ID: {member.id}', color = 0x00ced1 ))
	if language == 3:
		await channel.send( embed = discord.Embed( title = f'[{dt_string}] Користувач: **{ member.name}**, покинув нас', description= f'\n \n Ім\'я користувача: {member} \n ID користувача: {member.id}', color = 0x00ced1 ))
	if language == 4:
		await channel.send( embed = discord.Embed( title = f'[{dt_string}] Карыстальнік: **{ member.name}**, пакінуў нас', description= f'\n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}', color = 0x00ced1 ))

#лог удаления сообщения
@bot.event
async def on_message_delete(message):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel(logschannel)
	if message.author != 'Kara$1k':
		if language == 1:
			embed = discord.Embed(
				title = f"[{dt_string}] Сообщение от {message.author} было удалено.\n"
				f"Содержимое: {message.content}", description = f"Канал: {message.channel.mention}"
				f"\n \n Имя пользователя: {message.author} \n ID пользователя: {message.author.id}", color = 0x1e90ff)
		if language == 2:
			embed = discord.Embed(
				title = f"[{dt_string}] The message from {message.author} has been deleted.\n"
				f"Content: {message.content}", description = f"Channel: {message.channel.mention}"
				f"\n \n Username: {message.author} \n User ID: {message.author.id}", color = 0x1e90ff)
		if language == 3:
			embed = discord.Embed(
				title = f"[{dt_string}] Повідомлення від {message.author} було видалено.\n"
				f"Вміст: {message.content}", description = f"Канал: {message.channel.mention}"
				f"\n \n Ім'я користувача: {message.author} \n ID користувача: {message.author.id}", color = 0x1e90ff)
		if language == 4:
			embed = discord.Embed(
				title = f"[{dt_string}] Паведамленне ад {message.author} было выдаленае.\n"
				f"Змесціў: {message.content}", description = f"Канал: {message.channel.mention}"
				f"\n \n Імя карыстальніка: {message.author} \n ID карыстальніка: {message.author.id}", color = 0x1e90ff)
		await channel.send(embed = embed)

#лог редактирования сообщения
@bot.event
async def on_message_edit(message_before, message_after):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	if message_before.author.id != idbota:
		if message_before.author.id !=  idtestbota:
			if language == 1:
				embed = discord.Embed(title=f"[{dt_string}] Пользователь {message_before.author.name} отредактировал сообщение", description="", color=0xff3030)
				embed.add_field(name= "Было:" ,value= message_before.content,inline =True)
				embed.add_field(name= "Стало" ,value= message_after.content , inline=True)
				embed.set_footer(text=f"Имя пользователя: {message_before.author.name} \n ID пользователя: {message_before.author.id}")
			if language == 2:
				embed = discord.Embed(title=f"[{dt_string}] User {message_before.author.name} has edited the message", description="", color=0xff3030)
				embed.add_field(name= "Before:" ,value= message_before.content,inline =True)
				embed.add_field(name= "Became" ,value= message_after.content , inline=True)
				embed.set_footer(text=f"Username: {message_before.author.name} \n UserID: {message_before.author.id}")
			if language == 3:
				embed = discord.Embed(title=f"[{dt_string}] Користувач {message_before.author.name} відредагував повідомлення", description="", color=0xff3030)
				embed.add_field(name= "Було:" ,value= message_before.content,inline =True)
				embed.add_field(name= "Стало" ,value= message_after.content , inline=True)
				embed.set_footer(text=f"Ім'я користувача: {message_before.author.name} \n ID користувача: {message_before.author.id}")
			if language == 4:
				embed = discord.Embed(title=f"[{dt_string}] Карыстальнік {message_before.author.name} адрэдагаваў паведамленне", description="", color=0xff3030)
				embed.add_field(name= "Было:" ,value= message_before.content,inline =True)
				embed.add_field(name= "Стала" ,value= message_after.content , inline=True)
				embed.set_footer(text=f"Імя карыстальніка: {message_before.author.name} \n ID карыстальніка: {message_before.author.id}")
			channel=bot.get_channel(logschannel)
			await channel.send(embed=embed)
	else:
		pass

#логи входа, выхода, перезахода в голосовой канал
@bot.event
async def on_voice_state_update(member, before, after):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y ")
	if after.channel:
		with open('prgs.json') as react_file:
			data = json.load(react_file)
			for x in data:
				if after.channel.id == x['channel']:
					guild = member.guild 
					category = discord.utils.get(guild.categories, id= x['category'])
					created_channel = await guild.create_voice_channel(
						f'╠━⟪🔒⟫━╣{member.display_name}',
						position=6,
						category=category,
						bitrate=96000
					)
					await created_channel.set_permissions(member, connect=True, mute_members=True, move_members=True, manage_channels=True)
					await member.move_to(created_channel)
					temp.append(created_channel.id)

	elif before.channel:
		if before.channel.id in temp:
			if not before.channel.members:
				return await before.channel.delete()

	if before.channel == after.channel:
		return
	if not before.channel:
		channel = bot.get_channel( logschannel )
		if language == 1:
			embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member.name} зашёл в голосовой канал", description = f"Канал: {after.channel.mention} \n \n Имя пользователя: {member} \n ID пользователя: {member.id}", color  = 0x00ff00)
		if language == 2:
			embed = discord.Embed(title = f"[{dt_string}] User: {member.name} joined the voice channel", description = f"Channel: {after.channel.mention} \n \n Username: {member} \n User ID: {member.id }", color  = 0x00ff00)
		if language == 3:
			embed = discord.Embed(title = f"[{dt_string}] Користувач: {member.name} зайшов до голосового каналу", description = f"Канал: {after.channel.mention} \n \n Ім'я користувача: {member} \n ID користувача: {member.id }", color  = 0x00ff00)
		if language == 4:
			embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member.name} зайшоў у галасавы канал", description = f"Канал: {after.channel.mention} \n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id }", color  = 0x00ff00)

		return await channel.send(embed = embed)

	if not after.channel:
		channel = bot.get_channel( logschannel )
		if language == 1:
			embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member.name} вышел из голосового канала", description = f"Канал: {before.channel.mention} \n \n Имя пользователя: {member} \n ID пользователя: {member.id}", color  = 0x00ff00)
		if language == 2:
			embed = discord.Embed(title = f"[{dt_string}] User: {member.name} left the voice channel", description = f"Channel: {before.channel.mention} \n \n Username: {member } \n User ID: {member.id}", color = 0x00ff00)
		if language == 3:
			embed = discord.Embed(title = f"[{dt_string}] Користувач: {member.name} вийшов з голосового каналу", description = f"Канал: {before.channel.mention} \n \n Ім'я користувача: {member } \n ID користувача: {member.id}", color = 0x00ff00)
		if language == 4:
			embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member.name} выйшаў з галасавога канала", description = f"Канал: {before.channel.mention} \n \n Імя карыстальніка: {member } \n ID карыстальніка: {member.id}", color = 0x00ff00)
		return await channel.send(embed = embed)

	else:
		channel = bot.get_channel( logschannel )
		if language == 1:
			embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member.name} перешёл в голосовой канал", description = f"Канал до: {before.channel.mention}\nКанал после {after.channel.mention} \n \n Имя пользователя: {member} \n ID пользователя: {member.id}", color  = 0x00ff00)
		if language == 2:
			embed = discord.Embed(title = f"[{dt_string}] User: {member.name} moved to voice channel", description = f"Channel before: {before.channel.mention}\nChannel after {after.channel. mention} \n \n Username: {member} \n User ID: {member.id}", color = 0x00ff00)
		if language == 3:
			embed = discord.Embed(title = f"[{dt_string}] Користувач: {member.name} перейшов до голосового каналу", description = f"Канал до: {before.channel.mention}\nКанал після {after.channel. mention} \n \n Ім'я користувача: {member} \n ID користувача: {member.id}", color = 0x00ff00)
		if language == 4:
			embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member.name} перайшоў у галасавы канал", description = f"Канал да: {before.channel.mention}\nКанал пасля {after.channel. mention} \n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}", color = 0x00ff00)
		return await channel.send(embed = embed)

@bot.command(aliases =["prgsstart"])
async def пргсстарт(ctx):
	if language == 1:
		category = await ctx.guild.create_category(name = "◦─◦─◦┃Войс каналы┃◦─◦─◦",position = 0)
		created_channel = await ctx.guild.create_voice_channel(f'╠━⟪➕⟫━╣•Создать', position=1, category=category,bitrate=96000)
	if language == 2:
		category = await ctx.guild.create_category(name = "◦─◦─◦Voice channels┃◦─◦─◦",position = 0)
		created_channel = await ctx.guild.create_voice_channel(f'╠━⟪➕⟫━╣•Create', position=1, category=category,bitrate=96000)
	if language == 3:
		category = await ctx.guild.create_category(name = "◦─◦─◦┃Войс канали┃◦─◦─◦",position = 0)
		created_channel = await ctx.guild.create_voice_channel(f'╠━⟪➕⟫━╣•Створити', position=1, category=category,bitrate=96000)
	if language == 4:
		category = await ctx.guild.create_category(name = "◦─◦─◦┃Войс каналы┃◦─◦─◦",position = 0)
		created_channel = await ctx.guild.create_voice_channel(f'╠━⟪➕⟫━╣•Стварыць', position=1, category=category,bitrate=96000)

	with open('prgs.json') as json_file:
		data = json.load(json_file)
		ss1 = {
			'category': category.id,
			'channel': created_channel.id}

		data.append(ss1)

	with open('prgs.json', 'w') as f:
		json.dump(data, f, indent=4)
#=====================================================================================================================================================================================================

#выгнать
@bot.command(aliases = ["kick", "кік"])
@commands.has_permissions( kick_members = True )	

async def кик(ctx, member: discord.Member, *,reason = None ):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel(banlogchannel)

	await member.kick(reason = reason)
	if language == 1:
		await channel.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был кикнут по причине {reason}", description = f'Модератор **{ctx.author}** кикнул пользователя \n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0x4b0082, timestamp=ctx.message.created_at) )
		await ctx.send(f'Пользователь { member.mention } был кикнут')
	if language == 2:
		await channel.send( embed = discord.Embed(title = f"[{dt_string}] User: {member} was kicked for {reason}", description = f'Moderator **{ctx.author}** kicked user \n \n Username: {member} \n User ID: {member.id}', color = 0x4b0082, timestamp=ctx.message.created_at) )
		await ctx.send(f'User { member.mention } was kicked')	
	if language == 3:
		await channel.send( embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був кікнутий через {reason}", description = f'Модератор **{ctx.author}** кикнув користувача \n \n Ім\'я користувача: {member} \n ID користувача: {member.id}', color = 0x4b0082, timestamp=ctx.message.created_at) )
		await ctx.send(f'Користувач { member.mention } був кікнутий')
	if language == 4:
		await channel.send( embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў кікнуты з прычыны {reason}", description = f'Мадэратар **{ctx.author}** кікнуў карыстальніка \n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}', color = 0x4b0082, timestamp=ctx.message.created_at) )
		await ctx.send(f'Карыстальнік { member.mention } быў кікнуты')
	
#забанить 
@bot.command(aliases = ["ban"])
@commands.has_permissions( ban_members = True )
async def бан(ctx, member: discord.Member, time:int=0, *, reason=None):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	logchannel = bot.get_channel( banlogchannel )
	perms = discord.Permissions(read_messages = True, read_message_history = True)
	guild = ctx.guild
	
	if time == 0:
		time = None
		await member.ban(reason = reason)
		if language == 1:
			await member.send(f'вы были забанены модератором **{ctx.author}** на сервере {guild.name} по причине: {reason}')
			await ctx.send(f'{member.mention} получил бан на неопределённое время по причине: {reason}')
			await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был забанен **{ctx.author}** по причине: {reason} на неопределённое время", description = f'Модератор **{ctx.author}** забанил пользователя \n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
		if language == 2:
			await member.send(f'You were banned by moderator **{ctx.author}** on server {guild.name} for: {reason}')
			await ctx.send(f'{member.mention} banned indefinitely due to: {reason}')
			await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] User: {member} has been banned by **{ctx.author}** for reason: {reason} indefinitely", description = f'Moderator **{ctx.author}** banned user \n \n Username: {member} \n User ID: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
		if language == 3:
			await member.send(f'ви були забанені модератором **{ctx.author}** на сервері {guild.name} через: {reason}')
			await ctx.send(f'{member.mention} отримав бан на невизначений час через: {reason}')
			await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був забанен **{ctx.author}** через: {reason} на невизначений час", description = f'Модератор **{ctx.author}** забанив користувача \n \n Ім\'я користувача: {member} \n ID користувача: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
		if language == 4:
			await member.send(f'вы былі забанены мадэратарам **{ctx.author}** на серверы {guild.name} з прычыны: {reason}')
			await ctx.send(f'{member.mention} атрымаў бан на нявызначаны час з прычыны: {reason}')
			await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў забанены **{ctx.author}** па прычыне: {reason} на нявызначаны час", description = f'Мадэратар **{ctx.author}** забаніў карыстальніка \n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )

	else:
		await member.ban(reason = reason)
		if language == 1:
			await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был забанен **{ctx.author}** по причине: {reason} на {time} минут", description = f'Модератор **{ctx.author}** забанил пользователя \n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
			await ctx.send(f'{member.mention} получил бан на `{time}` минут по причине: **{reason}**')
		if language == 2:
			await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] User: {member} was banned by **{ctx.author}** for: {reason} for {time} minutes", description = f'Moderator **{ctx.author}** banned user \n \n Username: {member} \n User ID: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
			await ctx.send(f'{member.mention} got banned for `{time}` minutes due to: **{reason}**')
		if language == 3:
			await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був забанен **{ctx.author}** через: {reason} на {time} хвилин", description = f'Модератор **{ctx.author}** забанив користувача \n \n Ім\'я користувача: {member} \n ID користувача: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
			await ctx.send(f'{member.mention} отримав бан на `{time}` хвилин через: **{reason}**')
		if language == 4:
			await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў забанены **{ctx.author}** па прычыне: {reason} на {time} хвілін", description = f'Мадэратар **{ctx.author}** забаніў карыстальніка \n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
			await ctx.send(f'{member.mention} атрымаў бан на `{time}` хвілін па прычыне: **{reason}**')
		await asyncio.sleep(time * 60)

		baned_users = await ctx.guild.bans()

		for ban_entry in baned_users:
			user = ban_entry.user

			await ctx.guild.unban(user)
			if language == 1:
				await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был разбанен ", description = f' Время наказания прошло \n \n Имя пользователя: {member.name} \n ID пользователя: {member.id}' , color = 0xf5deb3, timestamp=ctx.message.created_at ) )
			if language == 2:
				await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] User: {member} was unbanned ", description = f' Punishment time has passed \n \n Username: {member.name} \n User ID: {member.id}' , color = 0xf5deb3, timestamp=ctx.message.created_at ) )
			if language == 3:
				await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був розбанений ", description = f' Час покарання минуло \n \n Ім\'я користувача: {member.name} \n ID користувача: {member.id}' , color = 0xf5deb3, timestamp=ctx.message.created_at ) )
			if language == 4:
				await logchannel.send( embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў разбанены ", description = f' Час пакарання прайшоў \n \n Імя карыстальніка: {member.name} \n ID карыстальніка: {member.id}' , color = 0xf5deb3, timestamp=ctx.message.created_at ) )

			return
#разбан
@bot.command(aliases=["unban", "розбан"])
@commands.has_permissions( ban_members = True )

async def разбан(ctx, *, member ):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel( banlogchannel )

	baned_users = ctx.guild.bans()

	async for entry in baned_users:
		user = entry.user

		await ctx.guild.unban(user)
		if language == 1:
			await ctx.send(f'Пользователь {user.mention} был разбанен')
			await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был разбанен", description = f'Модератор **{ctx.author}** разбанил пользователя \n \n    ID пользователя: {member}', color = 0xf5deb3, timestamp=ctx.message.created_at ) )
		if language == 2:
			await ctx.send(f'User {user.mention} has been unbanned')
			await channel.send(embed = discord.Embed(title = f"[{dt_string}] User: {member} was unbanned", description = f'Moderator **{ctx.author}** unbanned user \n \n ID user: {member}', color = 0xf5deb3, timestamp=ctx.message.created_at ) )
		if language == 3:
			await ctx.send(f'Користувач {user.mention} був розбанений')
			await channel.send(embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був розбанений", description = f'Модератор **{ctx.author}** розбанив користувача \n \n ID користувача: {member}', color = 0xf5deb3, timestamp=ctx.message.created_at ) )
		if language == 4:
			await ctx.send(f'Карыстальнік {user.mention} быў разбанены')
			await channel.send(embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў разбанены", description = f'Мадэратар **{ctx.author}** разбаніў карыстальніка \n \n ID карыстальніка: {member}', color = 0xf5deb3, timestamp=ctx.message.created_at ) )

		return

#мьют
@bot.command(aliases = ["mute", "м'ють", "м'юць"])
@commands.has_permissions( kick_members = True )
async def мьют(ctx, member: discord.Member, time: int =0, *, reason=None):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel1 = bot.get_channel( mutelogchannel )
	perms = discord.Permissions(read_messages = True, read_message_history = True)
	guild = ctx.guild
	if language == 1:
		mute_role = discord.utils.get( ctx.message.guild.roles, name = 'мьют')
	if language == 2:
		mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute')
	if language == 3:
		mute_role = discord.utils.get( ctx.message.guild.roles, name = 'м\'ють')
	if language == 4:
		mute_role = discord.utils.get( ctx.message.guild.roles, name = 'м\'юць')

	if member.id == 638362085922701333:
		await ctx.send('Ага, хер тебе')
		return

	if mute_role == None:
		if language == 1:
			mute_role = await ctx.guild.create_role(name='мьют', permissions=perms)
		if language == 2:
			mute_role = await ctx.guild.create_role(name='mute', permissions=perms)
		if language == 3:
			mute_role = await ctx.guild.create_role(name='м\'ють', permissions=perms)
		if language == 4:
			mute_role = await ctx.guild.create_role(name='м\'юць', permissions=perms)
		await mute_role.edit(color=discord.Color(0x378cdc))
		for channel in guild.channels:
			await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)

	await member.add_roles(mute_role)
	await member.move_to(None)

	if time == 0:
		time = None
		if language == 1:
			await ctx.send(f'{member.mention} получил мьют на неопределённое время по причине: {reason}')
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на неопределённое время", description = f'Модератор **{ctx.author}** замьютил пользователя \n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
		if language == 2:
			await ctx.send(f'{member.mention} got muted indefinitely due to: {reason}')
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] User: {member} was muted for: {reason} indefinitely", description = f'Moderator **{ctx.author} ** muted user \n \n Username: {member} \n User ID: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
		if language == 3:
			await ctx.send(f'{member.mention} отримав м\'ют на невизначений час через: {reason}')
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був зам'ючений через: {reason} на невизначений час", description = f'Модератор **{ctx.author} ** зам\'ютив користувача \n \n Ім\'я користувача: {member} \n ID користувача: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
		if language == 4:
			await ctx.send(f'{member.mention} атрымаў м\'ют на нявызначаны час з прычыны: {reason}')
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў зам'ючаны з прычыны: {reason} на нявызначаны час", description = f'Мадэратар **{ctx.author} ** зам\'юціў карыстальніка \n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )		
	else:
		if language == 1:
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на {time} минут", description = f'Модератор **{ctx.author}** замьютил пользователя \n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
			await ctx.send(f'{member.mention} получил мьют на {time} минут по причине: {reason}')
			await asyncio.sleep(time * 60)
			await member.remove_roles(mute_role)
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был размьючен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
		if language == 2:
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] User: {member} was muted for: {reason} for {time} minutes", description = f'Moderator **{ctx. author}** muted user \n \n Username: {member} \n User ID: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
			await ctx.send(f'{member.mention} got mute for {time} minutes due to: {reason}')
			await asyncio.sleep(time * 60)
			await member.remove_roles(mute_role)
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] User: {member} has been muted ", description = f' Punishment time has passed \n \n Username: {member} \n User ID : {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
		if language == 3:
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був зам'ючений через: {reason} на {time} хвилин", description = f'Модератор **{ctx. author}** зам\'ютив користувача \n \n Ім\'я користувача: {member} \n ID користувача: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
			await ctx.send(f'{member.mention} отримав м\'ют на {time} хвилин через: {reason}')
			await asyncio.sleep(time * 60)
			await member.remove_roles(mute_role)
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був розм'ючений ", description = f' Час покарання минуло \n \n Ім\'я користувача: {member} \n ID користувача : {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
		if language == 4:
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў зам'ючаны з прычыны: {reason} на {time} хвілін", description = f'Мадэратар **{ctx. author}** зам\'юціў карыстальніка \n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
			await ctx.send(f'{member.mention} атрымаў м\'ют на {time} хвілін з прычыны: {reason}')
			await asyncio.sleep(time * 60)
			await member.remove_roles(mute_role)
			await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў разм'ючаны ", description = f' Час пакарання прайшоў \n \n Імя карыстальніка: {member} \n ID карыстальніка : {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )

#размут
@bot.command(aliases =["unmute", "розм'ють", "разм'юць"])
@commands.has_permissions( kick_members = True )
async def размьют(ctx, member: discord.Member ):
	channel = bot.get_channel( mutelogchannel )
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	mute_role1 = discord.utils.get( ctx.message.guild.roles, name = 'мьют')
	mute_role2 = discord.utils.get( ctx.message.guild.roles, name = 'mute')
	mute_role3 = discord.utils.get( ctx.message.guild.roles, name = 'м\'ють')
	mute_role4 = discord.utils.get( ctx.message.guild.roles, name = 'м\'юць')

	if mute_role1 != None:
		await member.remove_roles( mute_role1 )
	elif mute_role2 != None:
		await member.remove_roles( mute_role2 )
	elif mute_role3 != None:
		await member.remove_roles( mute_role3 )
	elif mute_role4 != None:
		await member.remove_roles( mute_role4 )
	else:
		pass
	if language == 1:
		await ctx.send(f'Пользователь { member.mention } был размьючен')
		await channel.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был разьючен", description = f'Модератор **{ctx.author}** размутил пользователя \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
	if language == 2:
		await ctx.send(f'User { member.mention } was unmuted')
		await channel.send( embed = discord.Embed(title = f"[{dt_string}] User: {member} has been unbundled", description = f'Moderator **{ctx.author}** has unbundled user \n \n Name user: {member} \n user ID: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
	if language == 3:
		await ctx.send(f'Користувач { member.mention } був розм\'ючений')
		await channel.send( embed = discord.Embed(title = f"[{dt_string}] Користувач: {member} був розлючений", description = f'Модератор **{ctx.author}** розмутив користувача \n \n Ім\'я користувача: {member} \n ID користувача: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
	if language == 4:
		await ctx.send(f'Карыстальнік { member.mention } быў разм\'ючаны')
		await channel.send( embed = discord.Embed(title = f"[{dt_string}] Карыстальнік: {member} быў раз'юшаны", description = f'Мадэратар **{ctx.author}** размуціў карыстальніка \n \n Імя карыстальніка: {member} \n ID карыстальніка: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )

#удаление сообщений ( .clear [количество сообщений с учётом самой комманды])
@bot.command(aliases = ["clear", "очистити", "ачысціць"])
async def очистить( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )

#создвремроль
@bot.command(aliases = ["createmprole", "стварчасролю", "створтимчасроль"])
@commands.has_permissions( kick_members = True )
async def создвремроль(ctx, time: int, udalenie = True, member: discord.Member = None, *,rolename):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel( logschannel )
	guild = ctx.guild	
	if member != None:
		role = await guild.create_role(name= rolename )
		await role.edit(color=discord.Color( 0xbf61ff ))
		await member.add_roles(role)
		if language == 1:
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] Пользователь {ctx.author}, создал временную роль "{rolename}" для {member} на {time} минут \n \n Удаление: {udalenie}', description = f'Имя пользователя: {ctx.author} \n ID пользователя: {ctx.author.id}'))
			await ctx.send(f'Роль **{rolename}** была выдана **{member}**.\n Роль будет снята через {time} минут.')
			await asyncio.sleep(time * 60)
			await member.remove_roles(role)
			if udalenie == True:
				await role.delete()
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] "{rolename}" удалена. \n {time} минут прошло', description = f'Имя пользователя: {ctx.author} \n ID пользователя: {ctx.author.id}'))
		if language == 2:
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] User {ctx.author}, created temporary role "{rolename}" for {member} for {time} minutes \n \n Deleting: {delete}', description = f'Username: {ctx.author} \n UserID: {ctx.author.id}'))
			await ctx.send(f'Role **{rolename}** has been given to **{member}**.\n Role will be removed in {time} minutes.')
			await asyncio.sleep(time * 60)
			await member.remove_roles(role)
			if udalenie == True:
				await role.delete()
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] "{rolename}" removed. \n {time} minutes have passed', description = f'Username: {ctx.author} \n User ID: {ctx.author.id}'))
		if language == 3:
			await channel.send(embed = discord.Embed(title = f'[{dt_string}]) Пользователь {ctx.author} создал временную роль "{rolename}" для {member} на {time} минут \n \n Удаление: {udalenie}', description = f'Имя пользователя: {ctx.author} \n ID пользователя: {ctx.author.id}'))
			await ctx.send(f'Роль **{rolename}** была издана **{member}**.\nРоль будет снята через {time} минут.')
			await asyncio.sleep(time * 60)
			await member.remove_roles(role)
			if udalenie == True:
				await role.delete()
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] "{rolename}" удалена. \n {time} минут прошло', description = f'Имя пользователя: {ctx.author} \n ID пользователя: {ctx.author.id}'))
		if language == 4:
			await channel.send(embed = discord.Embed(title = f'[{dt_string}]) Карыстальнік {ctx.author} стварыў часовую ролю "{rolename}" для {member} на {time} хвілін \n \n Выдаленне: {udalenie}', description = f'Імя карыстальніка: {ctx.author} \n ID карыстальніка: {ctx.author.id}'))
			await ctx.send(f'Роля **{rolename}** была выдадзена **{member}**.\n Роля будзе знята праз {time} хвілін.')
			await asyncio.sleep(time * 60)
			await member.remove_roles(role)
			if udalenie == True:
				await role.delete()
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] "{rolename}" выдалена. \n {time} хвілін прайшло', description = f'Імя карыстальніка: {ctx.author} \n ID карыстальніка: {ctx.author.id}'))
	else:
		role = await guild.create_role(name= rolename )
		await role.edit(color=discord.Color(0xbf61ff))
		if language == 1:
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] Пользователь {ctx.author}, создал временную роль "{rolename}" на {time} минут \n Удаление: {udalenie}', description = f'Имя пользователя: {ctx.author} \n ID пользователя: {ctx.author.id}'))
			await ctx.send(f'Роль **{rolename}** была создана. \n Роль будет удалена через {time} минут.')
			await asyncio.sleep(time * 60)
			await role.delete()
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] "{rolename}" удалена. \n {time} минут прошло', description = f'Имя пользователя: {ctx.author} \n ID пользователя: {ctx.author.id}'))
		if language == 2:
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] User {ctx.author}, created temporary role "{rolename}" for {time} minutes \n Deletion: {delete}', description = f'Username: {ctx.author} \n User ID: {ctx.author.id}'))
			await ctx.send(f'The role **{rolename}** has been created. \n The role will be deleted in {time} minutes.')
			await asyncio.sleep(time * 60)
			await role.delete()
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] "{rolename}" removed. \n {time} minutes have passed', description = f'Username: {ctx.author} \n User ID: {ctx.author.id}'))
		if language == 3:
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] Користувач {ctx.author}, створив тимчасову роль "{rolename}" на {time} хвилин \n Видалення: {udalenie}', description = f'Ім\'я користувача: {ctx.author} \n ID користувача: {ctx.author.id}'))
			await ctx.send(f'Роль **{rolename}** була створена. \n Роль буде видалена через {time} хвилин.')
			await asyncio.sleep(time * 60)
			await role.delete()
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] "{rolename}" видалено. \n {time} хвилин минуло', description = f'Ім\'я користувача: {ctx.author} \n ID користувача: {ctx.author.id}'))
		if language == 4:
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] Пользователь {ctx.author}, створыўшы часовую ролю "{rolename}" на {time} хвілін \n Відалення: {udalenie}', description = f'Ім\'я карыстальніка: {ctx.author} \n ID карыстальніка: {ctx.author.id}'))
			await ctx.send(f'Роля **{rolename}** была створана. \n Роля будзе выдалена праз {time} хвілін.')
			await asyncio.sleep(time * 60)
			await role.delete()
			await channel.send(embed = discord.Embed(title = f'[{dt_string}] "{rolename}" выдалена. \n {time} хвілін мінула', description = f'Ім\'я карыстальніка: {ctx.author} \n ID карыстальніка: {ctx.author.id}'))






#времроль
@bot.command(aliases = ["temprole", "тимчаcроль", "часроля"])
@commands.has_permissions( ban_members = True )
async def времроль(ctx, time: int, member: discord.Member, * ,rolename):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel( logschannel )
	guild = ctx.guild
	role = discord.utils.get( ctx.message.guild.roles, name = rolename)
	role1 = discord.utils.get( ctx.message.guild.roles, mention = rolename)
	if language == 1:
		if role != None:
			if role <= ctx.author.top_role:
				await member.add_roles(role)
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] Пользователь {ctx.author}, выдал временный доступ к роли "{rolename}" для {member} на {time} минут', description = f'Имя пользователя: {ctx.author} \n ID пользователя: {ctx.author.id}'))
				await ctx.send(f'Роль **{rolename}** была выдана **{member}**.\n Роль будет снята через {time} минут.')
				await asyncio.sleep(time * 60)
				await member.remove_roles(role)
			else:
				await ctx.send('Ваша наивысшая роль находится ниже указанной')
		elif role1 != None:
			if role1 <= ctx.author.top_role:
				await member.add_roles(role1)
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] Пользователь {ctx.author}, выдал временный доступ к роли "{rolename}" для {member} на {time} минут', description = f'Имя пользователя: {ctx.author} \n ID пользователя: {ctx.author.id}'))
				await ctx.send(f'Роль **{rolename}** была выдана **{member}**.\n Роль будет снята через {time} минут.')
				await asyncio.sleep(time * 60)
				await member.remove_roles(role1)
			else:
				await ctx.send('Ваша наивысшая роль находится ниже указанной')
		else: 
			await ctx.send('Данной роли не существует, либо название указано неверно')
	if language == 2:
		if role != None:
			if role <= ctx.author.top_role:
				await member.add_roles(role)
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] User {ctx.author}, granted temporary access to role "{rolename}" to {member} for {time} minutes', description = f'Username: {ctx.author} \n User ID: {ctx.author.id}'))
				await ctx.send(f'Role **{rolename}** has been given to **{member}**.\n Role will be removed in {time} minutes.')
				await asyncio.sleep(time * 60)
				await member.remove_roles(role)
		elif role1 != None:
			if role <= ctx.author.top_role:
				await member.add_roles(role)
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] User {ctx.author}, granted temporary access to role "{rolename}" to {member} for {time} minutes', description = f'Username: {ctx.author} \n User ID: {ctx.author.id}'))
				await ctx.send(f'Role **{rolename}** has been given to **{member}**.\n Role will be removed in {time} minutes.')
				await asyncio.sleep(time * 60)
				await member.remove_roles(role)
			else:
				await ctx.send('Your highest role is below this one')
		else:
			await ctx.send('This role does not exist or the name is incorrect')
	if language == 3:
		if role != None:
			if role <= ctx.author.top_role:
				await member.add_roles(role)
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] Користувач {ctx.author}, видав тимчасовий доступ до ролі "{rolename}" для {member} на {time} хвилин', description = f'Ім\'я користувача: {ctx.author} \n ID користувача: {ctx.author.id}'))
				await ctx.send(f'Роль **{rolename}** була видана **{member}**.\n Роль буде знята через {time} хвилин.')
				await asyncio.sleep(time * 60)
				await member.remove_roles(role)
		elif role1 != None:
			if role <= ctx.author.top_role:
				await member.add_roles(role)
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] Користувач {ctx.author}, видав тимчасовий доступ до ролі "{rolename}" для {member} на {time} хвилин', description = f'Ім\'я користувача: {ctx.author} \n ID користувача: {ctx.author.id}'))
				await ctx.send(f'Роль **{rolename}** була видана **{member}**.\n Роль буде знята через {time} хвилин.')
				await asyncio.sleep(time * 60)
				await member.remove_roles(role)
			else:
				await ctx.send('Ваша найвища роль знаходиться нижче вказаної')
		else:
			await ctx.send('Даної ролі не існує, або назва вказана неправильно')
	if language == 4:
		if role != None:
			if role <= ctx.author.top_role:
				await member.add_roles(role)
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] Карыстальнік {ctx.author}, выдаў часовы доступ да ролі "{rolename}" для {member} на {time} хвілін', description = f'Імя карыстальніка: {ctx.author} \n ID карыстальніка: {ctx.author.id}'))
				await ctx.send(f'Роля **{rolename}** была выдадзена **{member}**.\n Роля будзе знята праз {time} хвілін.')
				await asyncio.sleep(time * 60)
				await member.remove_roles(role)
		elif role1 != None:
			if role <= ctx.author.top_role:
				await member.add_roles(role)
				await channel.send(embed = discord.Embed(title = f'[{dt_string}] Карыстальнік {ctx.author}, выдаў часовы доступ да ролі "{rolename}" для {member} на {time} хвілін', description = f'Імя карыстальніка: {ctx.author} \n ID карыстальніка: {ctx.author.id}'))
				await ctx.send(f'Роля **{rolename}** была выдадзена **{member}**.\n Роля будзе знята праз {time} хвілін.')
				await asyncio.sleep(time * 60)
				await member.remove_roles(role)
			else:
				await ctx.send('Ваша найвышэйшая роля знаходзіцца ніжэй паказанай')
		else:
			await ctx.send('Гэтай ролі не існуе, альбо назва пазначана памылкова')

class EmojiInfo(commands.Bot):
    def __init__(bot):
        self.bot = bot

    @bot.command(name="emoji", aliases=["эмодзи", "емодзі"])
    async def emoji(ctx, emoji: discord.Emoji = None):
        if language == 1:
            if not emoji:
                pass
            try:
                emoji = await emoji.guild.fetch_emoji(emoji.id)
            except discord.NotFound:
                return await ctx.send("Я не смог найти этот смайлик в данной гильдии.")

            time = ctx.message.created_at
            is_managed = "ДА" if emoji.managed else "Нет"
            is_animated = "Да" if emoji.animated else "Нет"
            requires_colons = "Да" if emoji.require_colons else "Нет"
            creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
            can_use_emoji = (
                "Все"
                if not emoji.roles
                else " ".join(role.name for role in emoji.roles)
            )

            description = f"""
            **Основное**
            **- Название:** {emoji.name}
            **- ID:** {emoji.id}
            **- URL:** [Link To Emoji]({emoji.url})
            **- Автор эмодзи:** {emoji.user.mention}
            **- Создан:** {creation_time}
            **- Могут использовать:** {can_use_emoji}
            
            **Дополнительно**
            **- Анимированный:** {is_animated}
            **- Управляемый:** {is_managed}
            **- Требуются двоеточия:** {requires_colons}
            **- Имя сервера:** {emoji.guild.name}
            **- ID сервера:** {emoji.guild.id}
            """

            embed = discord.Embed(
                title=f"**Информация об эмодзи:** `{emoji.name}`",
                description=description,
                colour=0xADD8E6,
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url=emoji.url)
            embed.set_footer(text=f"\n  Команду вызвал: {ctx.author},\n ID: ({ctx.author.id})")
            await ctx.send(embed=embed)
        if language == 2:
            if not emoji:
                pass
            try:
                emoji = await emoji.guild.fetch_emoji(emoji.id)
            except discord.NotFound:
                return await ctx.send("I couldn't find this emoji in this guild.")

            time = ctx.message.created_at
            is_managed = "YES" if emoji.managed else "No"
            is_animated = "Yes" if emoji.animated else "No"
            requires_colons = "Yes" if emoji.require_colons else "No"
            creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
            can_use_emoji = (
                "All"
                if not emoji.roles
                else " ".join(role.name for role in emoji.roles)
            )

            description = f"""
            **Basic**
            **- Name:** {emoji.name}
            **-ID:** {emoji.id}
            **- URL:** [Link To Emoji]({emoji.url})
            **- Emoji Author:** {emoji.user.mention}
            **- Created:** {creation_time}
            **- Can use:** {can_use_emoji}
            
            **Additionally**
            **- Animated:** {is_animated}
            **- Managed:** {is_managed}
            **- Colons required:** {requires_colons}
            **- Server name:** {emoji.guild.name}
            **- Server ID:** {emoji.guild.id}
            """

            embed = discord.Embed(
                title=f"**Emoji Info:** `{emoji.name}`",
                description=description,
                colour=0xADD8E6,
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url=emoji.url)
            embed.set_footer(text=f"\n Command called: {ctx.author},\n ID: ({ctx.author.id})")
            await ctx.send(embed=embed)
        if language == 3:
            if not emoji:
                pass
            try:
                emoji = await emoji.guild.fetch_emoji(emoji.id)
            except discord.NotFound:
                return await ctx.send("Я не зміг знайти цей смайлик у даній гільдії.")

            time = ctx.message.created_at
            is_managed = "ТАК" if emoji.managed else "Ні"
            is_animated = "Так" if emoji.animated else "Ні"
            requires_colons = "Так" if emoji.require_colons else "Ні"
            creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
            can_use_emoji = (
                "Всі"
                if not emoji.roles
                else " ".join(role.name for role in emoji.roles)
            )

            description = f"""
            **Основне**
            **- Назва: ** {emoji.name}
            **- ID:** {emoji.id}
            **- URL:** [Link To Emoji]({emoji.url})
            **- Автор емодзі: ** {emoji.user.mention}
            **- Створено:** {creation_time}
            **- Можуть використовувати: ** {can_use_emoji}
            
            **Додатково**
            **- Анімований:** {is_animated}
            ** - Керований: ** {is_managed}
            **- Потрібні двокрапки:** {requires_colons}
            **- Ім'я сервера:** {emoji.guild.name}
            **- ID сервера: ** {emoji.guild.id}
            """

            embed = discord.Embed (
                title=f"**Інформація про емодзі:** `{emoji.name}`",
                description=description,
                colour=0xADD8E6,
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url=emoji.url)
            embed.set_footer(text=f"\n Команду викликав: {ctx.author},\n ID: ({ctx.author.id})")
            await ctx.send(embed=embed)
        if language == 4:
            if not emoji:
                pass
            try:
                emoji = await emoji.guild.fetch_emoji(emoji.id)
            except discord.NotFound:
                return await ctx.send("Я не змог знайсці гэты смайлік у дадзенай гільдыі.")

            time = ctx.message.created_at
            is_managed = "ТАК" if emoji.managed else "Не"
            is_animated = "Так" if emoji.animated else "Не"
            requires_colons = "Так" if emoji.require_colons else "Не"
            creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
            can_use_emoji = (
                "Усе"
                if not emoji.roles
                else " ".join(role.name for role in emoji.roles)
            )

            description = f"""
            **Асноўнае**
            **- Назва:** {emoji.name}
            **- ID:** {emoji.id}
            **- URL:** [Link To Emoji]({emoji.url})
            **- Аўтар эмодзі:** {emoji.user.mention}
            **- Створаны:** {creation_time}
            **- Могуць выкарыстоўваць:** {can_use_emoji}
            
            **Дадаткова**
            **- Аніміраваны:** {is_animated}
            **- Кіраваны:** {is_managed}
            **- Патрабуюцца двукроп'я:** {requires_colons}
            **- Імя сервера:** {emoji.guild.name}
            **- ID сервера:** {emoji.guild.id}
            """

            embed = discord.Embed(
                title=f"**Інфармацыя аб эмодзі:** `{emoji.name}`",
                description=description,
                colour=0xADD8E6,
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url=emoji.url)
            embed.set_footer(text=f"\n Каманду выклікаў: {ctx.author},\n ID: ({ctx.author.id})")
            await ctx.send(embed=embed)

#комманда осебе
@bot.command(aliases = ["AboutMe","просебе", "прасябе"])
async def осебе(ctx):
	if language == 1:
		await ctx.send(
			'```cs\nМеня зовут Kara$1k, я многофункциональный бот версии 1.10.2 .'
			'Я создан smetаnka_v_dele#7556'
			f'\nЯ существую для поддержания порядка на сервере. Мой префикс "{prefix}"'
			'\nВ меня входят:'
			'\n.1)Система аудита'
			'\n.2)Большое количество модераторских команд'
			'\n.3)Система уровней'
			'\n.4)Уникальная система отзывов'
			'\n.5)Динамическая статистика'
			'\n.6)Роли за реакцию'
			'\n.7)Тикеты'
			'\n.8)Приватные войс каналы'
			'\n.5)Сторонние команды для пользователей'
			'\nМои приемущества:'
			'\n.1)Поддержка 4 языков (Русский, Английский, Украинский, Беларусский)'
			'\n.2)Все необходимые команды в одном боте.'
			f'\nболее подробно можно ознакомится с командами введя в чат "{prefix}команды" '
			'\n\n Бот сделан на языке программирования Python 3.8.7'
			'\nСервер разработчика: https://discord.gg/EKq9XGq4Q8'
			'\n\n Создатель: smetаnka_v_dele#7556 \n (ツ)'
			'\n```'
			)
	if language == 2:
		await ctx.send(
			'```cs\nMy name is Kara$1k, I am a feature rich bot version 1.10.2 .'
			'I was created by smetanka_v_dele#7556'
			f'\nI exist to maintain order on the server. My prefix is "{prefix}"'
			'\nMe includes:'
			'\n.1)Audit system'
			'\n.2)Too many moderator commands'
			'\n.3)Level system'
			'\n.4)Unique feedback system'
			'\n.5)Dynamic statistics'
			'\n.6)Reaction roles'
			'\n.7)Tickets'
			'\n.8)Private voice channels'
			'\n.5)Third party commands for users'
			'\nMy perks:'
			'\n.1)Support 4 languages (Russian, English, Ukrainian, Belarusian)'
			'\n.2)All necessary commands in one bot.'
			f'\nFor more information on commands, enter "{prefix}commands" into the chat '
			'\n\n Bot is made in Python 3.8.7 programming language'
			'\nDeveloper server: https://discord.gg/EKq9XGq4Q8'
			'\n\n Creator: smetanka_v_dele#7556 \n (ツ)'
			'\n```'
			)
	if language == 3:
		await ctx.send(
			'```cs\nМене звуть Kara$1k, я багатофункціональний бот версії 1.10.2 .'
			'Я створений smetаnka_v_dele#7556'
			f'\nЯ існую для підтримки порядку на сервері. Мій префікс "{prefix}"'
			'\nВ мене входять:'
			'\n.1)Система аудиту'
			'\n.2) Велика кількість модераторських команд'
			'\n.3) Система рівнів'
			'\n.4)Унікальна система відгуків'
			'\n.5) Динамічна статистика'
			'\n.6)Роли за реакцію'
			'\n.7)Тикети'
			'\n.8)Приватні війс канали'
			'\n.5) Сторонні команди для користувачів'
			'\nМої переваги:'
			'\n.1)Підтримка 4 мов (Російська, Англійська, Українська, Білоруська)'
			'\n.2)Всі необхідні команди в одному боті.'
			f'\nдокладніше можна ознайомитися з командами ввівши в чат "{prefix}команди" '
			'\n\n Бот зроблений мовою програмування Python 3.8.7'
			'\nСервер розробника: https://discord.gg/EKq9XGq4Q8'
			'\n\n Творець: smetаnka_v_dele#7556 \n (ツ)'
			'\n```'
			)
	if language == 4:
		await ctx.send(
			'```cs\nМяне клічуць Kara$1k, я шматфункцыянальны бот версіі 1.10.2 .'
			'Я створаны smetаnka_v_dele#7556'
			f'\nЯ існую для падтрымання парадку на серверы. Мой прэфікс "{prefix}"'
			'\nУ мяне ўваходзяць:'
			'\n.1)Сістэма аўдыту'
			'\n.2)Вялікая колькасць мадэратарскіх каманд'
			'\n.3)Сістэма ўзроўняў'
			'\n.4)Унікальная сістэма водгукаў'
			'\n.5)Дынамічная статыстыка'
			'\n.6)Ралі за рэакцыю'
			'\n.7)Тыкеты'
			'\n.8)Прыватныя войс каналы'
			'\n.5)Бачныя каманды для карыстальнікаў'
			'\nМае перавагі:'
			'\n.1)Падтрымка 4 моў (Руская, Англійская, Украінская, Беларуская)'
			'\n.2)Усе неабходныя каманды ў адным боце.'
			f'\nбольш падрабязна можна азнаёміцца з камандамі увёўшы ў чат "{prefix}каманды" '
			'\n\n Бот зроблены на мове праграмавання Python 3.8.7'
			'\nСервер распрацоўніка: https://discord.gg/EKq9XGq4Q8'
			'\n\n Стваральнік: smetаnka_v_dele#7556 \n (ツ)'
			'\n```'
			)

@bot.command()
async def команды(ctx):
	role0 = discord.utils.find(lambda r: r.id == Krole, ctx.message.guild.roles)
	role1 = discord.utils.find(lambda r: r.id == Rrole, ctx.message.guild.roles)
	role2 = discord.utils.find(lambda r: r.id == Arole, ctx.message.guild.roles)

	if role0 in ctx.author.roles:
		select = Select(
			placeholder="Выберите категорию",
			options= [
				discord.SelectOption(
					label= "Общедоступные команды", 
					emoji= '📘',
					description='Команды доступные всем пользователям сервера.', 
				),
				discord.SelectOption(
					label= "Команды администрации", 
					emoji= '🔩',
					description='Категория команд доступная администраторам.' 
				),
				discord.SelectOption(
					label= "Команды уровней", 
					emoji= '📗',
					description='Хотите посмотреть свой уровень? Жмите сюда.'
				),
				discord.SelectOption(
					label= "Команды отзывов и статистики", 
					emoji= '📊',
					description='Желаете оставить отзыв об ивенте? Этот раздел для вас.'
				),
				discord.SelectOption(
					label= "Сторонние команды", 
					emoji= '📕',
					description='Необходимая команда не подходит не под один из критериев? Вам сюда.'
				)
				
			],
		)
		async def my_callbak(interaction):
			if {select.values[0]} == {'Общедоступные команды'}:
				embed = discord.Embed(title = f"Список общедоступных команд", color = 0x628ffe, timestamp=ctx.message.created_at, )
				embed.add_field(name="Общедоступные команды", value=f"`{prefix}осебе` `{prefix}команды` `{prefix}пинг` `{prefix}аватар` `{prefix}юзер` `{prefix}сервер` `{prefix}эмодзи` `{prefix}хелп`")
				embed.set_footer(text=f'"Общедоступные команды" - это команды доступные всем пользователям сервера, за исключением пользователей в мьюте.\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Команды администрации'}:
				embed = discord.Embed(title = f"Список команд Администрации", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды администрации", value=f"`{prefix}бан` `{prefix}разбан` `{prefix}кик` `{prefix}мьют` `{prefix}размьют` `{prefix}пред` `{prefix}снятьпред` `{prefix}сброспред` `{prefix}преды` `{prefix}очистить` `{prefix}создвремроль` `{prefix}времроль` `{prefix}таблварн` ")
				embed.set_footer(text=f'"Команды администрации" - это команды доступные администрации сервера и выше уполномоченным людям\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Команды уровней'}:
				embed = discord.Embed(title = f"Список команд Уровней", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды системы уровней", value=f"`{prefix}стата` `{prefix}чарт` `{prefix}добранг` `{prefix}обнулить` `{prefix}обстав`")
				embed.set_footer(text=f'"Команды уровней" - это команды для взаимодействия с ситемой уровней\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Команды отзывов и статистики'}:
				embed = discord.Embed(title = f"Список команд отзывов и статистики", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды отзывов и статистики", value=f" `{prefix}статчат` `{prefix}обновстатчат` `{prefix}ивент` `{prefix}администрация` `{prefix}сбростабливт` `{prefix}сбростабладм` `{prefix}удалитьотзывивт` `{prefix}удалитьотзывадм` `{prefix}снятьотзывивт` `{prefix}снятьотзывадм` `{prefix}табладм` `{prefix}табливт`")
				embed.set_footer(text=f'"Команды отзывов и статистики" - это команды для взаиводествия с системой отзывов и статистики(категория чатов отображающая кол. пользователей, ботов и тд)\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Сторонние команды'}:
				embed = discord.Embed(title = f"Список список сторонних команд", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Сторонние команды", value=f"`{prefix}рекроль` `{prefix}тикстарт` `{prefix}тикобнов` `{prefix}пргсстарт`")			
				embed.set_footer(text=f'"Сторонние команды" - это одиночные команды не подходящие ни к одной из категорий выше. На данный момент в эту категорию входят команды системы тикетов, ролей за реакцию, приватных войс каналов\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)

		select.callback = my_callbak
		view = View()
		view.add_item(select)

		embed = discord.Embed(title = f"Список команд уровня: Редактор", color = 0x628ffe, timestamp=ctx.message.created_at)
		embed.add_field(
			name="Команды администрации", value=f"`{prefix}бан` `{prefix}разбан` `{prefix}кик` `{prefix}мьют` `{prefix}размьют` `{prefix}пред` `{prefix}снятьпред` `{prefix}сброспред` `{prefix}преды` `{prefix}очистить` `{prefix}создвремроль` `{prefix}времроль` `{prefix}таблварн` "
			)
		embed.add_field(
			name="Общедоступные команды", value=f"`{prefix}осебе` `{prefix}команды` `{prefix}пинг` `{prefix}аватар` `{prefix}юзер` `{prefix}сервер` `{prefix}эмодзи` `{prefix}хелп`"
			)
		embed.add_field(
			name="Команды системы уровней", value=f"`{prefix}стата` `{prefix}чарт` `{prefix}добранг` `{prefix}обнулить` `{prefix}обстав`"
			)
		embed.add_field(
			name="Команды отзывов и статистики", value=f" `{prefix}статчат` `{prefix}обновстатчат` `{prefix}ивент` `{prefix}администрация` `{prefix}сбростабливт` `{prefix}сбростабладм` `{prefix}удалитьотзывивт` `{prefix}удалитьотзывадм` `{prefix}снятьотзывивт` `{prefix}снятьотзывадм` `{prefix}табладм` `{prefix}табливт`"
			)
		embed.add_field(
			name="Сторонние команды", value=f"`{prefix}рекроль` `{prefix}тикстарт` `{prefix}тикобнов` `{prefix}пргсстарт`"
			)
		embed.add_field(
			name="Секретные команды", value=f"`{prefix}ПЕЧЕНЕГР` `{prefix}Neon` `{prefix}BreadCat` `{prefix}OmerX`"
			)
		embed.set_footer(text=f'Список уровня "Редактор" является полным списком всех команд, начиная от самых обычных, заканчивая системными командами. \nМой префикс "{prefix}". \nДля подробной информации о команде пропишите ({prefix}хелп название_команды) \nКоманду вызвал: {ctx.author}, \nID ({ctx.author.id})')
		await ctx.send(embed = embed, view = view)
		return

	if role1 in ctx.author.roles:

		select = Select(
			placeholder="Выберите категорию",
			options= [
				discord.SelectOption(
					label= "Общедоступные команды", 
					emoji= '📘',
					description='Команды доступные всем пользователям сервера.', 
				),
				discord.SelectOption(
					label= "Команды администрации", 
					emoji= '🔩',
					description='Категория команд доступная администраторам.' 
				),
				discord.SelectOption(
					label= "Команды уровней", 
					emoji= '📗',
					description='Хотите посмотреть свой уровень? Жмите сюда.'
				),
				discord.SelectOption(
					label= "Команды отзывов и статистики", 
					emoji= '📊',
					description='Желаете оставить отзыв об ивенте? Этот раздел для вас.'
				),
				discord.SelectOption(
					label= "Сторонние команды", 
					emoji= '📕',
					description='Необходимая команда не подходит не под один из критериев? Вам сюда.'
				)
			],
		)
		async def my_callbak(interaction):
			if {select.values[0]} == {'Общедоступные команды'}:
				embed = discord.Embed(title = f"Список общедоступных команд", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Общедоступные команды", value=f"`{prefix}осебе` `{prefix}команды` `{prefix}пинг` `{prefix}аватар` `{prefix}юзер` `{prefix}сервер` `{prefix}эмодзи` `{prefix}хелп`")
				embed.set_footer(text=f'"Общедоступные команды" - это команды доступные всем пользователям сервера, за исключением пользователей в мьюте.\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Команды администрации'}:
				embed = discord.Embed(title = f"Список команд Администрации", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды администрации", value=f"`{prefix}бан` `{prefix}разбан` `{prefix}кик` `{prefix}мьют` `{prefix}размьют` `{prefix}пред` `{prefix}снятьпред` `{prefix}сброспред` `{prefix}преды` `{prefix}очистить` `{prefix}создвремроль` `{prefix}времроль` ")
				embed.set_footer(text=f'"Команды администрации" - это команды доступные администрации сервера и выше уполномоченным людям\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Команды уровней'}:
				embed = discord.Embed(title = f"Список команд Уровней", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды системы уровней", value=f"`{prefix}стата` `{prefix}чарт` `{prefix}добранг` `{prefix}обнулить` ")
				embed.set_footer(text=f'"Команды уровней" - это команды для взаимодействия с ситемой уровней\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Команды отзывов и статистики'}:
				embed = discord.Embed(title = f"Список команд отзывов и статистики", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды отзывов и статистики", value=f" `{prefix}статчат` `{prefix}обновстатчат` `{prefix}ивент` `{prefix}администрация` `{prefix}сбростабливт` `{prefix}сбростабладм` `{prefix}удалитьотзывивт` `{prefix}удалитьотзывадм` `{prefix}снятьотзывивт` `{prefix}снятьотзывадм`")
				embed.set_footer(text=f'"Команды отзывов и статистики" - это команды для взаиводествия с системой отзывов и статистики(категория чатов отображающая кол. пользователей, ботов и тд)\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Сторонние команды'}:
				embed = discord.Embed(title = f"Список список сторонних команд", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Сторонние команды", value=f"`{prefix}рекроль` `{prefix}тикстарт` `{prefix}тикобнов` `{prefix}пргсстарт`")			
				embed.set_footer(text=f'"Сторонние команды" - это одиночные команды не подходящие ни к одной из категорий выше. На данный момент в эту категорию входят команды системы тикетов, ролей за реакцию, приватных войс каналов\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)

		select.callback = my_callbak
		view = View()
		view.add_item(select)

		embed = discord.Embed(title = f"Список команд уровня: Руководитель", color = 0x628ffe, timestamp=ctx.message.created_at)
		embed.add_field(
			name="Команды администрации", value=f"`{prefix}бан` `{prefix}разбан` `{prefix}кик` `{prefix}мьют` `{prefix}размьют` `{prefix}пред` `{prefix}снятьпред` `{prefix}сброспред` `{prefix}преды` `{prefix}очистить` `{prefix}создвремроль` `{prefix}времроль`"
			)
		embed.add_field(
			name="Общедоступные команды", value=f"`{prefix}осебе` `{prefix}команды` `{prefix}пинг` `{prefix}аватар` `{prefix}юзер` `{prefix}сервер` `{prefix}эмодзи` `{prefix}хелп`"
			)
		embed.add_field(
			name="Команды системы уровней", value=f"`{prefix}стата` `{prefix}чарт` `{prefix}добранг` `{prefix}обнулить` "
			)
		embed.add_field(
			name="Команды отзывов и статистики", value=f" `{prefix}статчат` `{prefix}обновстатчат` `{prefix}ивент` `{prefix}администрация` `{prefix}сбростабливт` `{prefix}сбростабладм` `{prefix}удалитьотзывивт` `{prefix}удалитьотзывадм` `{prefix}снятьотзывивт` `{prefix}снятьотзывадм`"
			)
		embed.add_field(
			name="Сторонние команды", value=f"`{prefix}рекроль` `{prefix}тикстарт` `{prefix}тикобнов` `{prefix}пргсстарт`"
			)
		embed.set_footer(text=f'Список уровня "Руководитель" является почти полным списком всех команд. В нём отсутствуют только системные команды. \nМой префикс "{prefix}". \nДля подробной информации о команде пропишите ({prefix}хелп название_команды) \nКоманду вызвал: {ctx.author}, \nID ({ctx.author.id})')
		await ctx.send(embed = embed, view = view)
		return

	if role2 in ctx.author.roles:

		select = Select(
			placeholder="Выберите категорию",
			options= [
				discord.SelectOption(
					label= "Общедоступные команды", 
					emoji= '📘',
					description='Команды доступные всем пользователям сервера.', 
				),
				discord.SelectOption(
					label= "Команды администрации", 
					emoji= '🔩',
					description='Категория команд доступная администраторам.' 
				),
				discord.SelectOption(
					label= "Команды уровней", 
					emoji= '📗',
					description='Хотите посмотреть свой уровень? Жмите сюда.'
				),
				discord.SelectOption(
					label= "Команды отзывов и статистики", 
					emoji= '📊',
					description='Желаете оставить отзыв об ивенте? Этот раздел для вас.'
				)
				
			],
		)
		async def my_callbak(interaction):
			if {select.values[0]} == {'Общедоступные команды'}:
				embed = discord.Embed(title = f"Список общедоступных команд", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Общедоступные команды", value=f"`{prefix}осебе` `{prefix}команды` `{prefix}пинг` `{prefix}аватар` `{prefix}юзер` `{prefix}сервер` `{prefix}эмодзи` `{prefix}хелп`")
				embed.set_footer(text=f'"Общедоступные команды" - это команды доступные всем пользователям сервера, за исключением пользователей в мьюте.\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			
			if {select.values[0]} == {'Команды администрации'}:
				embed = discord.Embed(title = f"Список команд Администрации", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды администрации", value=f"`{prefix}бан` `{prefix}разбан` `{prefix}кик` `{prefix}мьют` `{prefix}размьют` `{prefix}пред` `{prefix}снятьпред` `{prefix}преды` `{prefix}очистить` `{prefix}создвремроль` `{prefix}времроль`")
				embed.set_footer(text=f'"Команды администрации" - это команды доступные администрации сервера и выше уполномоченным людям\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			
			if {select.values[0]} == {'Команды уровней'}:
				embed = discord.Embed(title = f"Список команд Уровней", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды системы уровней", value=f"`{prefix}стата` `{prefix}чарт`")
				embed.set_footer(text=f'"Команды уровней" - это команды для взаимодействия с ситемой уровней\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			
			if {select.values[0]} == {'Команды отзывов и статистики'}:
				embed = discord.Embed(title = f"Список команд отзывов и статистики", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды отзывов и статистики", value=f" `{prefix}ивент` `{prefix}администрация`  `{prefix}удалитьотзывивт` `{prefix}удалитьотзывадм` `{prefix}снятьотзывивт` `{prefix}снятьотзывадм`")
				embed.set_footer(text=f'"Команды отзывов и статистики" - это команды для взаиводествия с системой отзывов и статистики(категория чатов отображающая кол. пользователей, ботов и тд)\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
		
		select.callback = my_callbak
		view = View()
		view.add_item(select)


		embed = discord.Embed(title = f"Список команд уровня: Администрация", color = 0x628ffe, timestamp=ctx.message.created_at)
		embed.add_field(
			name="Команды администрации", value=f"`{prefix}бан` `{prefix}разбан` `{prefix}кик` `{prefix}мьют` `{prefix}размьют` `{prefix}пред` `{prefix}снятьпред` `{prefix}преды` `{prefix}очистить` `{prefix}создвремроль` `{prefix}времроль`"
			)
		embed.add_field(
			name="Общедоступные команды", value=f"`{prefix}осебе` `{prefix}команды` `{prefix}пинг` `{prefix}аватар` `{prefix}юзер` `{prefix}сервер` `{prefix}эмодзи` `{prefix}хелп`"
			)
		embed.add_field(
			name="Команды системы уровней", value=f"`{prefix}стата` `{prefix}чарт`"
			)
		embed.add_field(
			name="Команды отзывов и статистики", value=f"  `{prefix}ивент` `{prefix}администрация` `{prefix}удалитьотзывивт` `{prefix}удалитьотзывадм` `{prefix}снятьотзывивт` `{prefix}снятьотзывадм`"
			)
		embed.set_footer(text=f'Список уровня "Руководитель" является почти полным списком всех команд. В нём отсутствуют только системные команды. \nМой префикс "{prefix}". \nДля подробной информации о команде пропишите ({prefix}хелп название_команды) \nКоманду вызвал: {ctx.author}, \nID ({ctx.author.id})')
		await ctx.send(embed = embed, view = view)
		return

	else:

		select = Select(
			placeholder="Выберите категорию",
			options= [
				discord.SelectOption(
					label= "Общедоступные команды", 
					emoji= '📘',
					description='Команды доступные всем пользователям сервера.', 
				),
				discord.SelectOption(
					label= "Команды уровней", 
					emoji= '📗',
					description='Хотите посмотреть свой уровень? Жмите сюда.'
				),
				discord.SelectOption(
					label= "Команды отзывов и статистики", 
					emoji= '📊',
					description='Желаете оставить отзыв об ивенте? Этот раздел для вас.'
				),
				
			],
		)
		async def my_callbak(interaction):
			if {select.values[0]} == {'Общедоступные команды'}:
				embed = discord.Embed(title = f"Список общедоступных команд", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Общедоступные команды", value=f"`{prefix}осебе` `{prefix}команды` `{prefix}пинг` `{prefix}аватар` `{prefix}юзер` `{prefix}сервер` `{prefix}эмодзи` `{prefix}хелп`")
				embed.set_footer(text=f'"Общедоступные команды" - это команды доступные всем пользователям сервера, за исключением пользователей в мьюте.\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Команды уровней'}:
				embed = discord.Embed(title = f"Список команд Уровней", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды системы уровней", value=f"`{prefix}стата` `{prefix}чарт`")
				embed.set_footer(text=f'"Команды уровней" - это команды для взаимодействия с ситемой уровней\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
			if {select.values[0]} == {'Команды отзывов и статистики'}:
				embed = discord.Embed(title = f"Список команд отзывов и статистики", color = 0x628ffe, timestamp=ctx.message.created_at)
				embed.add_field(name="Команды отзывов и статистики", value=f"  `{prefix}ивент` `{prefix}администрация` `{prefix}удалитьотзывивт` `{prefix}удалитьотзывадм`")
				embed.set_footer(text=f'"Команды отзывов и статистики" - это команды для взаиводествия с системой отзывов и статистики(категория чатов отображающая кол. пользователей, ботов и тд)\n')
				await interaction.response.send_message(embed = embed, ephemeral = True)
		select.callback = my_callbak
		view = View()
		view.add_item(select)

		embed = discord.Embed(title = f"Список команд уровня: Пользователь", color = 0x628ffe, timestamp=ctx.message.created_at)
		embed.add_field(
			name="Общедоступные команды", value=f"`{prefix}осебе` `{prefix}команды` `{prefix}пинг` `{prefix}аватар` `{prefix}юзер` `{prefix}сервер` `{prefix}эмодзи` `{prefix}хелп`"
			)
		embed.add_field(
			name="Команды системы уровней", value=f"`{prefix}стата` `{prefix}чарт`"
			)
		embed.add_field(
			name="Команды отзывов и статистики", value=f" `{prefix}ивент` `{prefix}администрация` `{prefix}удалитьотзывивт` `{prefix}удалитьотзывадм`"
			)
		embed.set_footer(text=f'Список уровня "Пользователь" является самым урезаным из всех существующих вариантов. Сделано это для того, чтобы пользователь не искал нужную команду среди большого количества недоступных ему команд. \nМой префикс "{prefix}". \nДля подробной информации о команде пропишите ({prefix}хелп название_команды) \nКоманду вызвал: {ctx.author}, \nID ({ctx.author.id})')
		await ctx.send(embed = embed, view = view)







@bot.command(aliases=["Хелп", "help", "Help"])
async def хелп(ctx, command = None):
	if language == 1:
		embed = discord.Embed( title = "Навигация по команде", color = 0x628ffe, timestamp=ctx.message.created_at)
		if command == 'бан':
			embed.add_field(name = f'{prefix}бан', 
				value = f'Банит определённого пользователя на сервере.\n \n **Для использования данной команды следуйте схеме:**\n {prefix}бан [пользователь] [время(в минутах)] [причина]) \n **Пример:** $бан @smetanka_v_dele 10 оск.администрации \n **Пример:** {prefix}бан @smetanka_v_dele 0 \n **Примечание 1:** Причину либо причину и время указывать необязательно. \n **Примечание 2:** Если указать время  `0`, то время не будет указано.')
		if command == 'разбан':
			embed.add_field(name = f'{prefix}разбан', 
				value = f'Снимает бан с определённого пользователя на сервере. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}разбан [пользователь] \n **Пример:** {prefix}разбан @Neon')
		if command == 'кик':
			embed.add_field(name = f'{prefix}кик', 
				value = f'Выгоняет определённого пользователя с сервера.\n \n **Для использования данной команды следуйте схеме**:\n {prefix}кик [пользователь] [причина] \n **Пример:** {prefix}кик @BreadCat Нарушение правила D6 \n **Примечание 1:** Причину указывать необязательно.')
		if command == 'мьют':
			embed.add_field(name = f'{prefix}мьют', 
				value = f'Мьютит определённого пользователя на сервере.\n \n Для использования данной команды следуйте схеме:\n {prefix}мьют [пользователь] [время(в минутах)] [причина] \n **Пример:** {prefix}мьют @ПЕЧЕНЕГР 10 По приколу \n **Примечание 1:** Причину либо причину и время указывать необязательно. \n **Примечание 2:** Если указать время  `0`, то время не будет указано.')
		if command == 'размьют':
			embed.add_field(name = f'{prefix}размьют', 
				value = f'Снимает мьют с определённого пользователя на сервере.\n \n **Для использования данной команды следуйте схеме:**\n {prefix}размьют [пользователь]\n **Пример:** {prefix}размьют @smetanka_v_dele ')
		if command == 'пред':
			embed.add_field(name = f'{prefix}пред', 
				value = f'Выдаёт предупреждение определённому пользователю на сервере.\n \n **Для использования данной команды следуйте схеме:**\n {prefix}пред [пользователь] [причина]\n **Пример:** {prefix}пред @Neon гей')
		if command == 'снятьпред':
			embed.add_field(name = f'{prefix}снятьпред', 
				value = f'Снимает определённому пользователю предупреждение на сервере.\n \n **Для использования данной команды следуйте схеме:**\n {prefix}снятьпред [случай]\n **Пример:** {prefix}снятьпред 42 \n **Примечание 1:** случай предупреждения можно посмотреть воспользовавшись командой **$преды**  ')
		if command == 'сброспред':
			embed.add_field(name = f'{prefix}сброспред', 
				value = f'Сбрасывает всю таблицу предупреждений(варнов) на сервере.')
		if command == 'преды':
			embed.add_field(name = f'{prefix}преды', 
				value = f'Выводит преды указанного пользователя на сервере.\n \n **Для использования данной команды следуйте схеме:**\n {prefix}преды [пользователь]\n **Пример:** {prefix}преды @BreadCat \n **Примечание 1:** Автор сообщения - пользователь по умолчанию')
		if command == 'очистить':
			embed.add_field(name = f'{prefix}очистить', 
				value = f'Очищает чат, в котором была вызвана команда.\n \n **Для использования данной команды следуйте схеме:**\n {prefix}очистить [количество сообщений] \n **Пример:** {prefix}очистить 57')
		if command == 'создвремроль':
			embed.add_field(name = f'{prefix}создвремроль', 
				value = f'Создаёт и выдаёт определённому пользователю временную роль на сервере.\n \n **Для использования данной команды следуйте схеме:**\n {prefix}создвремроль [время(в минутах)] [Удалить ли после срабатывания (True/False)] [пользователь] [название роли]\n **Пример:** {prefix}создвремроль 200 True @ПЕЧЕНЕГР побеитель ивента\n **Пример:** {prefix}создвремроль 235 False @ПЕЧЕНЕГР лузер')
		if command == 'времроль':
			embed.add_field(name = f'{prefix}времроль', 
				value = f'Временно выдатёт определённому пользователю существующую роль на сервере.\n \n **Для использования данной команды следуйте схеме:**\n {prefix}времроль [время(в минутах)] [пользователь] [название/упоминание существующей роли]  \n **Пример:** {prefix}времроль 10 @smetanka_v_dele @крендель')
		if command == 'таблварн':
			embed.add_field(name = f'{prefix}таблварн', 
				value = f'**Системная команда**\n \n Таблица варнов.')
		if command == 'осебе':
			embed.add_field(name = f'{prefix}осебе', 
				value = f'Вывести основную информацию о боте.')
		if command == 'команды':
			embed.add_field(name = f'{prefix}команды', 
				value = f'Вывести этот список.')
		if command == 'пинг':
			embed.add_field(name = f'{prefix}пинг', 
				value = f'Показывает пинг бота.')
		if command == 'аватар':
			embed.add_field(name = f'{prefix}аватар', 
				value = f'Отправляет аватар указанного пользователя в чат, в котором была вызвана команда. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}аватар [пользователь] \n **Пример:** {prefix}аватар @Neon \n **Примечание 1:** Автор сообщения - пользователь по умолчанию')
		if command == 'юзер':
			embed.add_field(name = f'{prefix}юзер', 
				value = f'Выводит основную информацию об определённом пользователе. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}юзер [пользователь] \n **Пример:** {prefix}юзер @Neon \n **Примечание 1:** Автор сообщения - пользователь по умолчанию')
		if command == 'сервер':
			embed.add_field(name = f'{prefix}сервер', 
				value = f'Выводит информацию о сервере, в котором была вызвана команда.')
		if command == 'эмодзи':
			embed.add_field(name = f'{prefix}эмодзи', 
				value = f'Информация об определённом пользовательском эмодзи на сервере. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}эмодзи [эмодзи] \n **Пример:** {prefix}эмодзи 🇧🇾 \n **Примечание 1:** Выводить информацию можно только о `ПОЛЬЗОВАТЕЛЬСКИХ` эмодзи. В примере эмодзи дискорда указан для корректного отображения')
		if command == 'стата':
			embed.add_field(name = f'{prefix}стата', 
				value = f'Выводит уровень определённого пользователя на сервере и всё связанное с ним. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}стата [пользователь]\n **Пример:** {prefix}стата @BreadCat** \n Примечание 1:** Автор сообщения - пользователь по умолчанию')
		if command == 'чарт':
			embed.add_field(name = f'{prefix}чарт', 
				value = f'Топ пользователей по уровню на сервере.')
		if command == 'добранг':
			embed.add_field(name = f'{prefix}добранг', 
				value = f'Добавить пользователю уровень на сервере (нуждается в доработке). \n \n **Для использования данной команды следуйте схеме:**\n {prefix}добранг [пользователь] \n **Пример:** {prefix}добранг @ПЕЧЕНЕГР')
		if command == 'обнулить':
			embed.add_field(name = f'{prefix}обнулить', 
				value = f'Обнулить ранг пользователя на сервере. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}обнулить [пользователь]\n **Пример:** {prefix}обнульть @smetanka_v_dele')
		if command == 'обстав':
			embed.add_field(name = f'{prefix}обстав', 
				value = f'**Системная команда**\n \n Запустить цикл автоматического обновленя отзывов.')
		if command == 'статчат':
			embed.add_field(name = f'{prefix}статчат', 
				value = f'**Системная команда**\n \n Создать чаты для динамической статистики на сервере.')
		if command == 'обновстатчат':
			embed.add_field(name = f'{prefix}обновстатчат', 
				value = f'**Системная команда**\n \n Ручное обновление чатов динамической статистики.')
		if command == 'ивент':
			embed.add_field(name = f'{prefix}ивент', 
				value = f'Оставить отзыв об ивентах на сервере. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}ивент [имя ивента] [оценка ивента(от 1 до 10)] [коментарий] \n **Пример:** {prefix}ивент бомбардировка 7 сложно')
		if command == 'администрация':
			embed.add_field(name = f'{prefix}администрация', 
				value = f'Оставить отзыв об администрации на сервере. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}администрация [имя администратора] [оценка работы администратора(от 1 до 10)] [коментарий]\n **Пример:** {prefix}администрация @BreadCat 4 толстый лентяй')
		if command == 'сбростабливт':
			embed.add_field(name = f'{prefix}сбростабливт', 
				value = f'Сбросить таблицу "iventi".')
		if command == 'сбростабладм':
			embed.add_field(name = f'{prefix}сбростабладм', 
				value = f'Сбросить таблицу "rabotaadminov".')
		if command == 'удалитьотзывивт':
			embed.add_field(name = f'{prefix}удалитьотзывивт', 
				value = f'Удалить свой отзыв об ивентах.')
		if command == 'удалитьотзывадм':
			embed.add_field(name = f'{prefix}удалитьотзывадм', 
				value = f'Удалить свой отзыв об администрации.')
		if command == 'снятьотзывивт':
			embed.add_field(name = f'{prefix}снятьотзывивт', 
				value = f'Удалить чужой отзыв об ивентах.  \n \n **Для использования данной команды следуйте схеме:**\n {prefix}снятьотзывивт [пользователь] \n **Пример:** {prefix}снятьотзывадм @ПЕЧЕНЕГР')
		if command == 'снятьотзывадм':
			embed.add_field(name = f'{prefix}снятьотзывадм', 
				value = f'Удалить чужой отзыв об администрации. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}снятьотзывадм [пользователь] \n **Пример:** {prefix}снятьотзывадм @ПЕЧЕНЕГР')
		if command == 'табладм':
			embed.add_field(name = f'{prefix}табладм', 
				value = f'**Системная команда**\n \n Таблица отзывов об админисстрации.')
		if command == 'табливт':
			embed.add_field(name = f'{prefix}табливт', 
				value = f'**Системная команда**\n \n Таблица отзывов об ивентах.')
		if command == 'рекроль':
			embed.add_field(name = f'{prefix}рекроль', 
				value = f'Создаёт сообщение, при нажатии на определённую реакцию под которым выдаёт определённому пользователю указанную роль на сервере. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}рекроль [эмодзи] [роль] [само сообщение] \n **Пример:** {prefix}рекроль 🇧🇾 @крендель если хотите получить роль, то нажмите на реакцию  \n **Примечание 1:** Можно использовать любой эмодзи \n **Примечание 2:** Можно использовать только существующие роли')
		if command == 'ПЕЧЕНЕГР':
			embed.add_field(name = f'{prefix}ПЕЧЕНЕГР', 
				value = f'Секретная комманда.')
		if command == 'Neon':
			embed.add_field(name = f'{prefix}Neon', 
				value = f'Секретная команда.')
		if command == 'BreadCat':
			embed.add_field(name = f'{prefix}BreadCat', 
				value = f'Секретная команда.')
		if command == 'OmerX':
			embed.add_field(name = f'{prefix}OmerX', 
				value = f'Секретная команда.')
		if command == None:
			embed.add_field(name = f'{prefix}хелп', 
				value = f'Команда для просмотра информации о команде. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}хелп [название_команды]')
		elif command == 'хелп':
			embed.add_field(name = f'{prefix}хелп', 
				value = f'Команда для просмотра информации о команде. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}хелп [название_команды]')
		elif command == 'help':
			embed.add_field(name = f'{prefix}хелп', 
				value = f'Команда для просмотра информации о команде. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}хелп [название_команды]')
		elif command == 'хелп':
			embed.add_field(name = f'{prefix}хелп', 
				value = f'Команда для просмотра информации о команде. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}хелп [название_команды]')
		elif command == 'Help':
			embed.add_field(name = f'{prefix}хелп', 
				value = f'Команда для просмотра информации о команде. \n \n **Для использования данной команды следуйте схеме:**\n {prefix}хелп [название_команды]')
		if command == 'тикстарт':
			embed.add_field(name = f'{prefix}тикстарт', 
				value = f'Команда для создания тикетчатов')
		if command == 'тикобнов':
			embed.add_field(name = f'{prefix}тикобнов', 
				value = f'**Внимание!!! Данная команда является прототипом и работает некорректно** \n\n Команда для регенерации чатов тикетов после перезагрузки бота')
		if command == 'пргсстарт':
			embed.add_field(name = f'{prefix}пргсстарт', 
				value = f'Команда для запуска системы приватных войс каналов')
		await ctx.send(embed = embed)
	#if language == 2:

	#if language == 3:
		
	#if language == 4:
#================================================================================================================================================================================

#пинг
@bot.command(aliases=["Ping","PING","pING","ping","Пинг","ПИНГ","пИНГ","пинг","Понг","ПОНГ","пОНГ","понг",])
async def __ping(ctx,): 
    ping = bot.ws.latency

    ping_emoji = "🟩🔳🔳🔳🔳"

    if ping > 0.10000000000000000:
        ping_emoji = "🟧🟩🔳🔳🔳"

    if ping > 0.15000000000000000:
        ping_emoji = "🟥🟧🟩🔳🔳"

    if ping > 0.20000000000000000:
        ping_emoji = "🟥🟥🟧🟩🔳"

    if ping > 0.25000000000000000:
        ping_emoji = "🟥🟥🟥🟧🟩"

    if ping > 0.30000000000000000:
        ping_emoji = "🟥🟥🟥🟥🟧"

    if ping > 0.35000000000000000:
        ping_emoji = "🟥🟥🟥🟥🟥"

    await ctx.send(content=f"Понг! {ping_emoji} `{ping * 1000:.0f}ms` :ping_pong:")

#не работает
#@bot.command()
async def стикер(ctx, *, stiker1 = None):
	stiker1 == stiker
	stiker = await stiker.guild.fetch_stiker(stiker.id)
	if stiker is None:
		pass
	else:
		time = ctx.message.created_at
		embed = discord.Embed(title =f"Информация о стикере {stiker.name}", colour=0xADD8E6, timestamp=ctx.message.created_at, inline=True)
		embed.add_field(name = f"Название: {stiker.name}", inline=True)
		embed.add_field(name = f"Описание: {stiker.description}", inline=True)
		embed.add_field(name = f"ID:{stiker.id}", inline=True)
		embed.add_field(name = f"Формат:{stiker.format}", inline=True)
		embed.add_field(name = f"Создан на сервере: {stiker.guild_id}", inline=True)
		embed.add_field(name = f"Автор: TEST")                                           #{stiker.user}
		embed.add_field(name = f"Эмодзи представляющий наклейку: {stiker.emoji}", inline=True)
		embed.set_footer(text=f"\n  Команду вызвал: {ctx.author},\n ID: ({ctx.author.id})")
		await ctx.send(embed=embed)

#команда user
@bot.command()
async def юзер(ctx, member: discord.Member = None):
	if member is None:
		member = ctx.author
	roles = [role for role in member.roles]
	embed =	discord.Embed(title = f"Инфориация о пользователе {member.name}",color = 0x0000ee, timestamp=ctx.message.created_at)
	embed.set_thumbnail(url=member.display_avatar)
	embed.add_field(name="ID", value=member.id, inline=True)
	embed.add_field(name="Никнейм", value=member.display_name, inline=True)
	embed.add_field(name="Аккаунт создан", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
	embed.add_field(name="Присоеденился", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
	embed.add_field(name="Бот?", value=member.bot, inline=True)
	embed.add_field(name="Лучшая роль", value=member.top_role.mention, inline=True)
	embed.add_field(name="Роли", value="".join(role.mention for role in roles), inline=True)
	await ctx.send(embed=embed)

#команда avatar
@bot.command()
async def аватар(ctx, member: discord.Member = None):
	if member == None:
		member = ctx.author

	memberAvatar = member.display_avatar

	avaEmbed = discord.Embed(title = f"Аватар {member.name}", color = 0xd8b9e8, timestamp=ctx.message.created_at)
	avaEmbed.set_image(url = memberAvatar)

	await ctx.send(embed = avaEmbed)

#команда server
@bot.command()
async def сервер(ctx):
    boosters = ctx.guild.premium_subscribers
    owner = ctx.guild.owner.mention
    all = len(ctx.guild.members)
    members = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
    bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
    channels = [len(list(filter(lambda m: str(m.type) == "text", ctx.guild.channels))),
                len(list(filter(lambda m: str(m.type) == "voice", ctx.guild.channels)))]
    embed = discord.Embed(title=f"Информация о сервере:{ctx.guild} ", color = 0x98F5FF, timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.add_field(name="Статус", value=f"🟢 Online: **{statuses[0]}** \n 🌙 Idle: **{statuses[1]}** \n ⛔ DND: **{statuses[2]}** \n ⚪ Offline: **{statuses[3]}**    ")
    embed.add_field(name="Пользователи", value=f"👥 All: **{all}** \n 👤 Humans: **{members}** \n 🤖 Bots: **{bots}**"    )
    embed.add_field(name="Каналы", value=f"📢 All: **{channels[0] + channels[1]}** \n 💬 Text: **{channels[0]}** \n 🎧 Voice: **{channels[1]}**   ")
    embed.add_field(name="Уровень верефикации", value=f'[**{ctx.guild.verification_level}**]')
    embed.add_field(name="Бустеры", value=f'**💸 {boosters}**')
    embed.add_field(name="Владелец", value=f"👑 {owner}")
    embed.set_footer(
    	text=f"команду вызвал: {ctx.author}, id ({ctx.author.id}) \n актуальная информация на"
    	)
    await ctx.send(embed=embed)
#=============================================================уровни==========================================================================================
intents = discord.Intents.default()
intents.members = True
bot.multiplier = 25

async def initialize():
    await bot.wait_until_ready()
    bot.db = await aiosqlite.connect("expData.db")
    await bot.db.execute("CREATE TABLE IF NOT EXISTS guildData (guild_id int, user_id int, exp int, PRIMARY KEY (guild_id, user_id))")
    
@bot.event
async def on_message(message):
    if not message.author.bot:
        cursor = await bot.db.execute("INSERT OR IGNORE INTO guildData (guild_id, user_id, exp) VALUES (?,?,?)", (message.guild.id, message.author.id, 1)) 

        if cursor.rowcount == 0:
            await bot.db.execute("UPDATE guildData SET exp = exp + 1 WHERE guild_id = ? AND user_id = ?", (message.guild.id, message.author.id))
            cur = await bot.db.execute("SELECT exp FROM guildData WHERE guild_id = ? AND user_id = ?", (message.guild.id, message.author.id))
            data = await cur.fetchone()
            exp = data[0]
            lvl = math.sqrt(exp) / bot.multiplier
        	
            if lvl.is_integer():
                await message.channel.send(f"Отлично, у {message.author.mention} уже : {int(lvl)} уровень.")

        await bot.db.commit()

    await bot.process_commands(message)

@bot.command()
async def стата(ctx, member: discord.Member=None):
    if member is None: member = ctx.author

    async with bot.db.execute("SELECT exp FROM guildData WHERE guild_id = ? AND user_id = ?", (ctx.guild.id, member.id)) as cursor:
        data = await cursor.fetchone()
        exp = data[0]

    async with bot.db.execute("SELECT exp FROM guildData WHERE guild_id = ?", (ctx.guild.id,)) as cursor:
        rank = 1
        async for value in cursor:
            if exp < value[0]:
                rank += 1

    lvl = int(math.sqrt(exp)//bot.multiplier)

    current_lvl_exp = (bot.multiplier*(lvl))**2
    next_lvl_exp = (bot.multiplier*((lvl+1)))**2

    lvl_percentage = ((exp-current_lvl_exp) / (next_lvl_exp-current_lvl_exp)) * 100

    embed = discord.Embed(title=f"Статистика пользователя {member.name}", colour=discord.Colour.gold())
    embed.add_field(name="📈 Уровень", value=f"{str(lvl)}.lvl")
    embed.add_field(name="🪙 Опыт", value=f"{exp}/{next_lvl_exp}")
    embed.add_field(name="🥇 Ранг", value=f"{rank}/{ctx.guild.member_count}")
    embed.add_field(name="⚙️ Прогесс", value=f"{round(lvl_percentage, 2)}%")

    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions( administrator = True )

async def добранг(message, member: discord.Member=None, amount=1):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	if member is None: member = message.author
	channel = bot.get_channel( logschannel ) 
	await bot.db.execute("UPDATE guildData SET exp = exp + 99999999999999 WHERE guild_id = ? AND user_id = ?", (message.guild.id, member.id)) 
	await message.send(f"Уровень **{member}** успешно увеличен")
	await channel.send( embed = discord.Embed( title = f'[{dt_string}] Пользователь: **{ message.author}**, увеличил  уровень **{member}**', description = f'\n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0x3c535f))

@bot.command()
@commands.has_permissions( administrator = True )
async def обнулить(message, member: discord.Member=None):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	if member is None: member = message.author
	channel = bot.get_channel( logschannel )
	await bot.db.execute("UPDATE guildData SET exp = exp * 0 WHERE guild_id = ? AND user_id = ?", (message.guild.id, member.id))
	await message.send(f"Уровень **{member}** успешно обнулён")
	await channel.send( embed = discord.Embed( title = f'[{dt_string}] Пользователь: **{message.author}**, обнулил  уровень **{member}**', description = f'\n \n Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xfffff4))

@bot.command()
async def чарт(ctx): 
    buttons = {}
    for i in range(1, 6):
        buttons[f"{i}\N{COMBINING ENCLOSING KEYCAP}"] = i 

    previous_page = 0
    current = 1
    index = 1
    entries_per_page = 10

    embed = discord.Embed(title=f"Таблица лидеров {current}", description="", colour=discord.Colour.gold())
    msg = await ctx.send(embed=embed)

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        if current != previous_page:
            embed.title = f"Таблица лидеров {current}"
            embed.description = ""

            async with bot.db.execute(f"SELECT user_id, exp FROM guildData WHERE guild_id = ? ORDER BY exp DESC LIMIT ? OFFSET ? ", (ctx.guild.id, entries_per_page, entries_per_page*(current-1),)) as cursor:
                index = entries_per_page*(current-1)

                async for entry in cursor:
                    index += 1
                    member_id, exp = entry
                    member = ctx.guild.get_member(member_id)
                    embed.description += f"{index}) {member.mention} : {exp}\n"

                await msg.edit(embed=embed)

        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            return await msg.clear_reactions()

        else:
            previous_page = current
            await msg.remove_reaction(reaction.emoji, ctx.author)
            current = buttons[reaction.emoji]
#===========================================================Динамическая статистика=================================================================================================


@bot.command()
@commands.has_permissions( administrator = True )
async def статчат(ctx):
	bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
	members = ctx.guild.member_count - bots
	all = len(ctx.guild.members)
	category1 = await ctx.guild.create_category(name = "◦─◦─◦┃Сводка┃◦─◦─◦",position = 0)
	channel1 = await ctx.guild.create_voice_channel(name = f'👥Игроков: {members}', category = category1)
	await channel1.set_permissions(ctx.guild.default_role, connect = False, manage_channels = False)
	channel2 = await ctx.guild.create_voice_channel(name = f'🤖Боты: {bots}', category = category1)
	await channel2.set_permissions(ctx.guild.default_role, connect = False, manage_channels = False)
	channel3 = await ctx.guild.create_voice_channel(name = f'📢Всего: {all}', category = category1)
	await channel3.set_permissions(ctx.guild.default_role, connect = False, manage_channels = False)
	channel4 = await ctx.guild.create_voice_channel(name = f'🔩Р/А: 0/10', category = category1)
	await channel4.set_permissions(ctx.guild.default_role, connect = False, manage_channels = False)
	channel5 = await ctx.guild.create_voice_channel(name = f'🥏К/И: 0/10', category = category1)
	await channel5.set_permissions(ctx.guild.default_role, connect = False, manage_channels = False)
	with open('DStats.json') as json_file:
		data = json.load(json_file)
		channels = {
		'allchannel': channel3.id,
		'botschannel': channel2.id,
		'playerchannel': channel1.id,
		'ki': channel5.id,
		'ra': channel4.id
		}

		data.append(channels)

	with open('DStats.json', 'w') as f:
		json.dump(data, f, indent=4)
	
#обновление динамической статистики ч1
@bot.command()
@commands.has_permissions( administrator = True )
async def обстав(ctx):
	print(f'цикл был запущен {ctx.author.name}')
	while True:
		await s(60*5)
		bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
		all = len(ctx.guild.members)
		members = ctx.guild.member_count - bots

		with open('DStats.json') as react_file:
			data = json.load(react_file)
			for x in data:
				playerchannel = x['playerchannel'] 
				botschannel = x['botschannel'] 
				allchannel = x['allchannel']
				#KIchennel = x['ki']
				#RAchannel =  x['ra']

		channel1 = bot.get_channel(playerchannel)
		channel2 = bot.get_channel(botschannel)
		channel3 = bot.get_channel(allchannel)
		new_name1 = f'👥Игроков: {members}'
		new_name2 = f'🤖Боты: {bots}'
		new_name3 = f'📢Всего: {all}'
		if channel1 != None:
			await channel1.edit(name = new_name1)
			print('"Игроков" обновлено')
		else:
			print(f"канал {channel1} не найден")
		if channel2 != None:
			await channel2.edit(name = new_name2)
			print('"Боты" обновлено')
		else:
			print(f"канал {channel2} не найден")
		if channel3 != None:
			await channel3.edit(name = new_name3)
			print('"Всего" обновлено')
		else:
			print(f"канал {channel3} не найден")

		#for sa1 in sql.execute("SELECT AVG(gradeivent) FROM stats WHERE admuserid == 0"):
			#sa11 = str(sa1)
			#db.commit()
			#channel4 = bot.get_channel(KIchennel)
			#new_name4 = f'🥏К/И: {sa11[1:-2]}/10'
		#for sa2 in sql.execute("SELECT AVG(gradework) FROM stats WHERE admuserid == 0"):
			#sa22 = str(sa2)
			#db.commit()
			#channel5 = bot.get_channel(RAchannel)
			#new_name5 = f'🔩Р/А: {sa22[1:-2]}/10'
			#if channel4 != None:
				#await channel4.edit(name = new_name4)
				#print('"К/И" обновлено1')
			#if channel5 != None:
				#await channel5.edit(name = new_name5)
				#print('"Р/А" обновлено1')

#логи изменения ролей
@bot.event
async def on_member_update(before, after):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	if before.roles != after.roles:
		channel = bot.get_channel(logschannel)
		emb = discord.Embed(description = f'[{dt_string}] **Обновление ролей пользователя -  {before.mention}**', colour = discord.Color.red())
		emb.add_field(name = '**Роли до**', value = ", ".join([r.mention for r in before.roles])) 
		emb.add_field(name = '**Роли после**', value = ", ".join([r.mention for r in after.roles])) 
		async for event in before.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update):

			if getattr(event.target, "id", None) != before.id:

				continue
			emb.add_field(name="Изменённые роли", value = ", ".join([getattr(r, "mention", r.id) for r in event.before.roles or event.after.roles]))
			emb.add_field(name="Модератор", value = event.user)
			break
		if event.user.id != idbota:
			await channel.send(embed = emb)

@bot.command()
@commands.has_permissions( administrator = True )
async def обновстатчат(ctx):
	with open('DStats.json') as react_file:
		data = json.load(react_file)
		for x in data:
			playerchannel = x['playerchannel'] 
			botschannel = x['botschannel'] 
			allchannel = x['allchannel']
			KIchennel = x['ki']
			RAchannel = x['ra']
			channel1 = bot.get_channel(playerchannel)
			channel2 = bot.get_channel(botschannel)
			channel3 = bot.get_channel(allchannel)
	bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
	all = len(ctx.guild.members)
	members = ctx.guild.member_count - bots

	channel1 = bot.get_channel(playerchannel)
	channel2 = bot.get_channel(botschannel)
	channel3 = bot.get_channel(allchannel)
	new_name1 = f'👥Игроков: {members}'
	new_name2 = f'🤖Боты: {bots}'
	new_name3 = f'📢Всего: {all}'
	if channel1 != None:
		await channel1.edit(name = new_name1)
		print('"Игроков" обновлено')
	if channel2 != None:
		await channel2.edit(name = new_name2)
		print('"Боты" обновлено')
	if channel3 != None:
		await channel3.edit(name = new_name3)
		print('"Всего" обновлено')
	for sa1 in sql.execute("SELECT AVG(gradeivent) FROM stats WHERE admuserid == 0"):
		sa11 = str(sa1)
		db.commit()
		channel4 = bot.get_channel(KIchennel)
		new_name4 = f'🥏К/И: {sa11[1:-2]}/10'
	for sa2 in sql.execute("SELECT AVG(gradework) FROM stats WHERE ivtuserid == 0"):
		sa22 = str(sa2)
		db.commit()
		channel5 = bot.get_channel(RAchannel)
		new_name5 = f'🔩Р/А: {sa22[1:-2]}/10'
		if channel4 != None:
			await channel4.edit(name = new_name4)
			print('"К/И" обновлено')
		if channel5 != None:
			await channel5.edit(name = new_name5)
			print('"Р/А" обновлено')
		await ctx.send(f'Статистика обновлена')

#=======================================================Динамическая статистика Ч2=========================================================
#ввод данных
@bot.command() 
async def ивент(ctx, iventname, gradeivent, * ,ivtcomment = None):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	if int(gradeivent) > -1:
		if int(gradeivent) < 11:
			channel = bot.get_channel( logschannel )
			ivtusername = ctx.author.name
			ivtuserid = ctx.author.id
			admuserid = 0 
			admusername = '-'
			administratorname = '-'
			gradework = 0
			admcomment = '-'

			sql.execute("SELECT ivtuserid FROM stats WHERE ivtuserid = ?", [ivtuserid])
			if sql.fetchone() is None:
				sql.execute(f"INSERT INTO stats VALUES (?,?,?,?,?,?,?,?,?,?)", (
					ivtuserid, ivtusername, iventname, gradeivent, ivtcomment, admuserid, admusername, administratorname, gradework, admcomment
					)
				)
				db.commit()

				await ctx.send('Спасибо за отзыв. \n Напоминаем, что для отправки отзыва необходимо следовать примеру: \n ```diff\n->  $ивент⠀[название ивента]⠀[оценка⠀0-10] [комментарий]⠀ ```')
				print(f'[{dt_string}] {ctx.author} оставил отзыв об ивентах')
				await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} оставил отзыв об ивентах", color = 0x3139ea, timestamp=ctx.message.created_at ) )
			else:
				sql.execute(f"DELETE FROM stats WHERE ivtuserid == {ctx.author.id} ")
				db.commit()

			sql.execute("SELECT ivtuserid FROM stats WHERE ivtuserid = ?", [ivtuserid])
			if sql.fetchone() is None:
				sql.execute(f"INSERT INTO stats VALUES (?,?,?,?,?,?,?,?,?,?)", (
					ivtuserid, ivtusername, iventname, gradeivent, ivtcomment, admuserid, admusername, administratorname, gradework, admcomment
					)
				)
				db.commit()
				await ctx.send('Ваш отзыв об ивентах отредактирован ')
				print(f'[{dt_string}] {ctx.author} отредактировал отзыв об ивентах')
				await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} отредактировал отзыв об ивентах", color = 0x3139ea, timestamp=ctx.message.created_at ) )
		else:
			await ctx.send('Вы указали значение"Баллы" больше максимального')
	else:
		await ctx.send('Вы указали значение"Баллы" меньше минимального')


@bot.command()
async def администрация(ctx, administratorname, gradework, * ,admcomment):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	if int(gradework) > -1:
		if int(gradework) < 11:	
			channel = bot.get_channel( logschannel )
			admusername = ctx.author.name
			admuserid = ctx.author.id
			ivtuserid = 0
			ivtusername = '-'
			iventname = '-'
			gradeivent = 0
			ivtcomment = '-'

			sql.execute("SELECT admuserid FROM stats WHERE admuserid = ?", [admuserid])
			if sql.fetchone() is None:
				sql.execute(f"INSERT INTO stats VALUES (?,?,?,?,?,?,?,?,?,?)", (
					ivtuserid, ivtusername, iventname, gradeivent, ivtcomment, admuserid, admusername, administratorname, gradework, admcomment
					)
				)
				db.commit()

				await ctx.send('Спасибо за отзыв. \n Напоминаем, что для отправки отзыва необходимо следовать примеру: \n ```diff\n->  $администрация⠀[имя⠀администратора]⠀[оценка⠀0-10] [комментарий]```')
				print(f'Пользователь: {ctx.author} оставил отзыв об администрации')
				await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} оставил отзыв  об администрации", color = 0x3139ea, timestamp=ctx.message.created_at ) )
			else:
				sql.execute(f"DELETE FROM stats WHERE admuserid == {ctx.author.id} ")
				db.commit()

			sql.execute("SELECT admuserid FROM stats WHERE admuserid = ?", [admuserid])
			if sql.fetchone() is None:
				sql.execute(f"INSERT INTO stats VALUES (?,?,?,?,?,?,?,?,?,?)", (
					ivtuserid, ivtusername, iventname, gradeivent, ivtcomment, admuserid, admusername, administratorname, gradework, admcomment
					)
				)
				db.commit()
				await ctx.send('Ваш отзыв об администрации отредактирован ')
				print(f'Пользователь: {ctx.author} отредактировал отзыв об администрации')
				await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} отредактировал отзыв об администрации", color = 0x3139ea, timestamp=ctx.message.created_at ) )
		else:
			await ctx.send('Вы указали значение "Баллы" больше максимального')
	else:
		await ctx.send('Вы указали значение "Баллы" меньше минимального')


#вывод таблицы "ивенты"
@bot.command()
@commands.has_permissions( kick_members = True )
async def табливт(ctx):
	await ctx.send('Список отзывов "ивенты"')
	for value in sql.execute("SELECT ivtuserid, ivtusername, iventname, gradeivent, ivtcomment  FROM stats WHERE ivtuserid != 0"):
		await ctx.send(value)
				
#вывод таблицы "администрация"
@bot.command()
@commands.has_permissions( kick_members = True )
async def табладм(ctx):
	await ctx.send('Список отзывов "администрация"')
	for value in sql.execute("SELECT admuserid, admusername, administratorname, gradework, admcomment FROM stats WHERE admuserid != 0"):
		await ctx.send(value)
			
#сбросить таблицу rabotaadminov
@bot.command()
@commands.has_permissions( administrator = True )
async def сбростабладм(ctx):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel( logschannel )
	channel4 = bot.get_channel(KIchennel)
	new_name4 = f'🥏К/И: 0/10'	
	sql.execute(f"DELETE FROM stats WHERE admuserid != 0 ")		
	await channel4.edit(name = new_name4)
	print(f'{ctx.author} обнулил таблицу об администрации')
	await ctx.send("таблица rabotaadminov успешно сброшена")
	await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} сбросил таблицу об администрации", color = 0x628ffe, timestamp=ctx.message.created_at ) )
	db.commit()

#сбросить таблицу iventi
@bot.command()
@commands.has_permissions( administrator = True )
async def сбростабливт(ctx):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel( logschannel )
	channel5 = bot.get_channel(RAchannel)
	new_name5 = f'🔩Р/А: 0/10'
	sql.execute(f"DELETE FROM stats WHERE ivtuserid != 0 ")
	await channel5.edit(name = new_name5)
	print(f'{ctx.author} обнулил таблицу об ивентах')
	await ctx.send("таблица iventi успешно сброшена")
	channel = bot.get_channel( logschannel )
	await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} сбросил таблицу об ивентах", color = 0x628ffe, timestamp=ctx.message.created_at ) )
	db.commit()

#удалить отзыв адм
@bot.command()
async def удалитьотзывадм(ctx):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	sql.execute(f"DELETE FROM stats WHERE admuserid == {ctx.author.id} ")
	db.commit()
	print(f'{ctx.author} удалил отзыв об администрации')
	await ctx.send("отзыв успешно удалён")
	channel = bot.get_channel( logschannel )
	await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} удалил отзыв об администрации", color = 0xacdbaa, timestamp=ctx.message.created_at ) )
	
#удалить отзыв ивт
@bot.command()
async def удалитьотзывивт(ctx):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	sql.execute(f"DELETE FROM stats WHERE ivtuserid == {ctx.author.id} ")
	db.commit()
	print(f'{ctx.author} удалил отзыв об ивентах')
	await ctx.send("отзыв успешно удалён")
	channel = bot.get_channel( logschannel )
	await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} удалил отзыв об ивентах", color = 0xacdbaa, timestamp=ctx.message.created_at ) )

#удалить чужой отзыв адм
@bot.command()
@commands.has_permissions( kick_members = True )
async def снятьотзывадм(ctx,  member: discord.Member):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	sql.execute(f"DELETE FROM stats WHERE admuserid == {member.id} ")
	db.commit()
	print(f'{ctx.author} удалил отзыв {member} об администрации')
	await ctx.send(f"отзыв {member} успешно удалён")
	channel = bot.get_channel( logschannel )
	await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} удалил отзыв {member} об администрации", color = 0xacdbaa, timestamp=ctx.message.created_at ) )

#удалить чужой отзыв ивт
@bot.command()
@commands.has_permissions( kick_members = True )
async def снятьотзывивт(ctx,  member: discord.Member):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	sql.execute(f"DELETE FROM stats WHERE ivtuserid == {member.id} ")
	db.commit()
	print(f'{ctx.author} удалил отзыв {member} об ивентах')
	await ctx.send(f"отзыв {member} успешно удалён")
	channel = bot.get_channel( logschannel )
	await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} удалил отзыв {member} об ивентах", color = 0xacdbaa, timestamp=ctx.message.created_at ) )

#=======================================================================Роль за реакцию==============================================================================================

@bot.event
async def on_raw_reaction_add(payload):

	if payload.member.bot:
		pass

	else:
		with open('reactrole.json') as react_file:
			data = json.load(react_file)
			for x in data:
				if x['message_id'] == payload.message_id:   
					if x['emoji'] == payload.emoji.name:
						role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])
						await payload.member.add_roles(role)
					if x['emoji1'] == payload.emoji.name:
						role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])
						await payload.member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):

	with open('reactrole.json') as react_file:
		data = json.load(react_file)
		for x in data:
			if x['message_id'] == payload.message_id: 
				if x['emoji'] == payload.emoji.name:
					role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])
					await bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)
				if x['emoji1'] == payload.emoji.name: 
					role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])
					await bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

@bot.command()
@commands.has_permissions(administrator=True, manage_roles=True)
async def рекроль(ctx, emoji, role: discord.Role, *, message):
    await ctx.channel.purge( limit =1 )
    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)
        new_react_role = {'role_name': role.name,
        'role_id': role.id,
        'emoji': emoji,
        'emoji1': emoji[2: -20],
        'message_id': msg.id}

        data.append(new_react_role)

    with open('reactrole.json', 'w') as f:
        json.dump(data, f, indent=4)

#========================================================предупреждения===========================================================================
#выдать пред
@bot.command()
@commands.has_permissions(kick_members=True)
async def пред(ctx, member: discord.Member, *,comment):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	if member == ctx.author:
		await ctx.send("вы не можете выдать предупреждение самому себе")
	else:
		if member.top_role <= ctx.author.top_role:
			if member.top_role == ctx.author.top_role:
				await ctx.send('Вы не можете выдать предупреждение равному по правам свами')
			else:
				channel = bot.get_channel( warnlogchannel )
				channel1 = bot.get_channel( banlogchannel )
				channel2 = bot.get_channel( mutelogchannel )
				adminname = ctx.author.name
				adminid = ctx.author.id
				userid = member.id
				username = member.name
				guild = ctx.guild
				msg = ctx.message
				perms = discord.Permissions(read_messages = True, read_message_history = True)
				mute_role = discord.utils.get( ctx.message.guild.roles, name = 'мут')
				for sa1 in sql.execute("SELECT COUNT(sluchai) FROM warns"):
					continue
				for count in sql.execute(f"SELECT COUNT(sluchai) + 1 FROM warns WHERE userid = {member.id} "):
					continue
				count1 = str(count)
				count1 = count1[1:-2]
				kolichestvo = count1
				sluchai = sa1[-1]
				sluchai1 = int(sluchai)
				sql.execute(f"INSERT INTO warns VALUES (?,?,?,?,?,?,?,?)", (userid, username, adminname, adminid, sluchai, sluchai1, kolichestvo, comment))
				db.commit()
				await msg.add_reaction('✅')	
				await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь {username} получил предупреждение по причине {comment}. \nСлучай: #{sluchai}", description = f'Имя администратора: {adminname}', color = 0xacdbaa, timestamp=ctx.message.created_at ) )
				await member.send(f"Вы получили предупреждение на сервере **{member.guild.name}**. \nАдминистратор: **{adminname}**. \nСлучай: **#{sluchai}** \nПричина: **{comment}**")
				for sa2 in sql.execute("SELECT COUNT(sluchai) FROM warns WHERE userid = ?", (member.id,)):
					sa3 = sa2[-1]
					
					if sa3 > (count_warns_to_permban -1):
						reason = (f" **Автоматический бан за получение {count_warns_to_permban} предупреждений**")
						await member.ban(reason = reason)
						await member.send(f'вы были забанены на сервере {guild.name} по причине: {reason}')
						await channel.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был забанен по причине: {reason}", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
						return

					if sa3 > (count_warns_to_ban -1):
						time = time_to_warnban
						reason = (f" **Автоматический бан за получение {count_warns_to_ban} предупреждений**")
						await member.ban(reason = reason)
						await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был забанен по причине: {reason} на {time} минут", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff00ff, timestamp=ctx.message.created_at ) )
						
						await asyncio.sleep(time * 60)

						baned_users = await ctx.guild.bans()

						for ban_entry in baned_users:
							user = ban_entry.user

							await ctx.guild.unban(user)
							await channel1.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был разбанен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xf5deb3, timestamp=ctx.message.created_at ) )
							return

					if sa3 >(count_warns_to_mute6 -1):
						reason = (f" **Автоматический мьют за получение {count_warns_to_mute6} предупреждений**")
						time = time_to_warnmute6
						if mute_role == None:
							mute_role = await ctx.guild.create_role(name='мут', permissions=perms)
							await mute_role.edit(color=discord.Color(0x378cdc))
							for channel in guild.channels:
								await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)

						await member.add_roles(mute_role)
						await member.move_to(None)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на {time} минут", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
						await ctx.send(f'{member.mention} получил мьют на {time} минут по причине: {reason}')
						await asyncio.sleep(time * 60)
						await member.remove_roles(mute_role)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был размьючен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
						return
					if sa3 >(count_warns_to_mute5 -1):
						reason = (f" **Автоматический мьют за получение {count_warns_to_mute5} предупреждений**")
						time = time_to_warnmute5
						if mute_role == None:
							mute_role = await ctx.guild.create_role(name='мьют', permissions=perms)
							await mute_role.edit(color=discord.Color(0x378cdc))
							for channel in guild.channels:
								await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)
								
						await member.add_roles(mute_role)
						await member.move_to(None)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на {time} минут", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
						await ctx.send(f'{member.mention} получил мьют на {time} минут по причине: {reason}')
						await asyncio.sleep(time * 60)
						await member.remove_roles(mute_role)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был размьючен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
						return
					if sa3 >(count_warns_to_mute4 -1):
						reason = (f" **Автоматический мьют за получение {count_warns_to_mute4} предупреждений**")
						time = time_to_warnmute4
						if mute_role == None:
							mute_role = await ctx.guild.create_role(name='мут', permissions=perms)
							await mute_role.edit(color=discord.Color(0x378cdc))
							for channel in guild.channels:
								await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)
								
						await member.add_roles(mute_role)
						await member.move_to(None)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на {time} минут", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
						await ctx.send(f'{member.mention} получил мьют на {time} минут по причине: {reason}')
						await asyncio.sleep(time * 60)
						await member.remove_roles(mute_role)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был размьючен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
						return

					if sa3 >(count_warns_to_mute3 -1):
						reason = (f" **Автоматический мьют за получение {count_warns_to_mute3} предупреждений**")
						time = time_to_warnmute3
						if mute_role == None:
							mute_role = await ctx.guild.create_role(name='мут', permissions=perms)
							await mute_role.edit(color=discord.Color(0x378cdc))
							for channel in guild.channels:
								await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)
								
						await member.add_roles(mute_role)
						await member.move_to(None)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на {time} минут", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
						await ctx.send(f'{member.mention} получил мьют на {time} минут по причине: {reason}')
						await asyncio.sleep(time * 60)
						await member.remove_roles(mute_role)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был размьючен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
						return

					if sa3 >(count_warns_to_mute2 -1):
						reason = (f" **Автоматический мьют за получение {count_warns_to_mute2} предупреждений**")
						time = time_to_warnmute2
						if mute_role == None:
							mute_role = await ctx.guild.create_role(name='мьют', permissions=perms)
							await mute_role.edit(color=discord.Color(0x378cdc))
							for channel in guild.channels:
								await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)
								
						await member.add_roles(mute_role)
						await member.move_to(None)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на {time} минут", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
						await ctx.send(f'{member.mention} получил мьют на {time} минут по причине: {reason}')
						await asyncio.sleep(time * 60)
						await member.remove_roles(mute_role)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был размьючен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
						return

					if sa3 >(count_warns_to_mute1 -1):
						reason = (f" **Автоматический мьют за получение {count_warns_to_mute1} предупреждений**")
						time = time_to_warnmute1
						if mute_role == None:
							mute_role = await ctx.guild.create_role(name='мут', permissions=perms)
							await mute_role.edit(color=discord.Color(0x378cdc))
							for channel in guild.channels:
								await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)
								
						await member.add_roles(mute_role)
						await member.move_to(None)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на {time} минут", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
						await ctx.send(f'{member.mention} получил мьют на {time} минут по причине: {reason}')
						await asyncio.sleep(time * 60)
						await member.remove_roles(mute_role)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был размьючен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
						return

					if sa3 >(count_warns_to_mute -1):
						reason = (f" **Автоматический мьют за получение {count_warns_to_mute} предупреждений**")
						time = time_to_warnmute
						if mute_role == None:
							mute_role = await ctx.guild.create_role(name='мут', permissions=perms)
							await mute_role.edit(color=discord.Color(0x378cdc))
							for channel in guild.channels:
								await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)
								
						await member.add_roles(mute_role)
						await member.move_to(None)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был замьючен по причине: {reason} на {time} минут", description = f'Имя пользователя: {member} \n ID пользователя: {member.id}', color = 0xff4500, timestamp=ctx.message.created_at ) )
						await ctx.send(f'{member.mention} получил мьют на {time} минут по причине: {reason}')
						await asyncio.sleep(time * 60)
						await member.remove_roles(mute_role)
						await channel2.send( embed = discord.Embed(title = f"[{dt_string}] Пользователь: {member} был размьючен ", description = f' Время наказания прошло \n \n Имя пользователя: {member} \n ID пользователя: {member.id}' , color = 0xc71585, timestamp=ctx.message.created_at ) )
						return
		else:
			await ctx.send('Вы не можете выдать предупреждение выше уполномоченному админу')

#сбросит преды
@bot.command()
@commands.has_permissions( administrator = True )
async def сброспред(ctx):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	channel = bot.get_channel( logschannel )
	sql.execute(f"DELETE FROM warns WHERE userid == userid ")
	print(f'{ctx.author} обнулил предупреждения')
	await ctx.send("предупреждения успешно сброшены")
	await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} сбросил предупреждения", color = 0x628ffe, timestamp=ctx.message.created_at ) )
	db.commit()

#снятьпред
@bot.command()
@commands.has_permissions( kick_members = True )
async def снятьпред(ctx, sluch):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	print(type(sluch))
	channel = bot.get_channel( logschannel )
	sql.execute("UPDATE warns SET userid = userid * 0 WHERE sluchai = ?", (str(sluch,)))

	print(f'{ctx.author} снял предупреждение **#{sluch}**')
	msg = ctx.message
	await msg.add_reaction('✅')
	await channel.send(embed = discord.Embed(title = f"[{dt_string}] Пользователь: {ctx.author} снял предупреждение #{sluch}", color = 0x628ffe, timestamp=ctx.message.created_at ) )
	db.commit()

#таблица варнов
@bot.command()
@commands.has_permissions( administrator = True )
async def таблварн(ctx):
	await ctx.send('Список варнов')
	for value in sql.execute("SELECT * FROM warns "):
		await ctx.send(value)

#список предов
@bot.command()
async def преды(ctx, member: discord.Member = None):
	if member == None:
		member = ctx.author
	for count in sql.execute(f"SELECT COUNT(sluchai) + 1 FROM warns WHERE userid = {member.id} "):
		continue
	count1 = str(count)
	count1 = count1[1:-2]
	kolichestvo = count1
	kolichestvo = int(kolichestvo)
	channel = bot.get_channel(logschannel)
	for count in sql.execute(f"SELECT COUNT(*) FROM warns WHERE userid = {member.id} "):
		continue

	embed1 = discord.Embed(title=f"Предупреждения **{member}**⠀(Всего: `{count[-1]}` )", color = 0x98F5FF, timestamp=ctx.message.created_at)
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 1 AND userid = {member.id} "):
		print(f'kolichestvo')
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed1.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed1.add_field(name="случай: ", value=f"`#{value3}`")
		embed1.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 2 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed1.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed1.add_field(name="случай: ", value=f"`#{value3}`")
		embed1.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 3 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed1.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed1.add_field(name="случай: ", value=f"`#{value3}`")
		embed1.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 4 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed1.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed1.add_field(name="случай: ", value=f"`#{value3}`")
		embed1.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 5 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed1.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed1.add_field(name="случай: ", value=f"`#{value3}`")
		embed1.add_field(name="Причина: ", value=f"**{value[-1]}**")
	embed1.set_footer(text=f"Команду вызвал: {ctx.author}, \nID ({ctx.author.id})")
	embed2 = discord.Embed(title=f"Предупреждения **{member}**⠀(Всего: `{count[-1]}` )", color = 0x98F5FF, timestamp=ctx.message.created_at)
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 6 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed2.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed2.add_field(name="случай: ", value=f"`#{value3}`")
		embed2.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 7 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed2.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed2.add_field(name="случай: ", value=f"`#{value3}`")
		embed2.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 8 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed2.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed2.add_field(name="случай: ", value=f"`#{value3}`")
		embed2.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 9 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed2.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed2.add_field(name="случай: ", value=f"`#{value3}`")
		embed2.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 10 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]
		embed2.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed2.add_field(name="случай: ", value=f"`#{value3}`")
		embed2.add_field(name="Причина: ", value=f"**{value[-1]}**")
	embed2.set_footer(text=f"Команду вызвал: {ctx.author}, \nID ({ctx.author.id})")	
	embed3 = discord.Embed(title=f"Предупреждения **{member}**⠀(Всего: `{count[-1]}` )", color = 0x98F5FF, timestamp=ctx.message.created_at)
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 11 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed3.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed3.add_field(name="случай: ", value=f"`#{value3}`")
		embed3.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 12 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed3.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed3.add_field(name="случай: ", value=f"`#{value3}`")
		embed3.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 13 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed3.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed3.add_field(name="случай: ", value=f"`#{value3}`")
		embed3.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 14 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed3.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed3.add_field(name="случай: ", value=f"`#{value3}`")
		embed3.add_field(name="Причина: ", value=f"**{value[-1]}**")
	for value in sql.execute(f"SELECT * FROM warns WHERE kolichestvo = 15 AND userid = {member.id} "):
		value1 = {value[2:-5]}
		value1 = (str(value1))
		value1 = value1[3: -4]
		value2 = {value[3: -4]}
		value2 = (str(value2))
		value2 = value2[3: -4]
		value3 = {value[4:-3]}
		value3 = (str(value3))
		value3 = value3[3: -4]	
		embed3.add_field(name="Имя администратора: ", value=f"**{value1}**(**{value2}**)")
		embed3.add_field(name="случай: ", value=f"`#{value3}`")
		embed3.add_field(name="Причина: ", value=f"**{value[-1]}**")
	embed3.set_footer(text=f"Команду вызвал: {ctx.author}, \nID ({ctx.author.id})")
	embeds = [embed1, embed2, embed3]
	message = await ctx.reply(embed=embed1)
	page = Paginator(bot, message, only=ctx.author, use_more=False, embeds=embeds)
	await page.start()
#====================================================================тикеты============================================================================
@bot.command()
@commands.has_permissions(administrator = True)
async def тикстарт(ctx):
	select = Select(
		placeholder="Выбрать разновидности тикетов",
		min_values=1,
		max_values=5,
		options= [
			discord.SelectOption(
				label= "Пожелания", 
				emoji= '📬',
				description='Пользователи смогут оставить свои пожелания', 
				value='0'
			),
			discord.SelectOption(
				label= "Жалобы", 
				emoji= '🛑',
				description='Пользователи смогут оставить свои жалобы', 
				value='1'

			),
			discord.SelectOption(
				label= "Апелляция наказания", 
				emoji= '📝',
				description='Пользователи смогут подать апелляцию', 
				value='2'

			),
			discord.SelectOption(
				label= "Вопросы", 
				emoji= '❓',
				description='Пользователи смогут оставить свои вопросы',
				default = True, 
				value='3'
			),
			discord.SelectOption(
				label= "Kara$1k bugreport", 
				emoji= '🔧',
				description='Пользователи смогут сообщить о некорректной работе бота', 
				value='4'

			)
		],
	)
	async def my_callbak(interaction):
		await ctx.channel.purge( limit =1 )
		now = datetime.now()
		dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
		role1 = discord.utils.find(lambda r: r.id == Prole, ctx.message.guild.roles)
		role2 = discord.utils.find(lambda r: r.id == Arole, ctx.message.guild.roles)
		if role1 == None:
			embed1 = discord.Embed(title = f"Администраторская роль не найдена ", description= "Укажите роль в конфигах", color = 0x628ffe)
			await ctx.send(embed = embed1, view = view)
		if role2 == None:
			role2 == ctx.guild.default_role
		mute_role = discord.utils.get( ctx.message.guild.roles, name = 'мьют')
		category3 = await ctx.guild.create_category(name = "╔━━━━━⟪Связь⟫━━━━━╗",position = 0)
		category1 = await ctx.guild.create_category(name = "╔━━━━━⟪Активные Тикеты⟫━━━━━╗",position = 0)
		category2 = await ctx.guild.create_category(name = "╔━━━━━⟪Архивированные тикеты⟫━━━━━╗",position = 0)
		await interaction.response.send_message(f"Настраиваем тикеты. Ожидайте...", ephemeral=True)
		channel1 = None
		channel2 = None
		channel3 = None
		channel4 = None
		channel5 = None

		for tiketype0 in select.values:
			if tiketype0 == '0':
				channel1 = await ctx.guild.create_text_channel(name = f'╔━⟪📬⟫━╗•Пожелания', category = category3)
				await channel1.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False)

		for tiketype1 in select.values:
			if tiketype1 == '1':
				channel2 = await ctx.guild.create_text_channel(name = f'╠━⟪🛑⟫━╣•Жалобы', category = category3)
				await channel2.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False)

		for tiketype2 in select.values:
			if tiketype2 == '2':
				channel3 = await ctx.guild.create_text_channel(name = f'╠━⟪📝⟫━╣•Апелляция наказания', category = category3)
				await channel3.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False)

		for tiketype3 in select.values:
			if tiketype3 == '3':
				channel4 = await ctx.guild.create_text_channel(name = f'╠━⟪ ❓ ⟫━╣•Вопросы', category = category3)
				await channel4.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False)

		for tiketype4 in select.values:
			if tiketype4 == '4':
				channel5 = await ctx.guild.create_text_channel(name = f'╚━⟪🔧⟫━╝•Kara$1k bugreport', category = category3)
				await channel5.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False)

		logchannel = bot.get_channel(logschannel)
		await category1.set_permissions(role1, read_messages=True, connect=False, speak=False, view_channel=False)
		await category2.set_permissions(role1, read_messages=False, send_messages=False, connect=False, speak=False, view_channel=False)
		await category1.set_permissions(role2, read_messages=True,  connect=False, speak=False, view_channel=True)
		await category2.set_permissions(role2, read_messages=False, send_messages=False, connect=False, speak=False, view_channel=True)

		if channel1 == None:
			channel1_id = 0
		else:
			channel1_id = channel1.id
		if channel2 == None:
			channel2_id = 0
		else:
			channel2_id = channel2.id
		if channel3 == None:
			channel3_id = 0
		else:
			channel3_id = channel3.id
		if channel4 == None:
			channel4_id = 0
		else:
			channel4_id = channel4.id
		if channel5 == None:
			channel5_id = 0
		else:
			channel5_id = channel5.id

		with open('tiketcannelinfo.json') as json_file:
			data = json.load(json_file)
			ss1 = {
			'category1': category1.id,
			'category2': category2.id,
			'category3': category3.id,
			'channel1': channel1_id,
			'channel2': channel2_id,
			'channel3': channel3_id,
			'channel4': channel4_id,
			'channel5': channel5_id}
		
			data.append(ss1)

		with open('tiketcannelinfo.json', 'w') as f:
			json.dump(data, f, indent=4)

		number = 1

		if 0 == 0:
			button1 = Button(label = 'Пожелание', style = discord.ButtonStyle.green, emoji = "📄")
			async def button_callback(interaction):
				member1 = interaction.user        
				channel6 = await ctx.guild.create_text_channel(name = f'Тикет - П{number}', category = category1, position = 0)

				embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
				lembed = discord.Embed(title= f'[{dt_string}] {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
				await logchannel.send(embed = lembed)
				await interaction.response.send_message(embed = embed0, ephemeral=True)
				await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
				await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
				embed = discord.Embed(title = f" **Форма подачи предложения:**", description = f'`1.` Подробное предложение : \n`2.` Почему вы считаете что, предложенное вами будет полезным :  ', color = 0x628ffe)
				embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
				button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
				await channel6.send(member1.mention)
				async def button_callback(interaction):
					await interaction.response.edit_message(content = embed, view = None)
					await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
					await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
					await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
					await channel6.edit(category = category2)
					embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
					button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
					button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
					embed8 = discord.Embed(title = 'Закрываем тикет...')
					async def button_callback(interaction):
						member2 = interaction.user
						lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed2)
						await channel6.delete(reason=None) 
						await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
					async def button_callback1(interaction):
						embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						await channel6.edit(category = category1)
						await interaction.response.edit_message(content = embed111, view = None)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							async def button_callback(interaction):
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
							async def button_callback1(interaction):
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                
										await channel6.delete(reason=None) 
										await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
									button111.callback = button_callback
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed1111, view = view)
						button111.callback = button_callback
					button1111.callback = button_callback1
					view = View(timeout = None)
					await channel6.send(embed = embed8)
					await asyncio.sleep(1 * 3)
					view.add_item(button111)
					view.add_item(button1111)
					await channel6.send(embed = embed111, view = view)
				button11.callback = button_callback
				view = View(timeout = None)
				view.add_item(button11)
				await channel6.send(embed = embed, view = view)
			button1.callback = button_callback
			view = View(timeout = None)
			view.add_item(button1)
			if channel1 != None:
				embed9 = discord.Embed(title = f"Если вы желаете оставить своё пожелание, то нажмите на кнопку под этим сообщением. Наши администраторы рассмотрят его в ближайшее время.", description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
				await channel1.send(embed = embed9, view = view)

		if 0 == 0:
			button2 = Button( label = 'Жалоба', style = discord.ButtonStyle.green, emoji = "📄")
			async def button_callback(interaction):
				member1 = interaction.user        
				channel6 = await ctx.guild.create_text_channel(name = f'Тикет - Ж{number}', category = category1, position = 0)
				embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
				lembed = discord.Embed(title= f'[{dt_string}] Пользователь: {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
				await logchannel.send(embed = lembed)
				await interaction.response.send_message(embed = embed0, ephemeral=True)
				await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
				await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
				embed = discord.Embed(title = f"**Форма подачи жалобы:**", description = f'`1.` Никнейм того на кого Вы хотите подать жалобу (никнейм в SCP:SL/Discord, в зависимости где были нарушены правила) : \n`2.` Подробное описание нарушения : \n`3.` Доказательства нарушения :', color = 0x628ffe)
				embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
				button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
				await channel6.send(member1.mention)
				async def button_callback(interaction):
					await interaction.response.edit_message(content = embed, view = None)
					await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
					await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
					await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
					await channel6.edit(category = category2)
					embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
					button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
					button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
					embed8 = discord.Embed(title = 'Закрываем тикет...')
					async def button_callback(interaction):
						member2 = interaction.user
						lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed2)
						await channel6.delete(reason=None) 
						await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
					async def button_callback1(interaction):
						embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						await channel6.edit(category = category1)
						await interaction.response.edit_message(content = embed111, view = None)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							async def button_callback(interaction):
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
							async def button_callback1(interaction):
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                
										await channel6.delete(reason=None) 
										await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
									button111.callback = button_callback
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed1111, view = view)
						button111.callback = button_callback
					button1111.callback = button_callback1
					view = View(timeout = None)
					await channel6.send(embed = embed8)
					await asyncio.sleep(1 * 3)
					view.add_item(button111)
					view.add_item(button1111)
					await channel6.send(embed = embed111, view = view)
				button11.callback = button_callback
				view = View(timeout = None)
				view.add_item(button11)
				await channel6.send(embed = embed, view = view)
			button2.callback = button_callback
			view = View(timeout = None)
			view.add_item(button2)
			if channel2 != None:
				embed10 = discord.Embed(title = f"Если вы желаете оставить жалобу на нарушение правил, то нажмите на кнопку под этим сообщением. Наши администраторы рассмотрят её в ближайшее время." , description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
				await channel2.send(embed = embed10, view = view)

		if 0 == 0:
			button3 = Button(label = 'Апелляция',style = discord.ButtonStyle.green, emoji = "📄")
			async def button_callback(interaction):
				member1 = interaction.user        
				channel6 = await ctx.guild.create_text_channel(name = f'Тикет - А{number}', category = category1, position = 0)
				embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
				lembed = discord.Embed(title= f'[{dt_string}] Пользователь: {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
				await logchannel.send(embed = lembed)
				await interaction.response.send_message(embed = embed0, ephemeral=True)
				await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
				await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
				embed = discord.Embed(title = f"**Форма подачи апелляции:**", description = f'`1.` Ваш никнейм (никнейм в SCP:SL/Discord, в зависимости где было выдано наказание) : \n`2.` Никнейм администратора который выдал наказание : \n`3.` Какое наказание было выдано : \n`4.` Подробное описание за что вы получили наказание : \n`5.` Почему вы считаете что наказание было выдано не честно :', color = 0x628ffe)
				embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
				button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
				await channel6.send(member1.mention)
				async def button_callback(interaction):
					await interaction.response.edit_message(content = embed, view = None)
					await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
					await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
					await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
					await channel6.edit(category = category2)
					embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
					button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
					button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
					embed8 = discord.Embed(title = 'Закрываем тикет...')
					async def button_callback(interaction):
						member2 = interaction.user
						lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed2)
						await channel6.delete(reason=None) 
						await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
					async def button_callback1(interaction):
						embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						await channel6.edit(category = category1)
						await interaction.response.edit_message(content = embed111, view = None)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							async def button_callback(interaction):
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
							async def button_callback1(interaction):
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                
										await channel6.delete(reason=None) 
										await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
									button111.callback = button_callback
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed1111, view = view)
						button111.callback = button_callback
					button1111.callback = button_callback1
					view = View(timeout = None)
					await channel6.send(embed = embed8)
					await asyncio.sleep(1 * 3)
					view.add_item(button111)
					view.add_item(button1111)
					await channel6.send(embed = embed111, view = view)
				button11.callback = button_callback
				view = View(timeout = None)
				view.add_item(button11)
				await channel6.send(embed = embed, view = view)
			button3.callback = button_callback
			view = View(timeout = None)
			view.add_item(button3)
			if channel3 != None:
				embed11 = discord.Embed(title = f"Если вы желаете обжаловать своё наказание, то нажмите на кнопку под этим сообщением. Наши администраторы рассмотрят апелляцию в ближайшее время.", description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
				await channel3.send(embed = embed11, view = view)

		if 0 == 0:
			button4 = Button(label = 'Вопрос',style = discord.ButtonStyle.green, emoji = "❓")
			async def button_callback(interaction):
				member1 = interaction.user        
				channel6 = await ctx.guild.create_text_channel(name = f'Тикет - В{number}', category = category1, position = 0)
				embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
				lembed = discord.Embed(title= f'[{dt_string}] Пользователь: {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
				await logchannel.send(embed = lembed)
				await interaction.response.send_message(embed = embed0, ephemeral=True)
				await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
				await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
				embed = discord.Embed(title = f"**Форма подачи вопроса:**", description = f'`1.` Краткое описание вашего вопроса: \n`2.` К чему относится(scpsl/discord) : \n`3.` Подробно распишите вопрос: ', color = 0x628ffe)
				embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
				button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
				await channel6.send(member1.mention)
				async def button_callback(interaction):
					await interaction.response.edit_message(content = embed, view = None)
					await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
					await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
					await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
					await channel6.edit(category = category2)
					embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
					button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
					button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
					embed8 = discord.Embed(title = 'Закрываем тикет...')
					async def button_callback(interaction):
						member2 = interaction.user
						lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed2)
						await channel6.delete(reason=None) 
						await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
					async def button_callback1(interaction):
						embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						await channel6.edit(category = category1)
						await interaction.response.edit_message(content = embed111, view = None)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							async def button_callback(interaction):
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
							async def button_callback1(interaction):
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                
										await channel6.delete(reason=None) 
										await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
									button111.callback = button_callback
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed1111, view = view)
						button111.callback = button_callback
					button1111.callback = button_callback1
					view = View(timeout = None)
					await channel6.send(embed = embed8)
					await asyncio.sleep(1 * 3)
					view.add_item(button111)
					view.add_item(button1111)
					await channel6.send(embed = embed111, view = view)
				button11.callback = button_callback
				view = View(timeout = None)
				view.add_item(button11)
				await channel6.send(embed = embed, view = view)
			button4.callback = button_callback
			view = View(timeout = None)
			view.add_item(button4)
			if channel4 != None:
				embed12 = discord.Embed(title = f"Если у вас есть вопрос по тематике сервера, то нажмите сюда и заполните тикет. Наши администраторы рассмотрят Вопрос в ближайшее время.", description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
				await channel4.send(embed = embed12, view = view)

		if 0 == 0:
			button5 = Button(label = 'Сообщить',style = discord.ButtonStyle.green, emoji = "🔧")
			async def button_callback(interaction):
				member1 = interaction.user        
				channel6 = await ctx.guild.create_text_channel(name = f'Тикет - К{number}', category = category1, position = 0)
				embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
				lembed = discord.Embed(title= f'[{dt_string}] Пользователь: {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
				await logchannel.send(embed = lembed)
				await interaction.response.send_message(embed = embed0, ephemeral=True)
				await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
				await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
				await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
				embed = discord.Embed(title = f"**Форма подачи баг репорта:**", description = f'`1.` Краткое описание бага/ошибки/недоработки: \n`2.` Как вы его обнаружили: \n`3.` **(Необязательно)**  Дополнительная информация о баге: ', color = 0x628ffe)
				embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
				button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
				await channel6.send(member1.mention)
				async def button_callback(interaction):
					await interaction.response.edit_message(content = embed, view = None)
					await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
					await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
					await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
					await channel6.edit(category = category2)
					embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
					button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
					button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
					embed8 = discord.Embed(title = 'Закрываем тикет...')
					async def button_callback(interaction):
						member2 = interaction.user
						lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed2)
						await channel6.delete(reason=None) 
						await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
					async def button_callback1(interaction):
						embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						await channel6.edit(category = category1)
						await interaction.response.edit_message(content = embed111, view = None)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							async def button_callback(interaction):
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
							async def button_callback1(interaction):
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] {member2} удалил тикет **{channel6.name}**', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                
										await channel6.delete(reason=None) 
										await member2.send(f'{member2.mention} **{channel6.name}** был удалён')
									button111.callback = button_callback
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed1111, view = view)
						button111.callback = button_callback
					button1111.callback = button_callback1
					view = View(timeout = None)
					await channel6.send(embed = embed8)
					await asyncio.sleep(1 * 3)
					view.add_item(button111)
					view.add_item(button1111)
					await channel6.send(embed = embed111, view = view)
				button11.callback = button_callback
				view = View(timeout = None)
				view.add_item(button11)
				await channel6.send(embed = embed, view = view)
			button5.callback = button_callback
			view = View(timeout = None)
			view.add_item(button5)
			if channel5 != None:
				embed13 = discord.Embed(title = f"Если вы обнаружили баг/ошибку/недоработку, то нажмите сюда и заполните тикет. Наши администраторы рассмотрят репорт в ближайшее время.", description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
				await channel5.send(embed = embed13, view = view)

			embed1 = discord.Embed(title = f' Желаете создать каналы с подсказками?("Для чего нужна эта категория")')

			button11 = Button(label = 'да', style = discord.ButtonStyle.blurple, emoji = "✅")
			async def button_callback(interaction):
				await ctx.channel.purge( limit =1 )
				channel6 = await ctx.guild.create_text_channel(name = f'Для чего нужна эта категория?', category = category1)
				channel7 = await ctx.guild.create_text_channel(name = f'Для чего нужна эта категория?', category = category2)

				with open('tiketcannelinfo.json') as json_file:
					data = json.load(json_file)
					ss1 = {
						'channel6': channel6.id,
						'channel7': channel7.id}

					data.append(ss1)

				with open('tiketcannelinfo.json', 'w') as f:
					json.dump(data, f, indent=4)

				if channel6 == None:
					print('канал 6 не найден')
				else:
					await channel6.send(embed = discord.Embed(title = f"Для чего нужна эта категория?", description = (f'В этой категории будут храниться тикеты созданные обычными игроками для того, чтобы пожаловаться на игрока, предложить идею для улучшения сервера или подать апелляцию. Задача администратора по его мере возможностей решать' 
						'проблемы и выслушивать людей до того момента, пока тикет не закроет его создатель. Обычные правила распространяются на тикеты, поэтому вы можете выдать наказание в нём при нарушении правила. \n \n Нумерация тикета происходит следующим образом.\n `[тип тикета]` `[номер тикета]`'
						'\n\n Типы могут быть следующие: \n **П** - `пожелание/просьба` \n **Ж** - `жалоба` \n **A** - `апелляция` \n **В** - `Вопрос` \n **К** - `Kara$1k Багрепорт`\n \n Нумерация происходит по порядковому номеру тикета'), color = 0x628ffe) )
				if channel7 == None:
					print('канал 7 не найден')
				else:
					await channel7.send(embed = discord.Embed(title = f"Для чего нужна эта категория?", description = (f'В этой категории будут хранится закрытые тикиты. Данную категорию можно назвать архивом. Тикеты из этой категории запрещено редактировать или удалять без разрешения главы сервера. '
						'\n \n Нумерация тикета происходит следующим образом.\n `[тип тикета]` `[номер тикета]` \n\n Типы могут быть следующие: \n **П** - `пожелание/просьба` \n **Ж** - `жалоба` \n **A** - `апелляция` \n **В** - `Вопрос` \n **К** - `Kara$1k Багрепорт`\n \n Нумерация происходит по порядковому номеру тикета'), color = 0x628ffe) )

			button22 = Button(label = 'нет', style = discord.ButtonStyle.blurple, emoji = "❌")
			async def button_callback1(interaction):
				await ctx.channel.purge( limit =1 )

			button11.callback = button_callback
			button22.callback = button_callback1
			view = View(timeout = None)
			view.add_item(button11)
			view.add_item(button22)
			await ctx.send(embed = embed1, view = view)

	select.callback = my_callbak
	view = View()
	view.add_item(select)

	embed = discord.Embed(title = "Выбор тикетов", description = "Выберите разновидности тикетов, которые хотите видеть на своём сервере \n"
		"\n Для изменения своего выбора необходимо пересоздать тикеты", color = 0x628ffe, timestamp=ctx.message.created_at)
	await ctx.send(embed = embed, view = view)

#обновление тикетов
#Внимание!!! работает некорректно
@bot.command()
@commands.has_permissions(administrator=True)
async def тикобнов(ctx):
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S  %d.%m.%Y")
	logchannel = bot.get_channel(logschannel)
	role1 = discord.utils.find(lambda r: r.id == Prole, ctx.message.guild.roles)
	role2 = discord.utils.find(lambda r: r.id == Arole, ctx.message.guild.roles)
	mute_role = discord.utils.get( ctx.message.guild.roles, name = 'мьют')

	lembed3 = discord.Embed(title= f'[{dt_string}] Пользователь:{ctx.author} востановил тикеты', color = 0xCCFFE5)
	await logchannel.send(embed = lembed3)   

	if 1 == 1:
		if 1 == 1:
			with open('tiketcannelinfo.json') as react_file:
				data = json.load(react_file)
				for x in data:
					if x['channel1'] == None:
						pass
					if x['channel2'] == None:
						pass
					if x['channel3'] == None:
						pass
					if x['channel4'] == None:
						pass
					if x['channel5'] == None:
						pass
					else:
						k1 = x['category1']
						k2 = x['category2']
						k3 = x['category2']
						c1 = x['channel1']
						c2 = x['channel2']
						c3 = x['channel3']
						c4 = x['channel4']
						c5 = x['channel5']
						c6 = x['channel6']
						c7 = x['channel7']
						print(k1)
						print(k2)
						print(k3)
				category1 = discord.utils.get(ctx.guild.categories, id = {k1})
				category2 = discord.utils.get(ctx.guild.categories, id = {k2})
				category3 = discord.utils.get(ctx.guild.categories, id = {k3})
				channel1 = bot.get_channel(c1)
				channel2 = bot.get_channel(c2)
				channel3 = bot.get_channel(c3)
				channel4 = bot.get_channel(c4)
				channel5 = bot.get_channel(c5)
				channel6 = bot.get_channel(c6)
				channel7 = bot.get_channel(c7)
				channel6 = await ctx.guild.create_text_channel(name = f'тест 1', category = category1)
				number = 1

				if channel1 == None:
					print('канал 1 не найден')
				else:
					button1 = Button(label = 'пожелание', style = discord.ButtonStyle.green, emoji = "📄")
					async def button_callback(interaction):
						member1 = interaction.user        
						channel6 = await ctx.guild.create_text_channel(name = f'Тикет - П{number}', category = category1, position = 0)
						embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
						lembed = discord.Embed(title= f'[{dt_string}] Пользователь:{member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed)
						await interaction.response.send_message(embed = embed0, ephemeral=True)
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						embed = discord.Embed(title = f" **Форма подачи предложения:**", description = f"'1.' Подробное предложение : \n'2.' Почему вы считаете что предложение будет полезным :  ", color = 0x628ffe)
						embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
						button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
						await channel6.send(member1.mention)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
							button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
							button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
							embed8 = discord.Embed(title = 'Закрываем тикет...')
							async def button_callback(interaction): 
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь:{member2} удалил тикет {channel6.name}', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)               
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} {channel6.name} был удалён')
							async def button_callback1(interaction):
								embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction): 
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)               
										await channel6.delete(reason=None)
										await member2.send(f'{member2.mention} {channel6.name} был удалён')
									async def button_callback1(interaction):
										await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
										await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
										await channel6.edit(category = category1)
										await interaction.response.edit_message(content = embed111, view = None)
										async def button_callback(interaction):
											await interaction.response.edit_message(content = embed, view = None)
											await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
											await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
											await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
											await channel6.edit(category = category2)
											async def button_callback(interaction):
												member2 = interaction.user
												lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
												await logchannel.send(embed = lembed2)                
												await channel6.delete(reason=None)
												await member2.send(f'{member2.mention} {channel6.name} был удалён')
											button111.callback = button_callback
											view = View(timeout = None)
											await channel6.send(embed = embed8)
											await asyncio.sleep(1 * 3)
											view.add_item(button111)
											await channel6.send(embed = embed111, view = view)
										button11.callback = button_callback
										view = View(timeout = None)
										view.add_item(button11)
										await channel6.send(embed = embed1111, view = view)
									button111.callback = button_callback
									button1111.callback = button_callback1
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									view.add_item(button1111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed, view = view)
					button1.callback = button_callback
					view = View(timeout = None)
					view.add_item(button1)
					embed9 = discord.Embed(title = f"Если вы желаете оставить своё пожелание, то нажмите на кнопку под этим сообщением. Наши администраторы рассмотрят его в ближайшее время.", description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
					await channel1.send(embed = embed9, view = view)


				if channel2 == None:
					print('канал 2 не найден')
				else:
					button2 = Button( label = 'жалоба', style = discord.ButtonStyle.green, emoji = "📄")
					async def button_callback(interaction):
						member1 = interaction.user        
						channel6 = await ctx.guild.create_text_channel(name = f'Тикет - Ж{number}', category = category1, position = 0)
						embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
						lembed = discord.Embed(title= f'[{dt_string}] Пользователь: {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed)
						await interaction.response.send_message(embed = embed0, ephemeral=True)
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						embed = discord.Embed(title = f"**Форма подачи жалобы:**", description = f"'1.' Никнейм того на кого Вы хотите подать жалобу (никнейм в SCP:SL/Discord, в зависимости где были нарушены правила) : \n'2.' Подробное описание нарушения : \n3. Доказательства нарушения :", color = 0x628ffe)
						embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
						button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
						await channel6.send(member1.mention)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
							button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
							button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
							embed8 = discord.Embed(title = 'Закрываем тикет...')
							async def button_callback(interaction):
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                       
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} {channel6.name} был удалён')
							async def button_callback1(interaction):
								embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                        
										await channel6.delete(reason=None)
										await member2.send(f'{member2.mention} {channel6.name} был удалён')
									async def button_callback1(interaction):
										await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
										await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
										await channel6.edit(category = category1)
										await interaction.response.edit_message(content = embed111, view = None)
										async def button_callback(interaction):
											await interaction.response.edit_message(content = embed, view = None)
											await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
											await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
											await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
											await channel6.edit(category = category2)
											async def button_callback(interaction):  
												member2 = interaction.user
												lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
												await logchannel.send(embed = lembed2)                      
												await channel6.delete(reason=None)
												await member2.send(f'{member2.mention} {channel6.name} был удалён')
											button111.callback = button_callback
											view = View(timeout = None)
											await channel6.send(embed = embed8)
											await asyncio.sleep(1 * 3)
											view.add_item(button111)
											await channel6.send(embed = embed111, view = view)
										button11.callback = button_callback
										view = View(timeout = None)
										view.add_item(button11)
										await channel6.send(embed = embed1111, view = view)
									button111.callback = button_callback
									button1111.callback = button_callback1
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									view.add_item(button1111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed, view = view)
					button2.callback = button_callback
					view = View(timeout = None)
					view.add_item(button2)
					embed10 = discord.Embed(title = f"Если вы желаете оставить жалобу на нарушение правил, то нажмите на кнопку под этим сообщением. Наши администраторы рассмотрят её в ближайшее время." , description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
					await channel2.send(embed = embed10, view = view)

					
				if channel3 == None:
					print('канал 3 не найден')
				else:
					button3 = Button(label = 'апелляция',style = discord.ButtonStyle.green, emoji = "📄")
					async def button_callback(interaction):
						member1 = interaction.user        
						channel6 = await ctx.guild.create_text_channel(name = f'Тикет - А{number}', category = category1, position = 0)
						embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
						lembed = discord.Embed(title= f'[{dt_string}] Пользователь: {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed)
						await interaction.response.send_message(embed = embed0, ephemeral=True)
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						embed = discord.Embed(title = f"**Форма подачи апелляции:**", description = f'`1.` Ваш никнейм (никнейм в SCP:SL/Discord, в зависимости где было выдано наказание) : \n2. Никнейм администратора который выдал наказание : \n3. Какое наказание было выдано : \n4. Подробное описание за что вы получили наказание : \n5. Почему вы считаете что наказание было выдано не честно :', color = 0x628ffe)
						embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
						button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
						await channel6.send(member1.mention)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
							button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
							button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
							embed8 = discord.Embed(title = 'Закрываем тикет...')
							async def button_callback(interaction): 
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                       
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} {channel6.name} был удалён')
							async def button_callback1(interaction):
								embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                        
										await channel6.delete(reason=None)
										await member2.send(f'{member2.mention} {channel6.name} был удалён')
									async def button_callback1(interaction):
										await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
										await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
										await channel6.edit(category = category1)
										await interaction.response.edit_message(content = embed111, view = None)
										async def button_callback(interaction):
											await interaction.response.edit_message(content = embed, view = None)
											await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
											await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
											await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
											await channel6.edit(category = category2)
											async def button_callback(interaction):
												member2 = interaction.user
												lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
												await logchannel.send(embed = lembed2)                
												await channel6.delete(reason=None)
												await member2.send(f'{member2.mention} {channel6.name} был удалён')
											button111.callback = button_callback
											view = View(timeout = None)
											await channel6.send(embed = embed8)
											await asyncio.sleep(1 * 3)
											view.add_item(button111)
											await channel6.send(embed = embed111, view = view)
										button11.callback = button_callback
										view = View(timeout = None)
										view.add_item(button11)
										await channel6.send(embed = embed1111, view = view)
									button111.callback = button_callback
									button1111.callback = button_callback1
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									view.add_item(button1111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed, view = view)
					button3.callback = button_callback
					view = View(timeout = None)
					view.add_item(button3)
					embed11 = discord.Embed(title = f"Если вы желаете обжаловать своё наказание, то нажмите на кнопку под этим сообщением. Наши администраторы рассмотрят апелляцию в ближайшее время.", description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
					await channel3.send(embed = embed11, view = view)

				if channel4 == None:
					print('канал 4 не найден')
				else:
					button4 = Button(label = 'Вопрос',style = discord.ButtonStyle.green, emoji = " ❓ ")
					async def button_callback(interaction):
						member1 = interaction.user        
						channel6 = await ctx.guild.create_text_channel(name = f'Тикет - В{number}', category = category1, position = 0)
						embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
						lembed = discord.Embed(title= f'[{dt_string}] Пользователь: {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed)
						await interaction.response.send_message(embed = embed0, ephemeral=True)
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						embed = discord.Embed(title = f"**Форма подачи вопроса:**", description = f'`1.` Краткое описание вашего вопроса: \n`2.` К чему относится(scpsl/discord) : \n`3.` Подробно распишите вопрос: ', color = 0x628ffe)
						embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
						button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
						await channel6.send(member1.mention)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
							button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
							button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
							embed8 = discord.Embed(title = 'Закрываем тикет...')
							async def button_callback(interaction): 
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь:{member2} удалил тикет {channel6.name}', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                       
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} {channel6.name} был удалён')
							async def button_callback1(interaction):
								embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                        
										await channel6.delete(reason=None)
										await member2.send(f'{member2.mention} {channel6.name} был удалён')
									async def button_callback1(interaction):
										await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
										await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
										await channel6.edit(category = category1)
										await interaction.response.edit_message(content = embed111, view = None)
										async def button_callback(interaction):
											await interaction.response.edit_message(content = embed, view = None)
											await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
											await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
											await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
											await channel6.edit(category = category2)
											async def button_callback(interaction):
												member2 = interaction.user
												lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
												await logchannel.send(embed = lembed2)                
												await channel6.delete(reason=None)
												await member2.send(f'{member2.mention} {channel6.name} был удалён')
											button111.callback = button_callback
											view = View(timeout = None)
											await channel6.send(embed = embed8)
											await asyncio.sleep(1 * 3)
											view.add_item(button111)
											await channel6.send(embed = embed111, view = view)
										button11.callback = button_callback
										view = View(timeout = None)
										view.add_item(button11)
										await channel6.send(embed = embed1111, view = view)
									button111.callback = button_callback
									button1111.callback = button_callback1
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									view.add_item(button1111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed, view = view)
					button4.callback = button_callback
					view = View(timeout = None)
					view.add_item(button4)
					embed11 = discord.Embed(title = f"Если у вас есть вопрос по тематике сервера, то нажмите сюда и заполните тикет. Наши администраторы рассмотрят Вопрос в ближайшее время.", description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
					await channel4.send(embed = embed11, view = view)

				if channel5 == None:
					print('канал 5 не найден')
				else:
					button5 = Button(label = 'Сообщить',style = discord.ButtonStyle.green, emoji = "🔧")
					async def button_callback(interaction):
						member1 = interaction.user        
						channel6 = await ctx.guild.create_text_channel(name = f'Тикет - К{number}', category = category1, position = 0)
						embed0 = discord.Embed(title = f"Ваш тикет создан (**{channel6.name}**)")
						lembed = discord.Embed(title= f'[{dt_string}] Пользователь: {member1} создал тикет **{channel6.name}**', color = 0xFFFF99)
						await logchannel.send(embed = lembed)
						await interaction.response.send_message(embed = embed0, ephemeral=True)
						await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
						await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
						await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
						embed = discord.Embed(title = f"**Форма подачи баг репорта:**", description = f'`1.` Краткое описание бага/ошибки/недоработки: \n`2.` Как вы его обнаружили: \n`3.` **(Необязательно)**  Дополнительная информация о баге: ', color = 0x628ffe)
						embed.set_footer(text=f'"Внимание! на тикеты так же распространяются правила. Постарайтесь не нарушать их."\n')
						button11 = Button(label = 'закрыть', style = discord.ButtonStyle.red, emoji = "📑")
						await channel6.send(member1.mention)
						async def button_callback(interaction):
							await interaction.response.edit_message(content = embed, view = None)
							await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
							await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
							await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
							await channel6.edit(category = category2)
							embed111 = discord.Embed(title = f" Тикет был закрыт и помещён в архив")
							button111 = Button(label = 'удалить тикет', style = discord.ButtonStyle.blurple, emoji = "🚫")
							button1111 = Button(label = 'открыть тикет', style = discord.ButtonStyle.green, emoji = "🔄")
							embed8 = discord.Embed(title = 'Закрываем тикет...')
							async def button_callback(interaction): 
								member2 = interaction.user
								lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
								await logchannel.send(embed = lembed2)                       
								await channel6.delete(reason=None)
								await member2.send(f'{member2.mention} {channel6.name} был удалён')
							async def button_callback1(interaction):
								embed1111 = discord.Embed(title = f" Тикет был открыт для повторного рассмотрения")
								await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
								await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
								await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
								await channel6.edit(category = category1)
								await interaction.response.edit_message(content = embed111, view = None)
								async def button_callback(interaction):
									await interaction.response.edit_message(content = embed, view = None)
									await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
									await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
									await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
									await channel6.edit(category = category2)
									async def button_callback(interaction):
										member2 = interaction.user
										lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
										await logchannel.send(embed = lembed2)                        
										await channel6.delete(reason=None)
										await member2.send(f'{member2.mention} {channel6.name} был удалён')
									async def button_callback1(interaction):
										await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(ctx.guild.default_role, send_messages = False, add_reactions = False, view_channel=False)
										await channel6.set_permissions(role2, send_messages = True, add_reactions =True, view_channel=True)
										await channel6.set_permissions(member1, send_messages = True, add_reactions = True, view_channel=True, read_messages=True)
										await channel6.edit(category = category1)
										await interaction.response.edit_message(content = embed111, view = None)
										async def button_callback(interaction):
											await interaction.response.edit_message(content = embed, view = None)
											await channel6.set_permissions(role1, send_messages = False, add_reactions = False, view_channel=False)
											await channel6.set_permissions(role2, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)
											await channel6.set_permissions(member1, send_messages = False, add_reactions = False, view_channel=False, read_messages=False)  
											await channel6.edit(category = category2)
											async def button_callback(interaction):
												member2 = interaction.user
												lembed2 = discord.Embed(title= f'[{dt_string}] Пользователь: {member2} удалил тикет {channel6.name}', color = 0xFFFF99)
												await logchannel.send(embed = lembed2)                
												await channel6.delete(reason=None)
												await member2.send(f'{member2.mention} {channel6.name} был удалён')
											button111.callback = button_callback
											view = View(timeout = None)
											await channel6.send(embed = embed8)
											await asyncio.sleep(1 * 3)
											view.add_item(button111)
											await channel6.send(embed = embed111, view = view)
										button11.callback = button_callback
										view = View(timeout = None)
										view.add_item(button11)
										await channel6.send(embed = embed1111, view = view)
									button111.callback = button_callback
									button1111.callback = button_callback1
									view = View(timeout = None)
									await channel6.send(embed = embed8)
									await asyncio.sleep(1 * 3)
									view.add_item(button111)
									view.add_item(button1111)
									await channel6.send(embed = embed111, view = view)
								button11.callback = button_callback
								view = View(timeout = None)
								view.add_item(button11)
								await channel6.send(embed = embed1111, view = view)
							button111.callback = button_callback
							button1111.callback = button_callback1
							view = View(timeout = None)
							await channel6.send(embed = embed8)
							await asyncio.sleep(1 * 3)
							view.add_item(button111)
							view.add_item(button1111)
							await channel6.send(embed = embed111, view = view)
						button11.callback = button_callback
						view = View(timeout = None)
						view.add_item(button11)
						await channel6.send(embed = embed, view = view)
					button3.callback = button_callback
					view = View(timeout = None)
					view.add_item(button3)
					embed11 = discord.Embed(title = f"Если вы обнаружили баг/ошибку/недоработку, то нажмите сюда и заполните тикет. Наши администраторы рассмотрят репорт в ближайшее время.", description= "После нажатия кнопки будет создан специальный канал, находящийся в категории активные тикеты, в котором вас пиганёт бот.", color = 0x628ffe)
					await channel3.send(embed = embed11, view = view)

					embed1 = discord.Embed(title = f' Желаете востановить каналы с подсказками?("Для чего нужна эта категория")')

					button11 = Button(label = 'да', style = discord.ButtonStyle.blurple, emoji = "✅")
					async def button_callback(interaction):

						if channel6 == None:
							print('канал 6 не найден')
						else:
							await channel6.send(embed = discord.Embed(title = f"Для чего нужна эта категория?", description = (f'В этой категории будут храниться тикеты созданные обычными игроками для того, чтобы пожаловаться на игрока, предложить идею для улучшения сервера или подать апелляцию. Задача администратора по его мере возможностей решать' 
								'проблемы и выслушивать людей до того момента, пока тикет не закроет его создатель. Обычные правила распространяются на тикеты, поэтому вы можете выдать наказание в нём при нарушении правила. \n \n Нумерация тикета происходит следующим образом.\n `[тип тикета]` `[номер тикета]`'
								'\n\n Типы могут быть следующие: \n **П** - `пожелание/просьба` \n **Ж** - `жалоба` \n **A** - `апелляция` \n **В** - `Вопрос` \n **К** - `Kara$1k Багрепорт`\n \n Нумерация происходит по порядковому номеру тикета'), color = 0x628ffe) )
						if channel7 == None:
							print('канал 7 не найден')
						else:
							await channel7.send(embed = discord.Embed(title = f"Для чего нужна эта категория?", description = (f'В этой категории будут хранится закрытые тикиты. Данную категорию можно назвать архивом. Тикеты из этой категории запрещено редактировать или удалять без разрешения главы сервера. '
								'\n \n Нумерация тикета происходит следующим образом.\n `[тип тикета]` `[номер тикета]` \n\n Типы могут быть следующие: \n **П** - `пожелание/просьба` \n **Ж** - `жалоба` \n **A** - `апелляция` \n **В** - `Вопрос` \n **К** - `Kara$1k Багрепорт`\n \n Нумерация происходит по порядковому номеру тикета'), color = 0x628ffe) )
						await interaction.response.edit_message(content = embed1, view = None)

					button22 = Button(label = 'нет', style = discord.ButtonStyle.blurple, emoji = "❌")
					async def button_callback1(interaction):
						await interaction.response.edit_message(content = embed1, view = None)

					button11.callback = button_callback
					button22.callback = button_callback1
					view = View(timeout = None)
					view.add_item(button11)
					view.add_item(button22)
					await ctx.send(embed = embed1, view = view)	

#=========================================================================================================================================================

def filterOnlyBots(member):
	return member.bot

bot.loop.create_task(initialize())
bot.run(tokentest)
asyncio.run(bot.db.close())