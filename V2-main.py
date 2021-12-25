import pandas as pd

df = pd.read_excel(r'C:\Users\tamil\Downloads\RDA_short_report-xl.xlsx',
                   sheet_name='Table 2')
name = input('your name : ')
age = int(input('age :'))
gender = int(input('1.Male \n 2.Female'))
if gender == 1:
    gender = 'male'
if gender == 2:
    gender = 'female \n'
h = int(input('Enter hieght: '))
w = int(input('Enter Weight:'))
bmi = (w / (h * h)) * 10000
print("bmi :", bmi)
bmiresult = 'data'
if bmi < 16:
    bmiresult = 'Very thin'
elif bmi >= 16 and bmi <= 18.6:
    bmiresult = 'Thin'
elif bmi > 18.6 and bmi <= 25:
    bmiresult = 'Normal'
elif bmi > 25 and bmi <= 30:
    bmiresult = 'Overweight'
elif bmi > 30 and bmi <= 35:
    bmiresult = 'Obese I'
elif bmi > 35 and bmi <= 40:
    bmiresult = 'Obese II'
elif bmi > 40:
    bmiresult = 'Obese III - Attention Needed'

lifestyle = int(
    input(
        "Choose your Lifestyle:\n 1.Sedentary \n   2.Moderately Active \n 3. Very Active"
    ))
if lifestyle == 1:
    lifestyle = 'Sedentary'
    cal = df.iloc[1, 3]
if lifestyle == 2:
    lifestyle = 'Moderately Active'
    cal = df.iloc[2, 3]
    lifestyle = 'Very Active'
    cal = df.iloc[3, 3]
a = df.iloc[10, 7]

print('Gender:', gender)
print('Body Type :', bmiresult)
print('Lifestyle:')
print('Calorie Intake', cal, 'Kcal')
