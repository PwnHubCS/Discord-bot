import discord
from discord.ext import commands
import datetime 
import asyncio
from pretty_help import PrettyHelp, Navigation
import base64
import traceback
import alexflipnote




bot = commands.Bot(command_prefix='>', description="BOT IS CODED BY THELINUX-USERCHOICE",help_command=PrettyHelp())

index_title = "welcome Octa-bot help"
no_category = "react emojis to go up down"

# custom ending note using the command context and help command formatters
ending_note = "coded by subodha prabash -{ctx.bot.user.name}\nFor command {help.clean_prefix}{help.invoked_with}"

# ":discord:743511195197374563" is a custom discord emoji format. Adjust to match your own custom emoji.
nav = Navigation("✔")
color = discord.Color.gold()


bot.help_command = PrettyHelp(index_title=index_title,no_category=no_category,navigation=nav, color=color, active_time=20, ending_note=ending_note)
cogs = ["on_message"]


@bot.command(name='ping',help='this command can bot s latency')
async def ping(ctx):  
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    embed = discord.Embed(title=f"Ping.. Pong ..latency is {round(bot.latency * 1000)} ms", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.set_thumbnail(url="https://i.postimg.cc/BnQyPrMx/tenor.gif")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(name='sum',help='this command will sums numbers what you insert')
async def sum(ctx, numOne: int, numTwo: int):
    output = (numOne + numTwo)
    embed = discord.Embed(title=f"Sum is {output}", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.set_thumbnail(url="https://i.postimg.cc/vBM5csvy/tenor.gif")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(name='serverinfo',help='you can get your server info with this')
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.green()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  sender = ctx.author.name
  embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed) 



@bot.event
async def on_ready():
   print('We have logged in as {0.user}'.format(bot))
   print('Servers connected to:')
   for cog in cogs:
    try:
        bot.load_extension(cog)
        print(f"{cog} was loaded.")
    except Exception as e:
        print(e)
   for guild in bot.guilds:
        print(f'name:{guild.name}\nguild id:{guild.id}') 
   while True:
    await bot.change_presence(activity=discord.Game(name="🌹USE >help📜 "))
    await asyncio.sleep(4)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="🐙USE >help📜 "))
    await asyncio.sleep(4)
    await bot.change_presence(activity=discord.Streaming(name="😜USE >help📜 ", url='https://www.twitch.tv/accountname'))
    await asyncio.sleep(4)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="💖USE >help📜 "))
    




@bot.command(name='clear', help='this command will clear messages ask author for permission')
async def clear(ctx, amount:int,static=1):
 if ctx.author.id == 780400901553782824 :   
  
    await ctx.channel.purge(limit=amount)
    author = ctx.author.name
    await ctx.send(f"`CLEARED`{amount}`MESSAGES...BY `{author} ")
 else:
    await ctx.send('`You do not have permission to delete this messages`')      
    

@bot.command(name='print',help='echo what you types')
async def print(ctx, *, content:str):
    embed = discord.Embed(title=f"{content}", timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    sender = ctx.author.name
    embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command(name='slap',help='fun command to slap your friend')
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    embed = discord.Embed(title= ('{} `just got slapped for` {}'.format(slapped, reason)),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.red())
    sender = ctx.author.name
    embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(name='greet',help='greet your boss :smile:')
async def greet(ctx,content:str):
  import asyncio
  message = await ctx.send("`starting greetings `:smile:")
  await asyncio.sleep(3)
  await message.edit(content="`h`")
  await asyncio.sleep(1)
  await message.edit(content="`he`")
  await asyncio.sleep(1)
  await message.edit(content="`hel`")
  await asyncio.sleep(1)
  await message.edit(content="`hell`")
  await asyncio.sleep(1)
  await message.edit(content="`hello`")
  await asyncio.sleep(1)
  await message.edit(content="`hellow`")
  await asyncio.sleep(1)
  await message.edit(content=f"`hellow`{content} `hope you are good!`")
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji)









@bot.command(name='hack',help='hack the nasa babe!')
async def hack(ctx):
  import asyncio
  message = await ctx.send("[:octopus:]`hacking the NASA`")
  await asyncio.sleep(3)
  await message.edit(content="[:key:]**IP FOUND!**")
  await asyncio.sleep(3)
  await message.edit(content="[:warning:] `DDOSING the ip of NASA {127.0.0.1}`")
  await asyncio.sleep(3)
  await message.edit(content="[:sos:]**Deploying botnets and sending 'weareanonymous' in tcp packets...**")
  await asyncio.sleep(4)
  await message.edit(content="> successfully taken down the nasa website now corps will come for ya!")
  await asyncio.sleep(4)
  await message.edit(content="[:wave:]**exiting tor nodes ....**")
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji)


    
 
