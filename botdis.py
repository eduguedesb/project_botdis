import discord
import requests

# Substitua 'seu_token_discord' pelo token do seu bot Discord
TOKEN = 'seu_token_discord'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Evento para quando o bot estiver pronto
@client.event
async def on_ready():
    print(f'Bot {client.user} está online!')

# Evento para responder mensagens
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Comando para clima
    if message.content.startswith('!clima'):
        cidade = message.content[len('!clima '):]
        if cidade:
            try:
                api_key = 'sua_api_key'  # Coloque sua chave de API para o OpenWeatherMap
                url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric'
                response = requests.get(url).json()
                if response.get('main'):
                    temp = response['main']['temp']
                    descricao = response['weather'][0]['description']
                    await message.channel.send(f'O clima em {cidade.capitalize()} é de {temp}°C com {descricao}.')
                else:
                    await message.channel.send('Cidade não encontrada, por favor tente novamente.')
            except Exception as e:
                await message.channel.send(f'Ocorreu um erro ao buscar o clima: {str(e)}')
        else:
            await message.channel.send('Por favor, insira o nome da cidade.')

    # Comando para ajuda
    elif message.content.startswith('!ajuda'):
        await message.channel.send('Comandos disponíveis:\n!clima <cidade> - Verificar o clima em uma cidade\n!ajuda - Exibir esta mensagem')

client.run(TOKEN)
