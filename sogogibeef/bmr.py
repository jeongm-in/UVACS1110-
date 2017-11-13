# Version : Jeong Min Lim (sogogibeef)
# bmr.py contains function st_jeor that takes mass, height, age, and sex
# and then returns Mifflin St Jeor estimate of the basic metabolic rate.

# P = ((10.0 * mass / 1 kg) + (6.25 * height / 1 cm) - (5.0 * age / 1 year) + sex) kcal / day
# if sex == male, s = 5 / if sex == female, s = -161

def st_jeor(mass, height, age, sex):
    if sex is 'female':
        sex_coefficient = -161
    else:
        sex_coefficient = 5
    metabolic_rate = (10.0 * mass) + (6.25 * height) - (5.0 * age) + sex_coefficient
    return metabolic_rate

