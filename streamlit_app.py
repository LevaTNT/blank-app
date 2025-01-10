import streamlit as st
f = open("test.txt","rw")
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
f.write(f"{user_input} {user_input2} {a}")
