# Conversion rates
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Amount of units for conversion.

kgs = 80
kms = 54
litres = 5

# Conversion calculations

lbs = kgs * kg_lb
miles = kms * km_mile
gallons = litres * l_gal


# Final answers
print(str(kgs) + ' kg is ' + str(lbs) +' lb')
print(kms, 'km is', miles, 'miles')
print(litres, 'l is', gallons, 'gallons')