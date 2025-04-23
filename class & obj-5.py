class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def add(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

t1 = Time(1, 45, 30)
t2 = Time(2, 20, 45)

print("Time 1:", t1.display())
print("Time 2:", t2.display())

t3 = t1.add(t2)
print("Added Time:", t3.display())

print("Time 1 in seconds:", t1.to_seconds())
print("Time 2 in seconds:", t2.to_seconds())
