import streamlit as st

# list of questions and answers
questions = [
    ("What type of food is sushi?", ["Japanese", "Mexican", "Italian"]),
    ("What is the main ingredient in a Caesar salad?", ["Romaine lettuce", "Spinach", "Kale"]),
    ("Which country is known for its curries?", ["India", "Thailand", "Italy"]),
    ("What is the main ingredient in a Margherita pizza?", ["Tomato sauce", "Pesto", "Alfredo sauce"]),
    ("Which type of cuisine is famous for its dumplings?", ["Chinese", "Italian", "Mexican"]),
]

# initialize score
score = 0

# loop through questions
for question, options in questions:
    # display question
    st.write(question)

    # get user's answer
    answer = st.selectbox("Choose the correct answer:", options)

    # check if answer is correct
    if answer == options[0]:
        score += 1
        st.write("Correct!")
    else:
        st.write("Incorrect!")

# display final score
st.write("Your final score is:", score)
