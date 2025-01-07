
listofskills = []

while True:
    skills = input('Enter skill number :\n')
    if skills == 'Done':
        break
    listofskills.append(skills)

print(', '.join(listofskills))
