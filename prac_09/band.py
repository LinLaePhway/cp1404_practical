class Band:
    def __init__(self, band_name):
        self.band_name = band_name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        return f"{self.band_name} ({', '.join([str(musician) for musician in self.musicians])})"

    def play(self):
        print(f"{self.band_name} (str)")
        for musician in self.musicians:
            print(musician.play())
