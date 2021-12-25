name = input('your name : ')
age = int(input('age :'))
gender= int(input('1.Male \n 2.Female'))
if gender==1:
  gender='male'
if gender==2:
  gender='female \n' 
h= int(input('Enter hieght: '))
w= int(input('Enter Weight:'))
bmi=(w/(h*h))*10000
print("bmi :",bmi)
bmiresult= 'data'
if bmi<16:
   bmiresult='Very thin'
elif bmi>=16 and bmi<=18.6:
     bmiresult='Thin'
elif bmi>18.6 and bmi<=25:
     bmiresult='Normal'
elif bmi>25 and bmi<=30:
     bmiresult='Overweight'
elif bmi>30 and bmi<=35:
     bmiresult='Obese I'
elif bmi>35 and bmi<=40:
     bmiresult='Obese II'
elif bmi>40:
     bmiresult='Obese III - Attention Needed'

print('Gender:',gender)
print('Body Type eqert:',bmiresult)