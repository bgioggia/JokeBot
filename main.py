import time
import jokes
import random
import discord
from config import BOT


"""
void -> string
"""
def prompt(choice):

    if choice == "random":
        options = ["sex_with_me", "pickup_lines", "bar_jokes", "yo_mama", "back_in_my_day"]
        choice = random.choice(options)

    if choice == "sex_with_me":
        joke = jokes.sex_with_me()
    elif choice == "pickup_lines":
        joke = jokes.pickup_lines()
    elif choice == "bar_jokes":
        joke = jokes.bar_joke()
    elif choice == "yo_mama":
        joke = jokes.yo_mama()
    else:
        joke = jokes.back_in_my_day()

    return '\n' + joke

"""
main
"""
if __name__ == '__main__':

    TOKEN = BOT['TOKEN']
    GUILD = BOT['GUILD']

    client = discord.Client()

    # helpful connection confirmtion
    # from https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python
    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\nREADY FOR JOKING'
        )


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        msg = message.content.lower()

        if '!prompt' in msg:
            choice = 'random'
            if 'sex' in msg:
                choice = 'sex_with_me'
            elif 'pickup' in msg:
                choice = 'pickup_lines'
            elif 'mama' in msg:
                choice = 'yo_mama'
            elif 'bar' in msg:
                choice = 'bar_jokes'
            elif 'back' in msg or 'day' in msg:
                choice = 'back_in_my_day'
            response = prompt(choice)
            await message.channel.send(response)


    client.run(TOKEN)





