# Take every second element starting from index 0 and format as "Temp: {value:.1f}°C"


temps = [30.567, 32.456, 28.9, 35.678, 29.111]

# values = [ f"Temp: {value:.1f}°C"
#           for value, value in enumerate(temps[0::2] ,start=0)
# ]

# print(values)


values = [ f"Temp: {value:.1f}°C" for value in temps[0::2]
]

print(values)