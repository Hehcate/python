
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, status = False, muted = False, volume = MIN_VOLUME, channel = MIN_CHANNEL):
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
        self.__prevVolume = volume
    def power(self):
        self.__status = not self.__status
    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__previous_volume = self.__volume
                self.__volume = self.MIN_VOLUME
                self.__muted = True
            else:  # Unmuting the TV
                self.__volume = self.__previous_volume
                self.__muted = False
    def channel_up(self):
        if self.__status == False:
            return
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1
    def channel_down(self):
        if self.__status == False:
            return
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1
    def volume_up(self):
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
            self.__volume = self.__previous_volume
        if self.__volume < self.MAX_VOLUME:
            self.__volume += 1
    def volume_down(self):
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
            self.__volume = self.__previous_volume
        if self.__volume > self.MIN_VOLUME:
            self.__volume -= 1
    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume} '