@bot.command(name='iptrack',help='tracks any ip instantly')
async def iptrack(ctx, ip: str):
 from requests import get
 track = get(f'https://ipapi.co/{ip}/json/')
 traced = (track.json())
 embed = discord.Embed(title=":small_red_triangle:IP TRACKER:small_red_triangle_down: ", description="**project on my github** :pirate_flag:", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
 embed.set_thumbnail(url="https://i.postimg.cc/XvWHrS3d/tenor.gif")
 sender = ctx.author.name
 embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
 embed.add_field(name=f"Results for ip - {ip} ", value=f"```py\n{traced}```")
 await ctx.send(embed=embed)
    
@bot.command(name='invite',help='invite this bot to your server')
async def invite(ctx):
    embed = discord.Embed(title=":red_circle: INVITE ME TO YOUR SERVER :red_circle:", description="**USE BELOW LINK**", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="`INVITE LINK`", value="Octa-bot")
    embed.add_field(name='https://dsc.gg/octa-bot',value=":heart: from Octa-bot")
    embed.set_thumbnail(url="https://i.postimg.cc/c45Rcgmh/tenor.gif")
    embed.add_field(name="`Send a message to dev`", value="**Anonymous |Doctor#1890**")
    sender = ctx.author.name
    embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed) 
    
@bot.command(name='angry',help='report command on Octa-bot')
async def angry(ctx, members: commands.Greedy[discord.Member], *, reason='bad personality'):
    slapped = ", ".join(x.name for x in members)
    embed = discord.Embed(title= ('{} was reported for {}'.format(slapped, reason)),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.red())
    embed.set_thumbnail(url="https://i.postimg.cc/8c7SrwMb/813436939738677267.gif")
    embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
    embed.add_field(name="Pease ping @moderator to report this guy", value="```py\nDo not use this as a joke because if you unnecessary used this you will get kicked or banned by server owner/admin/mod {this command is for your safety and democracy!}```")
    await ctx.send(embed=embed)    
    
