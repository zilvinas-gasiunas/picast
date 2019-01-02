class VideoIdProvider:

    def __init__(self):
        self.videoMap = {
            1: "YDJcZzia8QU",
            2: "8ljHzljQrY8",
            3: "9wL26G00pQc",
            4: "bvC_0foemLY",
            5: "X3qeygwQ8yU"
        }

    def getVideo(self, videoId):
        return self.videoMap[videoId]
