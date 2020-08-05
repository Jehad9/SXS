import discord
import random
import io
import aiohttp
from discord import user
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT

client = commands.Bot (command_prefix='.')


currentDT = DT.datetime.now ()


@client.event
async def on_ready():
    await client.change_presence (status=discord.Status.do_not_disturb,
                                  activity=discord.Game ('with pussy and reading'))
    print ("Bot is ready")


@client.command ()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick (reason=reason)
    await ctx.send (f'ابلع كك يخو الشرموطة {member.mention}')


@client.command ()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban (reason=reason)
    await ctx.send (f'ابلع باند يخو القحبة {member.mention}')


@client.command ()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans ()
    member_name, member_discriminator = member.split ('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban (user)
            await ctx.send (f'فكيت الباند عنك عشانك ممحون {user.mention}')
            return


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str (channel) == "hello":
            await channel.send (f'  نور السيرفر كس اختك{member.mention}')


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str (channel) == "hello":
            await channel.send (f' كس امك لاعاد ترجع للسيرفر{member.mention}')


@client.event
async def on_message(message):
    id = client.get_guild (713558576609624065)
    if message.content == "عرف عن نفسك ياخبير":
        embed = discord.Embed(
        title = "Sex Expert, خبير السكس",
            description = 'فاهم الحياة وخصيصا السكس!',
        colour = discord.Color.dark_red()

        )
        embed.set_footer(text ='هذه صورتي والان يكفيك شرف انك شفتها')
        embed.set_image(url='https://cdn.discordapp.com/attachments/715532355363668121/715532423420444682/download_8'
                            '.png')
        embed.set_thumbnail(url ='https://cdn.discordapp.com/attachments/715532355363668121/715532423420444682/download_8.png')
        embed.set_author(name= 'Sex Expert (خبير السكس)')
        icon_url= 'https://cdn.discordapp.com/attachments/715532355363668121/715532423420444682/download_8.png'
        embed.add_field(name='تقدر تسألني اذا عندك شي معين', value='وتأكد بينك وبين نفسك اني مو فاضي لك دائما', inline=False)
        embed.add_field(name='ممكن لساني يكون قذر؟', value='اي نعم لأنك تستاهل السب والشتم كونك جاهل! وانا افضل منك!؟', inline=True)
        embed.add_field(name='هل معنى اني افضل منك اتكبر عليك؟', value='اكيد مايحتاج تسأل زي هذه الاسئلة!', inline=True)
        await message.channel.send (content=None, embed=embed)

    await client.process_commands (message)

@client.command (aliases=['SEX'])
async def sex(ctx, *, question):
    global random_url_from_Pics
    Pics = ["https://cdn.discordapp.com/attachments/715532355363668121/715587484280553492/IMG_20200517_211900_389.jpg"
        ,"https://cdn.discordapp.com/attachments/715532355363668121/715587482900758569/Screenshot_20200518-201952.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587482640711782/IMG_20200520_005721_585.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587482447511574/IMG_20200522_094236_048.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587482107904010/Screenshot_2020-05-23-19-20-54.png",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587276444532756/Screenshot_2020-05-18-23-15-52.png",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587275852873788/ad6be70e15910d34804b14aa0b3ec8c8.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587275605671962/Screenshot_20200521-163701.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587143623376936/IMG_20200524_085459_397.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587143442890912/IMG_20200524_085901_708.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587143191494716/IMG_20200524_085903_649.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587142927122482/IMG_20200524_090054_443.jpg",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587104574537748/Screenshot_2020-05-26-11-31-26.png",
            "https://cdn.discordapp.com/attachments/715532355363668121/715587104574537748/Screenshot_2020-05-26-11-31-26.png"
            ,"https://cdn.discordapp.com/attachments/715532355363668121/715587026384322650/p6n8-20200528-0002.jpg"
            ,"https://cdn.discordapp.com/attachments/715532355363668121/715589016967446568/Screenshot_20200520-193902.jpg"
            ,"https://cdn.discordapp.com/attachments/715532355363668121/715589016967446568/Screenshot_20200520-193902.jpg"
            ,"https://cdn.discordapp.com/attachments/715532355363668121/715542878276943882/screen-0.jpg"]
    embed.set_image(random_url_from_Pics)
    random_url_from_Pics = random.choice(Pics)
    await ctx.send(f'{random.url(Pics)}')

@client.event
async def on_command_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        await ctx.send ('ايش سؤالك ياقحبة؟ ؟؟')
    elif isinstance (error, commands.CommandNotFound):
        await ctx.send ('كس اختك اكتب (.الخبير) اوكيه ياعمري ؟')

@client.command (aliases=['الخبير'])
async def expert(ctx, *, question):
    responses = [
        "منجدك انت كسم ذوقك",
        "كس امك هذه وحده تنيكها",
        "والله شف مع اني احس كسها وصخ بس يالله يجي منها",
        "والله ياحبيبي ودي بس مجرد اتخيل جسمها اطرش ",
        "كس امك شكلك ودك تحط زبك بأي فتحة",
        "يعني تقدر تقول ",
        "هذه ميزتها انها ام طيز",
        "سكسية والله ",
        "كس امك انيك ابو علاء ولا انيكها ",
        "اححح ياليتني انيكها انا بعد"
        "ياكريم ارزقنا بوحدة زيها"

    ]
    await ctx.send (f'{random.choice(responses)}')


client.run (os.environ['DISCORD_TOKEN'])

