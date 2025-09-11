from flask import Flask, render_template, request, redirect, url_for, flash, session
import random
import csv
import os

app = Flask(__name__)
app.secret_key = 'ssafy_secret_santa'

STUDENT_LIST = [
    "박명수","유재석"
]
RESULT_FILE = os.path.join(os.path.dirname(__file__), "result.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    name = request.form.get('name', '').strip()
    santa_dict = {}
    try:
        with open(RESULT_FILE, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                santa_dict[row["이름"]] = row["비밀친구"]
    except Exception:
        return render_template('index.html', error="아직 배정 결과가 없습니다.")
    if name not in santa_dict:
        return render_template('index.html', error="이름이 명단에 없거나 배정이 완료되지 않았습니다.")
    santa = santa_dict[name]
    return render_template('index.html', result=name, santa=santa)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    msg = None
    results = []
    if request.method == 'POST':
        if 'assign' in request.form:
            names = STUDENT_LIST[:]
            assigned = False
            tries = 0
            while not assigned and tries < 100:
                shuffled = names[:]
                random.shuffle(shuffled)
                assigned = all(a != b for a, b in zip(names, shuffled))
                tries += 1
            if not assigned:
                msg = '배정 실패. 다시 시도하세요.'
            else:
                assignments = dict(zip(names, shuffled))
                with open(RESULT_FILE, "w", encoding="utf-8", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(["이름", "비밀친구"])
                    for k, v in assignments.items():
                        writer.writerow([k, v])
                msg = '비밀 친구가 랜덤으로 배정되었습니다!'
    # 결과 읽기
    try:
        with open(RESULT_FILE, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) == 2:
                    results.append(row)
    except Exception:
        pass
    students = STUDENT_LIST
    return render_template('admin.html', students=students, msg=msg, results=results)

if __name__ == '__main__':
    app.run(debug=True)
