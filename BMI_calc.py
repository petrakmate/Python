def bmi(height, weight):
    try:
        height_cm = float(height)
        weight_kg = float(weight)
        if height_cm <= 0 or weight_kg <= 0:
            print('You need to enter a positive number. ')
        else:
            index_bmi = weight_kg / (height_cm/100)**2
            return round(index_bmi,2)
    except ValueError:
        print('You need to enter a positive number. ')

h = input("What's your height in centimetres? ")
w = input("What's your weight in kilograms? ")

bmi_value = bmi(h,w)

if type(bmi_value) == float:
    print('You BMI is:', bmi_value)
    if bmi_value < 18.5:
        print('This is described as underweight.')
    elif bmi_value < 25:
        print("This is described as the ‘healthy range’.")
    elif bmi_value < 30:
        print("This is described as overweight.")
    elif bmi_value < 40:
        print("This is described as obesity.")
    else:
        print("This is described as severe obesity.")
else:
    pass