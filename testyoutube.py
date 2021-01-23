import youtube_dl
url = "https://www.youtube.com/watch?v=IosaWkNnRYw"

ydlOpt = {'outtmpl': '%(id)s.%(ext)s','format':'22'}
ydl = youtube_dl.YoutubeDL(ydlOpt)

with ydl:
    result = ydl.extract_info(
        url,
        download=True # We just want to extract the info
    )