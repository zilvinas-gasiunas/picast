import pychromecast
from pychromecast.controllers.youtube import YouTubeController

class ChromeCast:

    # Initializer / Instance Attributes
    def __init__(self, name):
        self.name = name
        chromecasts = pychromecast.get_chromecasts()
        cast = next(cc for cc in chromecasts if cc.device.friendly_name == name)
        cast.wait()
        self.yt = YouTubeController()
        cast.register_handler(self.yt)

    def play(self, videoId):

        self.yt.start_session_if_none()
        self.yt.play_video(videoId)
