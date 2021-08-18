## 1. Уберите эту строчку.
## 2. Идите к последней строчке
## 3. Вставляйте свой токен.
## 4. Робот должен заработать

import discord
from discord.ext import commands
import requests
import json
import bs4
from bs4 import BeautifulSoup as BS
import random


client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
        await client.change_presence(activity=discord.Game(name=".хелп | For KGDPS"))
        print('Я работаю!')


@client.command(aliases=['аватар', 'аватарка'])
async def avatar(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    embed = discord.Embed(
        title=f'Аватарка данного пользователя'
    )
    embed.set_image(url=userAvatar)
    embed.set_footer(text=f'Команду запросил @{ctx.author.name}')
    await ctx.send(embed=embed)

@client.command(aliases=['скажи'])
async def say(ctx, *, content):
    title, description= content.split('|') 
    embed = discord.Embed(title=title, 
        description=description,
        colour=discord.Color.orange())
    embed.set_footer(text=f'Администратор {ctx.author.name} запросил команду', 
                     icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@say.error
async def say_error(ctx, error): 
    if isinstance(error, commands.MissingPermissions):
                        embed = discord.Embed(
                title="Ошибка! :warning:",
                description="**У вас нет прав на использование этой команды.**",
                color = discord.Colour.red(),
                        )
                        embed.set_footer(text=f'Запросил @{ctx.author.name}, с кодом отказа помог bangakek#7000')
                        await ctx.send(embed=embed)

@client.command(aliases=['добавить', 'addsong'])
async def songadd(ctx, song: str=None):
    atts = ctx.message.attachments
    if (not song or 'youtube' in song) and len(atts) == 0:
        embed = discord.Embed(
            title='Маленькие проблемки!',
            description='Вы не ввели ссылку, или она не соотвествует параметрам!',
            color = discord.Colour.light_grey(),
        )
        embed.set_footer(text=f'Команду запросил @{ctx.author.name}. Код сделан ikov9lev#1337 & leestarb#5050')
        return await ctx.send(embed=embed)
    if len(atts) > 0:
        att = atts[0]
        song = att.proxy_url
    url = 'http://ps.fhgdps.com/KarasiKrutie/tools/songAdd.php'
    payload = {
    'songlink': song
    }
    s = requests.Session()
    answ = s.post(url, data=payload)
    answ_bs = BS(answ.content, 'html.parser')
    text = answ_bs.text
    id = text.split()[2]
    clean = id.replace('Soundcloud', '')
    if id == clean:
        result = 'Ошибка!'
        desc = 'Проверьте ведет ли ссылка на Файл с музыкой, либо на сайт `https://soundcloud.com`. Возможно она уже загружена на сервер!'
        color = discord.Colour.red()
    else:
        result = 'Успех!'
        desc = 'Ваша музыка успешно добавлена на сервер под ID:  ' + clean
        color = discord.Colour.green()
    emb = discord.Embed(title=result, description=desc, colour=color)
    emb.set_footer(text=f'Запрошено пользователем @{ctx.author.name}. Код сделан ikov9lev#1337 & leestarb#5050')
    await ctx.send(embed=emb)

@client.command(pass_context=True, aliases=['хелп', 'команды'])
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
            colour = discord.Colour.orange(),
    )
    embed.set_author(name='Команды!')
    embed.add_field(name='**Обычные команды**', value='**Данные команды доступны обычным участникам.**', inline=False)
    embed.add_field(name='.пинг', value='Отвечаем вам "Понг!"', inline=False)
    embed.add_field(name='.шар/ .8ball', value='Вы задаете вопрос - шар судьба дает вам ответ! Все просто.', inline=False)
    embed.add_field(name='.привет', value='Рандомный ответ бота на ваш "Привет"!', inline=False)
    embed.add_field(name='.собака', value='Рандомная картинки собаки со сайта Imgur!', inline=False)
    embed.add_field(name='.кот', value='Рандомная картинки кота со сайта Imgur!', inline=False)
    embed.add_field(name='.songadd / .addsong / .добавить', value='Добавить музыку на наш приватный сервер! Прикрепите файл и все будет готово!')
    embed.add_field(name='.проверка / .работаю / .work', value='Проверка, работает ли бот, или нет. Если ответит, то он работает!', inline=False)
    embed.add_field(name='.аватар / .аватарка / .avatar', value='Узнать аватарку определенного пользователя. Просто пинганите его! А можно узнать и свою аватарку..', inline=False)
    embed.add_field(name='**Команды для администаторов**', value='**Данные команды доступны __только__ для администраторов.**', inline=False)
    embed.add_field(name='.разбан / .разбанить / .unban', value='Разбанить участника сервера.', inline=False)
    embed.add_field(name='.ban / .бан / .забанить', value='А это уже забанить участника сервера.', inline=False)
    embed.add_field(name='.clear / .очисти20 / .очисти', value='Очистить чат на 20 строчек', inline=False)
    embed.add_field(name='.say / .скажи', value='Говорит то, что захочет администратор! Используется: .скажи Название|Описание', inline=False)

    await author.send(embed=embed)

@client.command(aliases=['проверка', 'работаю'])
async def work(ctx):
    embed = discord.Embed(
        title='Пшш-Пшш! :radio:',
        description='Агент "KGDPS Bot" работает! Конец связи.',
        color = discord.Colour.purple(),
    )
    embed.set_footer(text=f'Команду запросил {ctx.author.name}.')
    await ctx.send(embed=embed)

@client.command(aliases=['разбан','разбанить'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator =member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(
                        title=f'Я разбанил {ctx.message.author.mention}!',
                        color = discord.Colour.green(),
            )
            embed.set_footer(text=f'Администратор {ctx.author.name} запросил эту команду.')
            await ctx.send(embed=embed)
    

@client.command() # кот
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') 
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff9900, title = 'Рандомная картинка Кота :cat:') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)

@client.command() # кот
async def собака(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') 
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff9900, title = 'Рандомная картинка Собаки :dog:') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 


@client.command() # привет
async def привет(ctx):
    responses = ['Привет, привет!',
                'Салам-алейкум! Как дела?',
                'Ну.. Привет?',
                'Ты получил секретный ответ)',
                'Я не хочу тебе отвечать, у меня нет настроения...',
                'Здрасте! Я вася голубцов, шо ты хочешь?',
                'ЫАЛЫВОАЗПВФЫОАДЫВОАЛФЫВАФЫВАОВЫАЫФВА',
                'Я хочу здохнуть',
                'Приветик-Омлетик!']
    embed = discord.Embed(
                title=f'{random.choice(responses)}',
                color = discord.Colour.orange(),
    )
    embed.set_footer(text=f'Я ответил @{ctx.author.name}!')
    await ctx.send(embed = embed)

@client.command()
async def пинг(ctx):
    embed = discord.Embed(
        title='Понг! :ping_pong:',
        descrption=f'Я смог ответить за {round(client.latency * 1000)} миллисекунд!',
        color = discord.Colour.teal(),
    )
    embed.set_footer(text=f'Команду запросил @{ctx.author.message}')
    await ctx.send(embed=embed)

@client.command(aliases=['8ball', 'шар'])
async def _8ball(ctx, *, question):
    responses = ["Это несомненно!",
                "Это определенно так",
                "Без сомнения.",
                "Да - определенно.",
                "Вы можете положиться на это.",
                "Как я вижу - да.",
                "Да!",
                "Признаки указывают на \'ДА!\'",
                "Не очень уверен в ответе, попробуй ещё раз.",
                "Нет..",
                "Даже не думай.",
                "Я не могу предсказать...",
                "Даже не надейся.",
                "Не могу сосредоточиться... Спроси ещё раз."]
    embed = discord.Embed(
            title=f'Ваш вопрос: "{question}"',
            description=f'Мой ответ: {random.choice(responses)}.',
            color = discord.Colour.green(),
        )
    embed.set_footer(text=f'Команду запросил: @{ctx.author.name}')
    await ctx.send(embed=embed)

@client.command(pass_context = True, aliases=['очисти20', 'очисти'])
@commands.has_permissions( administrator = True )
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title="Было удалено 20 сообщений!",
        color = discord.Colour.green(),
    )
    embed.set_footer(text=f'Запросил: @{ctx.author.name}')
    await ctx.send(embed=embed, delete_after=15)

    
