def play_instrument(obj):
    return obj.play()


class Guitar:
    @staticmethod
    def play():
        print("playing the guitar")


guitar = Guitar()
play_instrument(guitar)


class Piano:
    @staticmethod
    def play():
        print("playing the piano")


piano = Piano()
play_instrument(piano)
