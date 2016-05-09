import tkinter as tk
class SimpleTodo():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x600+30+30')
        self.root.title('SimpleTodo')
        input_text = tk.Entry(self.root)
        input_text.pack(side=tk.TOP, fill=tk.X)
        todo_list = tk.Listbox(self.root)

        todos = self.load_data()
        for todo in todos:
            todo_list.insert(tk.END, todo.strip())
        def return_callback(event):
            todo_list.insert(0, input_text.get())
            input_text.delete(0, tk.END)

        def edit_callback(event):
            input_text.delete(0, tk.END)
            input_text.insert(0,todo_list.get(todo_list.curselection()))

        input_text.bind("<Return>", return_callback)
        todo_list.pack(fill=tk.X)
        todo_list.bind("<Return>", edit_callback)
        b = tk.Button(self.root, text="Delete", command=lambda lb=todo_list: todo_list.delete(tk.ANCHOR))
        b.pack()

        def on_closing():
            todos = todo_list.get(0, tk.END)
            self.save_data(todos)
            self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        self.root.mainloop()

    def load_data(self):
        """
        Load data/todolist.txt

        Returns
        --------
        todo list
        """
        todos = []
        with open('data/todolist.txt', 'r') as f:
            todos = f.readlines()
        return todos

    def save_data(self, todos):
        """
        Save todos to data/todolist.txt
        
        Parameters
        ----------
        todos: list of todo(string)

        """
        with open('data/todolist.txt', 'w') as f:
            for todo in todos:
                f.write(todo)
                f.write('\n')
if __name__ == '__main__':
    app = SimpleTodo()
