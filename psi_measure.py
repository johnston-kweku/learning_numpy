bottom_hole_pressure = float(input('Please enter Bottom-Hole Pressure: \n'))

if bottom_hole_pressure > 2000 and bottom_hole_pressure < 5000:
    message = f'BHP of {bottom_hole_pressure} falls in the Safe Zone. Continue normal operations.'

elif (bottom_hole_pressure >= 1000 and bottom_hole_pressure <= 1999) or \
     (bottom_hole_pressure >= 5001 and bottom_hole_pressure <= 7000):
    message = f'BHP of {bottom_hole_pressure} falls in the Warning Zone. Monitor closely.'

else:
    message = f'BHP of {bottom_hole_pressure} falls in the Critical Zone. Shut down the well immediately!'

print(message)