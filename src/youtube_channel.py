from pytube import Channel


class YtChannel:
  def __init__(self, url) -> None:
    self.yt = Channel(url=url)

  def test(self):
    # print(json.dumps(self.yt.sidebar_info, indent=2))
    pass