@clear.error
async def clear_error(ctx, error): 
    if isinstance(error, commands.MissingPermissions):
                        embed = discord.Embed(
                title="Ошибка! :warning:",
                description="**У вас нет прав на использование этой команды.**",
                color = discord.Colour.red(),
                        )
                        embed.set_footer(text=f'Запросил @{ctx.author.name}')
                        await ctx.send(embed=embed)

@client.command(aliases=['кик', 'выкинуть'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
        title="Произведено успешно!",
        description=f"Пользователь {member} был кикнут с причиной: {reason}.",
        color= discord.Colour.green(),
        )
        embed.set_footer(text=f'Администратор выдавший наказание: @{ctx.author.name}')
        await ctx.send(embed=embed, delete_after=15)

        
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
                        embed = discord.Embed(
                title="Ошибка! :warning:",
                description="**У вас нет прав на использование этой команды.**",
                color = discord.Colour.red(),
                        )
                        embed.set_footer(text=f'Запросил: @{ctx.author.name}')
                        await ctx.send(embed=embed, delete_after=15)
                        
@client.command(aliases=['бан', 'забанить'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(
        title="Произведено успешно!",
        description=f"Пользователь {member} был забанен с причиной: {reason}.",
        color= discord.Colour.green()
        )
        embed.set_footer(text=f'Запросил: @{ctx.author.name}')
        await ctx.send(embed=embed, delete_after=15)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
                        embed = discord.Embed(
                title="Ошибка! :warning:",
                description="**У вас нет прав на использование этой команды.**",
                color = discord.Colour.red(),
                        )
                        embed.set_footer(text=f'Запросил: @{ctx.author.name}')
                        await ctx.send(embed=embed, delete_after=15)

@unban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermision):
                embed = discord.Embed(
                    title="Ошибка! :warning:",
                    description="**У вас нет прав на использование этой команды.**",
                    color = discord.Colour.red(), 
                )
                embed.set_footer(text=f'Команды запросил @{ctx.author.name}')
                await ctx.send(embed=embed, delete_after=15)

client.run('your token :)')
