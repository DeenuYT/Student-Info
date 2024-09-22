# Student-Info
KNCET Student Information Web App for PTA. This web application shows the student details such as ACADEMIC PERFORMANCE IN UNIVERSITY EXAMINATION , CO-CURRICULAR & EXTRA CURRICULAR ACTIVITIES and PLACEMENT OFFERS.

## Setup Instructions
1. Clone the git repo.
   
   ```bash
   git clone https://github.com/DeenuYT/Student-Info.git
   ```
3. Create a virtual environment.
   ```bash
   python -m venv <venv name>
   ```
4. Install the required libraries.
   ```bash
   pip install flask pandas
   ```
5. Copy the students data `(student_details.csv)` to the `data` directory.  `Note`: Use the exact format given in the `student_details.csv` and the register number must match the profile file name.
6. Copy the student profile image inside the `data/images/` directory. Use the **register number** as the profile image file name.
7. Run the `app.py`.
   ```bash
   python app.py
   ```
