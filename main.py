import discord, sys, os, time, asyncio
from discord.ext import commands
from colorama import Fore

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def logo():
    clear()
    return f'''{Fore.LIGHTBLUE_EX}
  ___        _         ______                                 
 / _ \      | |        | ___ \                                
/ /_\ \_   _| |_ ___   | |_/ /_   _ _ __ ___  _ __   ___ _ __ 
|  _  | | | | __/ _ \  | ___ \ | | | '_ ` _ \| '_ \ / _ \ '__|
| | | | |_| | || (_) | | |_/ / |_| | | | | | | |_) |  __/ |   
\_| |_/\__,_|\__\___/  \____/ \__,_|_| |_| |_| .__/ \___|_|   
                                             | |              
                                             |_|              

{Fore.LIGHTCYAN_EX}
Made by MysteriousK#6969 - https://discord.gg/dTAeY2rftR
{Fore.WHITE}
'''

@bot.event
async def on_ready():
    channel = bot.get_channel(channelID)
    sent = 0
    while True:
        await channel.send('!d bump')
        try:
            await asyncio.sleep(delay)
        except:
            print(f'{Fore.RED}The delay is too big or too low. Please try again.{Fore.WHITE}')
        sent += 1
        print(f'Sent a message! A total of {sent} messages have been sent!')
def login(token):
    print(logo())
    try:
        bot.run(token,bot=False)
    except:
        print(f'{Fore.RED}Invalid token was passed...{Fore.WHITE}')
        time.sleep(5)
        return

def main():
    global channelID, delay
    print(logo())
    print(f'{Fore.LIGHTBLUE_EX}Enter your accounts token: {Fore.WHITE}')
    token = input()
    print(f'{Fore.LIGHTBLUE_EX}Enter your channels ID: {Fore.WHITE}')
    try:
        channelID = int(input())
    except:
        print(f'{Fore.RED}Invalid input...{Fore.WHITE}')
        time.sleep(3)
        return
    print(f'{Fore.LIGHTBLUE_EX}Enter the delay you would like to send the message at: {Fore.WHITE}')
    try:
        delay = int(input())
    except:
        print(f'{Fore.RED}Invalid input...{Fore.WHITE}')
        time.sleep(3)
        return
    login(token)

if __name__ == '__main__':
    main()
