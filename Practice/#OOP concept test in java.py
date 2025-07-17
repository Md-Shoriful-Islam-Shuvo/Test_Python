class Temperature:
    def __init__(self, celsius):
        # Store the temperature, but use the setter for validation
        self.celsius = celsius
    
    # Add property and setter methods here
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self,value):
        if value < -273:
            raise ValueError("celcius can not be below -273°C")
        self._celsius=value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9
    
# Test the class:
# 1. Create a temperature instance at 25°C
temp = Temperature(25)

# 2. Print both Celsius and Fahrenheit
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")

# 3. Set the temperature to 98.6°F
temp.fahrenheit = 98.6

# 4. Print both values again
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")

# 5. Try setting an invalid temperature (should show error)
#temp.celsius = -300