from pathlib import Path
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, AgeRestrictedError, LiveStreamError, VideoPrivate, RecordingUnavailable, MembersOnly

class YouTubeDownloader:

    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path or Path().cwd()
        self.quality = quality or 'highest'
        try:
            self.yt = YouTube(
                self.url,
                on_progress_callback=self.on_progress,
                # on_complete_callback=self.on_progress
                )
        except VideoUnavailable as e:
            print(e.error_string)
            # handle video unavailable error
        except Exception as e:
            print(e)
            # handle other errors

    def download(self):
        if self.quality == "highest":
            stream = self.yt.streams.filter(
                progressive=True,
                file_extension='mp4'
            ).get_highest_resolution()
        else:
            stream = self.yt.streams.filter(
                progressive=True,
                file_extension='mp4',
                res=self.quality
                ).first()
        stream.download(self.output_path)
        
    def on_progress(self, stream, chunk, bytes_rm):
        print(bytes_rm)
        
        
if __name__ == "__main__":
    yt = YouTubeDownloader(
    "https://www.youtube.com/watch?v=2QsW_n2Dies&ab_channel=Limad"
    ).download()
