from youtube_dl import YoutubeDL
# Sample1:
dl = YoutubeDL ()
dl.download (["https://www.youtube.com/watch?v=Bmo4PSbB8E8"])

# Sample2:
dl = YoutubeDL()
dl.download (["https://www.youtube.com/watch?v=5quhM8hp3OY", "https://www.youtube.com/watch?v=IKx5CvIayV0"])

#Sample3:
options = {
        "format": "bestaudio/audio"
    }
dl = YoutubeDL (options)
dl.download (["https://www.youtube.com/watch?v=zP50Ewh31E4"])

#Sample4:
options = {
        "default_search": "ytsearch",
        "max_downloads": 1
    }
dl = YoutubeDL (options)
dl.download (["i got 5 on it"])

#Sample5:
options = {
        "default_search": "ytsearch",
        "max_downloads": 1,
        "format": "bestaudio/audio",
    }
dl = YoutubeDL (options)
dl.download (["sun flower"])