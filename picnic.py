temperature = float(input("Enter the temperature in °C: "))
sky_condition = input("Is the sky sunny or cloudy? ").lower().strip()

if sky_condition == "sunny" and 23 < temperature < 28:
    print("It's the perfect day for a picnic!")
    
elif sky_condition == "cloudy" and 23 <= temperature <= 30:
    print("It's the perfect day for a picnic!")
    
else:
    print("Better not go out for a picnic today.")
  
