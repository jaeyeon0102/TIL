# Secret Santa GUI (tkinter 기반) 파일

import tkinter as tk
from tkinter import messagebox, filedialog
import random
import csv


import os

# 항상 SecretSanta 폴더 내에 저장
RESULT_FILE = os.path.join(os.path.dirname(__file__), "result.csv")

# 학생 명단을 파이썬 리스트로 직접 작성
student = [
    "권혁준", "김가영", "김명준", "김서현", "김소원", "김승수", "김은수", "김은주",
    "김주연", "김휘민", "문경진", "박사랑", "박주양", "박해웅", "변지훈", "소재헌",
    "송영석", "안치원", "유동훈", "이선영", "이재연", "이희수", "임선우", "정문기",
    "정성윤", "최준형", "한가희", "홍지은"
]

class SecretSantaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Secret Santa 추첨기")
        master.geometry("400x500")

        self.participants = []
        self.assignments = {}

        # UI 요소
        self.label = tk.Label(master, text="Secret Santa (비밀 친구) 추첨기", font=("Arial", 16))
        self.label.pack(pady=10)


        self.load_btn = tk.Button(master, text="참가자 명단 불러오기", command=self.load_participants)
        self.load_btn.pack(pady=5)

        self.listbox = tk.Listbox(master, height=10)
        self.listbox.pack(pady=5, fill=tk.BOTH, expand=True)

        self.assign_btn = tk.Button(master, text="비밀 친구 랜덤 배정", command=self.assign_secret_santa)
        self.assign_btn.pack(pady=5)

        self.name_entry = tk.Entry(master)
        self.name_entry.pack(pady=5)
        self.name_entry.insert(0, "이름 입력 후 확인")

        self.check_btn = tk.Button(master, text="내 비밀 친구 확인", command=self.check_my_santa)
        self.check_btn.pack(pady=5)

        self.admin_btn = tk.Button(master, text="전체 결과(관리자)", command=self.show_all_assignments)
        self.admin_btn.pack(pady=5)

        self.save_btn = tk.Button(master, text="결과 저장", command=self.save_results)
        self.save_btn.pack(pady=5)

    def load_participants(self):
        # student 리스트에서 참가자 명단을 불러옴
        self.participants = student[:]
        self.listbox.delete(0, tk.END)
        for name in self.participants:
            self.listbox.insert(tk.END, name)
        messagebox.showinfo("성공", f"{len(self.participants)}명 참가자 불러옴!")

    def assign_secret_santa(self):
        if not self.participants or len(self.participants) < 2:
            messagebox.showwarning("경고", "참가자 명단을 먼저 불러오세요.")
            return
        names = self.participants[:]
        assigned = False
        tries = 0
        while not assigned and tries < 100:
            shuffled = names[:]
            random.shuffle(shuffled)
            assigned = all(a != b for a, b in zip(names, shuffled))
            tries += 1
        if not assigned:
            messagebox.showerror("오류", "배정 실패. 다시 시도하세요.")
            return
        self.assignments = dict(zip(names, shuffled))
        messagebox.showinfo("성공", "비밀 친구가 랜덤으로 배정되었습니다!")

    def check_my_santa(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("경고", "이름을 입력하세요.")
            return
        if name not in self.assignments:
            messagebox.showwarning("경고", "이름이 명단에 없거나 배정이 완료되지 않았습니다.")
            return
        santa = self.assignments[name]
        messagebox.showinfo("비밀 친구", f"{name}님의 비밀 친구는: {santa}")

    def show_all_assignments(self):
        if not self.assignments:
            messagebox.showwarning("경고", "아직 배정이 완료되지 않았습니다.")
            return
        result = "전체 비밀 친구 배정 결과:\n"
        for k, v in self.assignments.items():
            result += f"{k} → {v}\n"
        messagebox.showinfo("전체 결과", result)

    def save_results(self):
        if not self.assignments:
            messagebox.showwarning("경고", "아직 배정이 완료되지 않았습니다.")
            return
        try:
            with open(RESULT_FILE, "w", encoding="utf-8", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["이름", "비밀친구"])
                for k, v in self.assignments.items():
                    writer.writerow([k, v])
            messagebox.showinfo("성공", f"결과가 {RESULT_FILE}에 저장되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"저장 실패: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SecretSantaGUI(root)
    root.mainloop()
