from src.utils.date_processor import get_last_week_info
import pandas as pd
import random
import sys
import os


folder_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.abspath(".")

last_week_info = get_last_week_info()
folder_name = f"{last_week_info['year']}W{last_week_info['week_no']}"
save_path = os.path.join(folder_path, 'result', folder_name)
os.makedirs(save_path, exist_ok=True)

file_name = 'ABC.xlsx'

excel_file = os.path.join(save_path, file_name)
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    pd.DataFrame().to_excel(writer, index=False, sheet_name='Data')

