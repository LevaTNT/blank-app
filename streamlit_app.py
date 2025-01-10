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
user_input = st.text_input("Введите что-нибудь:")

# Кнопка для подтверждения ввода
if st.button("Подтвердить"):
    st.write(f"Вы ввели: {user_input}")
