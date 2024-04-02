import tkinter as tk
from tkinter import ttk


class BlockSalesTab:
    def __init__(self, notebook, db):
        self.db = db
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Bloquer les ventes")
        block_sales_label = tk.Label(self.tab, text="Entrer un user ID por bloquer les ventes:")
        block_sales_label.pack()
        self.block_sales_entry = tk.Entry(self.tab)
        self.block_sales_entry.pack()
        block_sales_button = tk.Button(self.tab, text="Bloquer les ventes", command=self.block_sales)
        block_sales_button.pack()
        self.block_sales_result_label = tk.Label(self.tab, text="")
        self.block_sales_result_label.pack()

    def block_sales(self):
        user_id = self.block_sales_entry.get()
        cursor = self.db.cursor()
        query = "UPDATE oc_user SET status = 'blocked' WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        self.db.commit()

        self.block_sales_result_label.config(text=f"Ventes bloquer pour l'utilisateur: {user_id}")
        cursor.close()

        
