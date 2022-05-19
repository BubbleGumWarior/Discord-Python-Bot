import discord
import random
TOKEN = 'ODAwMzA3NDI2OTA5NDg3MTA0.YAQOXw.OEeuVt8AEVX4uPE9fEV7c0RCln4'
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return

    Command = str(user_message).split(' ') [0]

    if Command == '!color':
        arrColor = ["Red", "Orange", "Yellow", "Green", "Cyan", "Magenta", "Blue", "White", "Black", "Grey", "Silver", "Pink", "Maroon", "Brown", "Beige", "Tan", "Peach", "Purple", "Lime", "Olive", "Turquoise", "Teal", "Gold", "Indigo", "Violet"]
        sColor1 = arrColor[random.randint(1, 25)]
        sColor2 = arrColor[random.randint(1, 25)]
        sColor3 = arrColor[random.randint(1, 25)]
        await message.channel.send('Your colors are: ' + sColor1 + ', ' + sColor2 + ', ' + sColor3)

    if Command == '!roll':
        if username != 'Dungeon Lurker':
            Dice = str(user_message).split(' ') [1]
            RollCount = str(Dice).split('d') [0]
            if RollCount == '':
                RollCount = '1'
            RandomNumber = str(Dice).split('d') [1]
            try:
                Modifier = str(user_message).split(' ') [2]
            except IndexError:
                Modifier = str(+0);
            Total = int(0)

            if int(RollCount) > 1:
                for x in range(int(RollCount)):
                    Roll = random.randint(1, int(RandomNumber))
                    ModRoll = Roll + int(Modifier)
                    if int(ModRoll) < 1:
                        ModRoll = '1'
                    if Modifier != '0':
                        await message.channel.send('Roll number ' + str(x + 1) + ': ' + str(Roll) + str(Modifier) + ' = ' + str(ModRoll))
                    else:
                        await message.channel.send('Roll number ' + str(x + 1) + ': ' + str(Roll))
                    Total = Total + int(ModRoll)
                await message.channel.send('By rolling a ' + Dice + ' your Total Value is: ' + str(Total))

            if int(RollCount) == 1:
                Roll = random.randint(1, int(RandomNumber))
                ModRoll = Roll + int(Modifier)
                if int(ModRoll) < 1:
                    ModRoll = '1'
                if Modifier != '0':
                    await message.channel.send('By rolling a ' + Dice + ' your Total Value is: ' + str(Roll) + str(Modifier) + ' = ' + str(ModRoll))
                else:
                    await message.channel.send('By rolling a ' + Dice + ' your Total Value is: ' + str(Roll))
client.run(TOKEN)
