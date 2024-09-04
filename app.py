import streamlit as st
from random import choice

hands = ["グー", "チョキ", "パー"]

st.title("じゃんけんゲーム")
st.caption("グー、チョキ、パーのどれかを出そう！")

st.subheader("説明")
st.text("ボタンを押すと、相手が手を出します。じゃんけんで勝利しましょう！")

gu_btn = st.button("グー")
choki_btn = st.button("チョキ")
pa_btn = st.button("パー")


hand = choice(hands)
if gu_btn == True:
    st.text("あなた：グー")
    if hand == "グー":
        st.text("相手：グー")
        st.text("引き分け！")
    elif hand == "チョキ":
        st.text("相手：チョキ")
        st.text("あなたの勝ち！")
    else:
        st.text("相手：パー")
        st.text("あなたの負け")

if choki_btn == True:
    st.text("チョキが押されました")
    if hand == "グー":
        st.text("相手：グー")
        st.text("あなたの負け")
    elif hand == "チョキ":
        st.text("相手：チョキ")
        st.text("引き分け！")
    else:
        st.text("相手：パー")
        st.text("あなたの勝ち！")

if pa_btn == True:
    st.text("パーが押されました")
    if hand == "グー":
        st.text("相手：グー")
        st.text("あなたの勝ち！")
    elif hand == "チョキ":
        st.text("相手：チョキ")
        st.text("あなたの負け")
    else:
        st.text("相手：パー")
        st.text("引き分け！")