"""
- One talent = 20 pounds.
- One pound = 32 lots.
- One lot = 13.3 grams.
"""



talents=float(input('Enter Talents:'))
pounds=float(input('Enter Pounds:'))
lots= float(input('Enter lots:'))
total_grams=((talents*20*32*13.3)+ (pounds*32*13.3)+ (lots*13.3))
kilograms=int(total_grams/1000)
grams=total_grams%1000

print(f'The weight in modern units:\n{kilograms} kilograms and {grams:.2f} grams')
