class Weather:
    def __init__(self, parameters):
        self.parameters = parameters  

    def __contains__(self, item):
        return item in self.parameters

    def display(self):
        print("Weather parameters:", self.parameters)

w = Weather(['sunny', 'cloudy', 'rainy'])

w.display()

print("'sunny' in weather:", 'sunny' in w)     
print("'stormy' in weather:", 'stormy' in w)   
