import streamlit as st
import sqlite3
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Установление области доступа для Google Sheets и Google Drive API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Путь к файлу JSON с учетными данными
creds = ServiceAccountCredentials.from_json_keyfile_name('nimble-bonus-343713-1fd134be8df7.json', scope)

# Авторизация клиента с учетными данными
client = gspread.authorize(creds)
st.write(client)

# Подключение к таблице по ее названию
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/165ZyfacpRoQpw7CuCymJfNgwEwMXKUGDRjIkclce4to/edit?usp=sharing').sheet1  # Используйте sheet1 для первой страницы

# Чтение всех данных из таблицы
data = sheet.get_all_records()

# Преобразование данных в DataFrame для удобного отображения в Streamlit
df2 = pd.DataFrame(data)
st.dataframe(df)

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
