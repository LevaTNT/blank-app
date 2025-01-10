import streamlit as st
import sqlite3
import pandas as pd
import os

# Определение пути к базе данных
db_path = os.path.join(os.path.dirname(__file__), 'data.db')

# Подключение к базе данных (или создание новой)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)''')
st.title("Введите данные для ввода")
# Текстовое поле для ввода данных
user_input = st.text_input("Введите имя:")
user_input2 = st.text_input("Введите возраст:")
if st.button("Ввести"):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (user_input, int(user_input2)))
    conn.commit()

if st.button("Вывести"):
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['Имя', 'Возраст'])
    st.title('База данных пользователей')
    st.dataframe(df)  # Можно использовать st.table(df) для статической таблицы

        
# Закрытие соединения
conn.close()
