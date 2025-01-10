import streamlit as st
st.title("🎈 My new app")
st.write(
    "HELLO FOR ALL 962 PROGRAMMERS! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write(
    "HELLO FOR ALL 962 PROGRAMMERS! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title("🎈 My new app")
# Заголовок приложения
st.title("Пример ввода данных")

# Текстовое поле для ввода данных
user_input = st.text_input("Введите первое число:")
user_input2 = st.text_input("Введите второе число:")
# Кнопка для подтверждения ввода
if st.button("Сложить"):
    a = int(user_input) +int(user_input2)
    st.write(f"Сумма чисел {user_input} и {user_input2} равна {int(user_input) +int(user_input2)}")
import sqlite3

# Подключение к базе данных (или создание новой)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER, city TEXT)''')

# Вставка данных
cursor.execute('INSERT INTO users (name, age, city) VALUES (?, ?, ?)', ('Алиса', 25, 'Москва'))
conn.commit()

# Чтение данных
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закрытие соединения
conn.close()
