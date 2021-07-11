lower_temperature = 0
step_temperature = 20
upper_temperature = 300

fahr = lower_temperature
while(fahr <= upper_temperature):
    celcius = (5.0/9.0) * (fahr-32.0)
    print(fahr, celcius)
    fahr = fahr + step_temperature
