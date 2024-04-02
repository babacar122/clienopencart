import tkinter as tk
from tkinter import ttk

class OngoingTransactionsTab:
    def __init__(self, notebook, db):
        self.db = db
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Transactions en cours")

        ongoing_transactions_label = tk.Label(self.tab, text="Transactions en cours:")
        ongoing_transactions_label.pack()
        self.ongoing_transactions_listbox = tk.Listbox(self.tab, width=50)
        self.ongoing_transactions_listbox.pack()

        list_ongoing_transactions_button = tk.Button(self.tab, text="Listes des transactions en cours", command=self.list_ongoing_transactions)
        list_ongoing_transactions_button.pack()

    def list_ongoing_transactions(self):
        cursor = self.db.cursor()
        query = "SELECT order_id, customer_id, total FROM oc_order WHERE order_status_id = (SELECT order_status_id FROM oc_order_status WHERE name = 'Processing')"
        cursor.execute(query)
        ongoing_transactions = cursor.fetchall()
        self.ongoing_transactions_listbox.delete(0, tk.END)

        for transaction in ongoing_transactions:
            transaction_info = f"Id commande: {transaction[0]}, Id customer: {transaction[1]}, Totale: {transaction[2]}"
            self.ongoing_transactions_listbox.insert(tk.END, transaction_info)
        cursor.close()