@bot.command(name='google',help='search it! :hehe:')
async def google(ctx,content:str): 
 message = await ctx.send("`if this didn't donot gives a output donot worry , it means there is no such wikis on you requested.`")
 await asyncio.sleep(5)
 await message.edit(content="`tip=try using same but different{synonyms}`")
  
 import wikipedia
 txt =  wikipedia.summary(f"{content}",sentences=2)
 embed = discord.Embed(title=":small_red_triangle:GOOGLE:small_red_triangle_down: ", description="**Just google it! but sometimes it doesn't give you output it means there i no wiki of you requested**" , timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
 embed.set_thumbnail(url="https://i.postimg.cc/437ZyXkS/tenor.gif")
 sender = ctx.author.name
 embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
 embed.add_field(name=f"Results for {content} ", value=f"```py\n{txt}```")
 await ctx.send(embed=embed)    
    
@bot.command(name='b64',help='this can encode and decode base64')
async def b64(ctx,tag,*,inputb64):
    try:
        outputdec=None
        outputenc=None

        if tag in ["-e","--encode"]: 
            encoded_as_bytes = base64.b64encode(inputb64.encode("utf-8"))
            outputenc = str(encoded_as_bytes , "utf-8")
            embed = discord.Embed(title=f"**your encoded b64 output of**  `{inputb64}`  **is** -----> `{outputenc}`", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
            embed.set_thumbnail(url="https://i.postimg.cc/hjSLVLVJ/tenor.gif")
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

            #await ctx.send(f'**your encoded b64 output of**  `{inputb64}`  **is** -----> `{outputenc}`')

        if tag in ["-d","--decode"]:
            decoded_as_bytes = base64.b64decode(inputb64.encode("utf-8"))
            outputdec = str(decoded_as_bytes , "utf-8")
            embed = discord.Embed(title=f"**your decoded base64 output of** `{inputb64}`  **is** -----> `{outputdec}`", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
            embed.set_thumbnail(url="https://i.postimg.cc/mr4CGYXd/tenor.gif")
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            #await ctx.send(f'**your decoded base64 output of** `{inputb64}`  **is** -----> `{outputdec}`')

        if outputdec == None and outputenc == None:
            embed = discord.Embed(title="`pls check the tag and try again (-e/-d)`\n`use -e to encode base64 and -d to decode base64`\n`example:>b64 -e test `\n`example:>b64 -d dGVzdA==`", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
            embed.set_thumbnail(url="https://i.postimg.cc/gj1Lt8LH/tenor.gif")
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            #await ctx.send("`pls check the tag and try again (-e/-d)`\n`use -e to encode base64 and -d to decode base64`\n`example:>b64 -e test `\n`example:>b64 -d dGVzdA==`")

        else:
            print('erros')

    except Exception:
            traceback.print_exc()
            print("error")

alex_api = alexflipnote.Client("ALEXFLIPNOTE API KEY")


@bot.command()#cat
async def cat(ctx):
    """gives you a cute cat image!"""
    embed = discord.Embed()
    catimg = await alex_api.cats()
    embed = discord.Embed(title= ('CUTY CATTY'),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
    embed.set_image(url=f"{catimg}")
    #embed.set_thumbnail(url="https://i.postimg.cc/mr4CGYXd/tenor.gif")   
    #await ctx.send(catimg)
    await ctx.send(embed=embed)

@bot.command()#fml
async def fml(ctx):
    """gives you an incident that fvked mah life forever""" 
    fmlimg = await alex_api.fml()
    embed = discord.Embed(title= ('FML JOKES :smile:'),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    embed.set_thumbnail(url="https://i.postimg.cc/pyNYcc7Y/tenor.gif")
    sender = ctx.author.name
    embed.set_footer(text=f"This was requested by {sender}", icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"HA HA HA!", value=f"```py\n{fmlimg}```")
    await ctx.send(embed=embed)
    #await ctx.send(f"```py\n{fmlimg}```")

@bot.command()#dog
async def dog(ctx):
    """shows you a image of a cute doggo"""
    dogimg = await alex_api.dogs()
    embed = discord.Embed(title= ('CUTE DOGGO'),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
    embed.set_image(url=f"{dogimg}")
    await ctx.send(embed=embed)
    #await ctx.send(dogimg)

@bot.command()#poorly_photoshopped_sadcat
async def sadcat(ctx):
    """ image of a sad cat UwU"""
    sadcatimg = await alex_api.sadcat()
    embed = discord.Embed(title= ('SAD CAT UwU'),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
    embed.set_image(url=f"{sadcatimg}")
    await ctx.send(embed=embed)
    #await ctx.send(sadcatimg)

@bot.command()
async def bird(ctx):
    """gives a bird image"""
    birdimg = await alex_api.birb()
    embed = discord.Embed(title= ('BIRDS 0_0'),timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.green())
    embed.set_footer(text=ctx.author.name , icon_url=ctx.author.avatar_url)
    embed.set_image(url=f"{birdimg}")
    await ctx.send(embed=embed)
    #await ctx.send(birbimg)  

@bot.command()
async def mineach(ctx, text: str, icon = None): 
    """Displays a minecraft achievemt"""
    image = await alex_api.achievement(text=text, icon=icon)
    image_bytes = await image.read()
    file = discord.File(image_bytes, "achievement.png")
    await ctx.send(f"`Rendered by {ctx.author}`", file=file)

@bot.command()
async def supreme(ctx, text: str):
  """just displays your text on supreme background"""
  # Embed
  #embed = discord.Embed(title = f"Rendered by {ctx.author}")  # this is a example, everything is optional.
  #embed.set_image(url = "attachment://supreme.png")  # attaching file image to embed.
  # Wrapper
  #image = await alex_api.supreme(text = text)  # get Image object
  #image_bytes = await image.read()  # get io.BytesIO object
  # Sending
  #file = discord.File(image_bytes, "supreme.png") # pass io.BytesIO object to discord.File with a filename.
  #await ctx.send(embed=embed, file=file) # send both the embed and file, the file will attach to the embed.

  # Or ----

  # Oneline, because oneline = best
  embed = discord.Embed(title = f"Rendered by {ctx.author}").set_image(url="attachment://supreme.png")
  image = discord.File(await (await alex_api.supreme(text=text)).read(), "supreme.png")
  await ctx.send(embed=embed, file=image)









bot.run('YOUR BOT TOKEN HERE')
