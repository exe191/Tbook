import tkinter as tk
from tkinter import ttk, filedialog


class BookManager:
    def __init__(self, window):
        self.window = window
        self.text_area = None
        self.label = None
        self.btn = None
        self.btn2 = None
        self.create_window()
        self.create_text_area()
        self.add_button_book()
        self.delete_button_book()

    def create_window(self):
        self.window.title("BookMagic_V0.0.1")
        self.window.iconbitmap(r'img\book.ico')
        self.window.wm_state('zoomed')
        self.window.configure(bg='#DDBEAA')
        self.label = tk.Label(self.window, bg='#DDBEAA')
        self.label.pack(pady=60)

    def create_text_area(self):
        self.text_area = tk.Text(self.window, wrap='word', width=50, height=15)
        self.text_area.pack(expand=True, fill='both')

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=(('Текстовые файлы', '*.fb2'), ('Все файлы', '*.*'))
        )
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def delete_book(self):
        self.text_area.delete(1.0, tk.END)

    def add_button_book(self):
        self.btn = ttk.Button(self.window, text="Добавить книгу", command=self.open_file)
        self.btn.place(relx=0.1, rely=0.07)

    def delete_button_book(self):
        self.btn2 = ttk.Button(self.window, text="Удалить книгу", command=self.delete_book)
        self.btn2.place(relx=0.8, rely=0.07)


if __name__ == '__main__':
    root = tk.Tk()
    app = BookManager(root)
    root.mainloop()
