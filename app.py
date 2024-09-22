from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, static_folder='data/')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        reg_no = int(request.form['reg_no'])
        data = pd.read_csv('data/student_data1.csv')
        stu_data = data.loc[data['Reg_no']==reg_no]

        subjects, marks = [], []
        sem_subjects, grades = [], []
        change = False
        for i in range(4, len(stu_data.columns)):
            if stu_data.columns[i] == 'Class Attendance':
                change = True
                continue
            elif stu_data.columns[i] == 'Rank':
                break

            if not change:
                subjects.append(stu_data.columns[i])
                marks.append(stu_data.values[0][i])
            else:
                sem_subjects.append(stu_data.columns[i])
                grades.append(stu_data.values[0][i])

            semesters = ['I SEM', 'II SEM', 'III SEM', 'IV SEM', 'V SEM', 'VI SEM', 'VII SEM', 'VIII SEM', 'CGPA']
            gpas = list(stu_data[semesters].values[0])
            placement = stu_data['Placement Offers'].values[0].split('|')
            placement = [{"name": x.split("_")[0], "salary": x.split("_")[1]} for x in placement if len(x) > 2]
            failed_sub = ""
            for i in range(len(subjects)):
                if marks[i] != "-":
                    if int(marks[i]) < 50:
                        failed_sub += subjects[i] + ", "
            failed_sub = failed_sub[:-2]


            failed_sem_sub = ""
            for i in range(len(sem_subjects)):
                    if grades[i] == 'U':
                        failed_sem_sub += sem_subjects[i] + ", "
            failed_sem_sub = failed_sem_sub[:-2]
            

        return render_template('dashboard.html',
                               photo=f'data/images/{reg_no}.png',
                               name=stu_data['Name'].values[0],
                               reg_no=reg_no,
                               tenth=stu_data['10th'].values[0],
                               twelth=stu_data['12th'].values[0],
                               subjects=subjects,
                               marks=marks,
                               failed_sub=failed_sub,
                               attendence=stu_data['Class Attendance'].values[0],
                               sem_subjects=sem_subjects,
                               grades=grades,
                               failed_sem_sub=failed_sem_sub,
                               semesters=semesters,
                               gpas=gpas,
                               rank=stu_data['Rank'].values[0],
                               total_no_of_arrears=stu_data['Total No of Arrears'].values[0],
                               no_of_mini_project=stu_data['No of Mini Project'].values[0],
                               no_of_paper_presented=stu_data['No of Paper Presented'].values[0],
                               no_of_workshop_attended=stu_data['No of Workshop Attended'].values[0],
                               iv=stu_data['IV'].values[0],
                               placement=placement,
                               vac=stu_data['VAC'].values[0],
                               prizes_won=stu_data['No of Prizes Won'].values[0]
                               )
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)