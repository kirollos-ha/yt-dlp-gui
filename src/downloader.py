from subprocess import call

class Downloader:
    def __init__(self):
        pass

    def download(self, **kwargs):
        call(self.make_download_command(**kwargs))

    def make_download_command(self, **kwargs):
        command = ["yt-dlp"]
        if kwargs["down_playlist"]:
            command.append("--yes-playlist")
        if kwargs["just_audio"]:
            command.append("--extract-audio")

        command.append(kwargs["link"])
        print(command)
        return ["ls", "-l"] # placeholder
