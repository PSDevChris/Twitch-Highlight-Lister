# Twitch Highlight Lister

This is a simple Python script to list all highlights for a specific Twitch channel, since on april 19th Twitch will begin to delete VoDs until the creator meets the 100h mark.

The script is by far not finished or user-friendly but since there are hundreds of hours of year-old content for small creators that want to save their streams, I wanted to get this out asap. 

The highlights.txt can be used with tools like yt-dlp to download the vods all in one go without the need to get the URL or to browse through every single highlight page.

You need a Twitch Token, a client id and the user_id of the streamer you want to download from. Twitch has a lot of documentation on this, so please get familiar with that first.

# How to get your broadcaster id, client id and an oauth Token

- An easy way to get the Broadcaster ID is: https://www.streamweasels.com/tools/convert-twitch-username-%20to-user-id/
- You need to register your application at: https://dev.twitch.tv/console/apps (a free Twitch Account is required)
- Get the Client ID from your previously registered App
- Generate a Client Secret and get an oauth token via curl or other similar commands: https://dev.twitch.tv/docs/api/get-started/
- Enter all three values in line 6-8 in the script
