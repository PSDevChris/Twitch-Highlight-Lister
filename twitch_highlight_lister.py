import asyncio
import json

import aiohttp

TWITCH_CLIENT_ID = ""
TWITCH_TOKEN = ""
BROADCASTER_ID = ""

twitchapiurl = f"https://api.twitch.tv/helix/videos?user_id={BROADCASTER_ID}&type=highlight&first=100"


async def list_twitch_highlights():
    async with (
        aiohttp.ClientSession(
            headers={
                "Authorization": f"Bearer {TWITCH_TOKEN}",
                "Client-Id": f"{TWITCH_CLIENT_ID}",
            }
        ) as session,
        session.get(f"{twitchapiurl}") as r,
    ):
        clipstring = ""
        if r.status == 200:
            Clips = await r.json()
            Pagination = Clips["pagination"]["cursor"] if Clips["pagination"] else ""
            while Pagination != "":
                async with session.get(f"{twitchapiurl}&after={Pagination}") as r:
                    if r.status == 200:
                        NextPage = await r.json()
                        # Append new list to old one
                        Clips["data"] = Clips["data"] + NextPage["data"]
                        Pagination = (
                            NextPage["pagination"]["cursor"]
                            if NextPage["pagination"]
                            else ""
                        )
            print(f"Loaded the Twitch Clips, I found {len(Clips['data'])} Clips.")
        else:
            print("ERROR: Twitch Clips could not be loaded!")
        for index, element in enumerate(Clips["data"]):
            clipstring = clipstring + json.dumps(Clips["data"][index]["url"]) + "\n"
    return clipstring.replace('"', "")


async def write_cliplist():
    with open("highlights.txt", "w") as cliplist:
        cliplist.write(await list_twitch_highlights())


asyncio.run(write_cliplist())
