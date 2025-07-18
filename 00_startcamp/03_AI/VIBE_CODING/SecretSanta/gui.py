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
        master.geometry("430x600")
        master.configure(bg="#f6f7fb")

        self.participants = []
        self.assignments = {}
        self.is_admin = False

        # --- 상단 로고 및 타이틀 ---
        self.logo = tk.Label(master, text="SSAFY", font=("Segoe UI", 24, "bold"), fg="#1976d2", bg="#f6f7fb")
        self.logo.pack(pady=(25, 0))
        self.title_label = tk.Label(master, text="마니또 정하기!", font=("Segoe UI", 16, "bold"), fg="#333", bg="#f6f7fb")
        self.title_label.pack(pady=(5, 18))

        # --- 중앙 프레임 (화면 전환용) ---
        self.center_frame = tk.Frame(master, bg="#f6f7fb")
        self.center_frame.pack(expand=True, fill=tk.BOTH)

        # --- 하단 화면전환 버튼 ---
        self.switch_btn = tk.Button(master, text="담당자 화면으로 전환하기", command=self.toggle_admin,
                                    font=("Segoe UI", 10), bg="#1976d2", fg="white", activebackground="#1251a3", relief="flat")
        self.switch_btn.pack(side=tk.BOTTOM, pady=18, ipadx=8, ipady=2)

        self.show_user_view()

    def clear_center(self):
        for widget in self.center_frame.winfo_children():
            widget.destroy()

    def show_user_view(self):
        self.is_admin = False
        self.clear_center()

        # 이름 입력 (placeholder)
        entry_frame = tk.Frame(self.center_frame, bg="#f6f7fb")
        entry_frame.pack(pady=(40, 10))
        self.name_entry = tk.Entry(entry_frame, font=("Segoe UI", 13), width=18, bd=2, relief="groove", fg="#aaa")
        self.name_entry.pack(side=tk.LEFT, padx=(0, 8))
        self.name_entry.insert(0, "이름 입력")
        self.name_entry.bind("<Button-1>", self._clear_placeholder)
        self.name_entry.bind("<FocusIn>", self._clear_placeholder)
        self.name_entry.bind("<FocusOut>", self._add_placeholder)
        self.name_placeholder = True

        self.check_btn = tk.Button(entry_frame, text="내 마니또 확인하기", command=self.check_my_santa,
                                   font=("Segoe UI", 12), bg="#6c63ff", fg="white", activebackground="#554fd8", relief="flat")
        self.check_btn.pack(side=tk.LEFT)

        # 결과 표시 라벨
        self.result_label = tk.Label(self.center_frame, text="", font=("Segoe UI", 14), bg="#f6f7fb", fg="#333")
        self.result_label.pack(pady=(40, 0))

    def _clear_placeholder(self, event):
        if getattr(self, 'name_placeholder', False):
            self.name_entry.delete(0, tk.END)
            self.name_entry.config(fg="#444")
            self.name_placeholder = False

    def _add_placeholder(self, event):
        if not self.name_entry.get():
            self.name_entry.insert(0, "이름 입력")
            self.name_entry.config(fg="#aaa")
            self.name_placeholder = True

    def show_admin_view(self):
        self.is_admin = True
        self.clear_center()

        # 뒤로가기 버튼
        back_btn = tk.Button(self.center_frame, text="뒤로가기", command=self.toggle_admin,
                             font=("Segoe UI", 10), bg="#bdbdbd", fg="#333", activebackground="#888", relief="flat")
        back_btn.pack(pady=(10, 0), ipadx=8, ipady=2, anchor="ne")

        # 참가자 명단 불러오기
        self.load_btn = tk.Button(self.center_frame, text="참가자 명단 불러오기", command=self.load_participants,
                                  font=("Segoe UI", 12), bg="#1976d2", fg="white", activebackground="#1251a3", relief="flat", height=2)
        self.load_btn.pack(pady=10, ipadx=10, ipady=2)

        # 참가자 리스트박스
        frame_list = tk.Frame(self.center_frame, bg="#f6f7fb")
        frame_list.pack(pady=5)
        self.listbox = tk.Listbox(frame_list, height=10, width=30, font=("Segoe UI", 11), bd=2, relief="groove", fg="#333")
        self.listbox.pack(side=tk.LEFT, padx=(0, 0))
        scrollbar = tk.Scrollbar(frame_list, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # 랜덤 배정 버튼
        self.assign_btn = tk.Button(self.center_frame, text="비밀 친구 랜덤 배정", command=self.assign_secret_santa,
                                    font=("Segoe UI", 12), bg="#ffb347", fg="white", activebackground="#e09e36", relief="flat", height=2)
        self.assign_btn.pack(pady=10, ipadx=10, ipady=2)

        # 결과 저장 버튼
        self.save_btn = tk.Button(self.center_frame, text="결과 저장", command=self.save_results,
                                  font=("Segoe UI", 12), bg="#4caf50", fg="white", activebackground="#357a38", relief="flat", height=2)
        self.save_btn.pack(pady=10, ipadx=10, ipady=2)

        # 안내문구
        tk.Label(self.center_frame, text="※ 담당자만 배정/저장이 가능합니다.",
                 font=("Segoe UI", 10), fg="#888", bg="#f6f7fb").pack(pady=(30, 0))

    def toggle_admin(self):
        if self.is_admin:
            self.switch_btn.config(text="담당자 화면으로 전환하기")
            self.show_user_view()
        else:
            self.switch_btn.config(text="마니또 확인 화면으로 전환하기")
            self.show_admin_view()

    def load_participants(self):
        self.participants = student[:]
        if self.is_admin:
            self.listbox.delete(0, tk.END)
            for name in self.participants:
                self.listbox.insert(tk.END, name)
            messagebox.showinfo("성공", f"{len(self.participants)}명 참가자 불러옴!")

    def assign_secret_santa(self):
        if not self.is_admin:
            messagebox.showwarning("경고", "담당자 화면에서만 가능합니다.")
            return
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
            self.result_label.config(text="이름을 입력하세요.", fg="#e53935", font=("Segoe UI", 14, "bold"))
            return
        if name not in self.assignments:
            self.result_label.config(text="이름이 명단에 없거나 배정이 완료되지 않았습니다.", fg="#e53935", font=("Segoe UI", 14, "bold"))
            return
        santa = self.assignments[name]
        # 이름만 크게, 색상 강조
        result_text = f"{name}님의 비밀친구는\n"
        self.result_label.config(text=result_text, fg="#333", font=("Segoe UI", 14))
        self.result_label.after(10, lambda: self.result_label.config(text=f"{result_text}{santa}", fg="#1976d2", font=("Segoe UI", 28, "bold")))
        # result.csv에서 읽기
        santa_dict = {}
        try:
            with open(RESULT_FILE, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    santa_dict[row["이름"]] = row["비밀친구"]
        except Exception:
            self.result_label.config(text="아직 배정 결과가 없습니다.", fg="#e53935", font=("Segoe UI", 14, "bold"))
            return
        if name not in santa_dict:
            self.result_label.config(text="이름이 명단에 없거나 배정이 완료되지 않았습니다.", fg="#e53935", font=("Segoe UI", 14, "bold"))
            return
        santa = santa_dict[name]
        # 이름만 크게, 색상 강조
        result_text = f"{name}님의 비밀친구는\n"
        self.result_label.config(text=result_text, fg="#333", font=("Segoe UI", 14))
        self.result_label.after(10, lambda: self.result_label.config(text=f"{result_text}{santa}", fg="#1976d2", font=("Segoe UI", 28, "bold")))

    def save_results(self):
        if not self.is_admin:
            messagebox.showwarning("경고", "담당자 화면에서만 가능합니다.")
            return
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
