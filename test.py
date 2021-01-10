import uvicorn
from fastapi import FastAPI

from starlette_discord.client import DiscordOauthClient


app = FastAPI()
client = DiscordOauthClient('', '', '')


@app.get('/login')
async def login_with_discord():
    return client.redirect()


@app.get('/callback')
async def callback(code: str):
    return await client.login(code)



uvicorn.run(app, host='localhost', port=9000)