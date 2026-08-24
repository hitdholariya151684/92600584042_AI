print('='*30)
print('CAREER GUIDANCE SYSTEM')
print('='*30)
print('\nAnswer the following questions with yes or no.')
q1=input('Do you like coding? : Yes / NO ---  ').lower()
q2=input('DO you like mathematics? : Yes / NO ---  ').lower()
q3=input('DO you like bialogy? : Yes / NO ---  ').lower()
q4=input('DO you like drawing? : Yes / NO ---  ').lower()
print()
print('='*5,'Career Suggestion','='*5,'\n')
print('Suggested Career : ',end="")
if q1=='no' and q2=='no' and q3=='no' and q4=='no':
    print('Explore your intrests and cureer option further.')
elif q1=='no' and q2=='no' and q3=='no' and q4=='yes':
    print('Graphic Designer / Animator')
elif q1=='no' and q2=='no' and q3=='yes' and q4=='no':
    print('Pharacist / Nurse')
elif q1=='no' and q2=='no' and q3=='yes' and q4=='yes':
    print('Medial Illustrator / Healthcare Educator')
elif q1=='no' and q2=='yes' and q3=='no' and q4=='no':
    print('Engineer / Data Analyst')
elif q1=='no' and q2=='yes' and q3=='no' and q4=='yes':
    print('Architect')
elif q1=='no' and q2=='yes' and q3=='yes' and q4=='no':
    print('Doctor')
elif q1=='no' and q2=='yes' and q3=='yes' and q4=='yes':
    print('Medical illustrator / Biomedical Designer')
elif q1=='yes' and q2=='no' and q3=='no' and q4=='no':
    print('Programmer / Web Developer')
elif q1=='yes' and q2=='no' and q3=='no' and q4=='yes':
    print('Web Designer / UI-UX Designer')
elif q1=='yes' and q2=='no' and q3=='yes' and q4=='no':
    print('Haalth App Developer')
elif q1=='yes' and q2=='no' and q3=='yes' and q4=='yes':
    print('Medical Illustrator')
elif q1=='yes' and q2=='yes' and q3=='no' and q4=='no':
    print('Software Engineer / Computer Scientist')
elif q1=='yes' and q2=='yes' and q3=='no' and q4=='yes':
    print('Game Developer / UI Engineer')
elif q1=='yes' and q2=='yes' and q3=='yes' and q4=='no':
    print('Bioinformatics Scientist')
elif q1=='yes' and q2=='yes' and q3=='yes' and q4=='yes':
    print('Biomedical Software Engineer / Medical Thechnology Specialist')
else :
    print('Please, Give proper answer about your Career.') 
    
print('\nThank you for using the Carrer Guidance Expert System!\n')