#Streamlitのインストール
import streamlit as st

# 問題文とその選択肢をリスト表記する
questions = [
    ("What type of food is sushi?", ["Japanese", "Mexican", "Italian"]),
    ("What is the main ingredient in a Caesar salad?", ["Romaine lettuce", "Spinach", "Kale"]),
    ("Which country is known for its curries?", ["India", "Thailand", "Italy"]),
    ("What is the main ingredient in a Margherita pizza?", ["Tomato sauce", "Pesto", "Alfredo sauce"]),
    ("Which type of cuisine is famous for its dumplings?", ["Chinese", "Italian", "Mexican"]),
]

# 正解数を示す変数scoreを定義し0を代入
score = 0

# クイズをループ形式で表現する
for question, options in questions:
    # 問題文の表記
    st.write(question)

    # ユーザーに選択肢を選ばせるセレクトボックスを作成
    answer = st.selectbox("Choose the correct answer:", options)

    # 正誤判定
    if answer == options[0]:
        score += 1
        st.write("Correct!")
    else:
        st.write("Incorrect!")

# 最終的なスコアを表示する
st.write("Your final score is:", score)
