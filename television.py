
class Television:
    '''
    A class representing a television
    '''
    MIN_VOLUME: int = 0
    MAX_VOLUME = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    def __init__(self):
        '''
        Method to set the default values of the television object
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__prevVolume: int = self.__volume
    def power(self) -> None:
        '''
        Changes truth value of status
        '''
        self.__status = not self.__status
        # Method to switch the power of the TV

    def mute(self) -> None:
        '''
        Method that checks to see if the TV is already muted.
        If not, store the volume that it was before setting the volume to 0
        If it is, restore the volume to its previous value before being muted
        '''
        if self.__status:
            if not self.__muted:
                self.__previous_volume = self.__volume
                self.__volume = self.MIN_VOLUME
                self.__muted = True
            else:  # Unmuting the TV
                self.__volume = self.__previous_volume
                self.__muted = False
    def channel_up(self) -> None:
        '''
        Method that increases the channel if it is below the MAX_CHANNEL variable
        '''
        if self.__status == False:
            return
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1
    def channel_down(self) -> None:
        '''
        Method that decreases the channel if it is above the MIN_CHANNEL variable
        '''
        if self.__status == False:
            return
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1
    def volume_up(self) -> None:
        '''
        Method that increases the volume if it is below the MAX_VOLUME variable
        '''
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
            self.__volume = self.__previous_volume
        if self.__volume < self.MAX_VOLUME:
            self.__volume += 1
    def volume_down(self) -> None:
        '''
        Method that decreases the volume if it is above the MIN_VOLUME variable
        '''
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
            self.__volume = self.__previous_volume
        if self.__volume > self.MIN_VOLUME:
            self.__volume -= 1
    def __str__(self):
        '''
        Method that prints the Power, Channel, and Volume status when called
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'