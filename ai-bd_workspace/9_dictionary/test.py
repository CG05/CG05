import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel

class InstagramCloneApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('인스타 클론')
        self.geometry('300x200')

        self.user_dict = {"admin": "1234"}
        self.account_dict = {}
        self.tag_dict = {}
        self.feed_list = []

        self.current_user = None
        self.initialize_login_frame()

    def initialize_login_frame(self):
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(self.login_frame, text="계정명").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        tk.Label(self.login_frame, text="비밀번호").pack()
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.pack()

        tk.Button(self.login_frame, text="로그인", command=self.login).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in self.user_dict and self.user_dict[username] == password:
            self.current_user = "@" + username
            messagebox.showinfo("로그인 성공", f"{username}님 환영합니다.")
            self.login_frame.pack_forget()  # 로그인 화면 숨기기
            self.initialize_main_frame()    # 메인 화면 표시
        else:
            messagebox.showerror("로그인 실패", "계정명 또는 비밀번호가 잘못되었습니다.")

    def initialize_main_frame(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        tk.Button(self.main_frame, text="게시", command=self.post).pack()
        tk.Button(self.main_frame, text="검색", command=self.search).pack()
        tk.Button(self.main_frame, text="피드 보기", command=self.show_feed).pack()
        tk.Button(self.main_frame, text="로그아웃", command=self.logout).pack()
        tk.Button(self.main_frame, text="계정 삭제", command=self.delete_account).pack()

    def post(self):
        post_window = Toplevel(self)
        post_window.title("게시물 작성")
        
        tk.Label(post_window, text="게시물 내용:").pack()
        content_entry = tk.Entry(post_window)
        content_entry.pack()
        
        tk.Label(post_window, text="태그 입력(#a #b):").pack()
        tags_entry = tk.Entry(post_window)
        tags_entry.pack()
        
        def submit_post():
            content = content_entry.get()
            tags = tags_entry.get().split()
            if not all(tag.startswith('#') for tag in tags):
                messagebox.showerror("오류", "모든 태그는 '#'으로 시작해야 합니다.")
                return
            if self.current_user not in self.account_dict:
                self.account_dict[self.current_user] = {}
            self.account_dict[self.current_user][content] = tags
            for tag in tags:
                if tag not in self.tag_dict:
                    self.tag_dict[tag] = {}
                self.tag_dict[tag][content] = self.current_user
            post_window.destroy()
            messagebox.showinfo("성공", "게시물이 성공적으로 등록되었습니다.")

        tk.Button(post_window, text="게시", command=submit_post).pack()

    def search(self):
        search_query = simpledialog.askstring("검색", "검색어 입력(@계정명 또는 #태그):")
        if not search_query:
            return
        if search_query.startswith("@"):
            accounts = [acc for acc in self.account_dict if search_query.strip("@") in acc]
            if accounts:
                messagebox.showinfo("검색 결과", "\n".join(accounts))
            else:
                messagebox.showerror("검색 결과", "계정이 없습니다.")
        elif search_query.startswith("#"):
            if search_query in self.tag_dict:
                posts = "\n".join(f"{post}: {self.tag_dict[search_query][post]}" for post in self.tag_dict[search_query])
                messagebox.showinfo("검색 결과", posts)
            else:
                messagebox.showerror("검색 결과", "태그에 해당하는 게시물이 없습니다.")
        else:
            messagebox.showerror("검색 오류", "검색어는 '@' 또는 '#'으로 시작해야 합니다.")

    def show_feed(self):
        feed_window = Toplevel(self)
        feed_window.title("피드")
        if self.current_user in self.account_dict:
            for post, tags in self.account_dict[self.current_user].items():
                tk.Label(feed_window, text=f"{post} {tags}").pack()
        else:
            tk.Label(feed_window, text="게시물이 없습니다.").pack()

    def logout(self):
        self.current_user = None
        self.main_frame.pack_forget()
        self.initialize_login_frame()

    def delete_account(self):
        if messagebox.askyesno("계정 삭제", "정말로 계정을 삭제하시겠습니까?"):
            del self.user_dict[self.current_user.lstrip("@")]
            if self.current_user in self.account_dict:
                del self.account_dict[self.current_user]
            self.logout()

if __name__ == "__main__":
    app = InstagramCloneApp()
    app.mainloop()
