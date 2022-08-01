#%%
from typing import Tuple
import streamlit as st
import pandas as pd
import engine
import sys
from streamlit import cli as stcli

#%%
if __name__ == '__main__':
    if not st._is_running_with_streamlit:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
#%%
@st.cache
def answer(question : str) -> Tuple:
    response = engine.answer(question)
    ans = response.get("answers")
    quotes = [doc.text for doc in response.get("selected_documents")]
    return ans, quotes, response

#%%
def update(question: str):
    ans, quotes, response = answer(question)
    st.write(ans[0])
    df = pd.DataFrame(quotes, columns=['quotes'])
    st.write(df)
    st.write(response)


#%%
st.title('GPT-3 Q/A Engine')
st.sidebar.text_input("Your question", value="Who is the show host?", key="question")
st.sidebar.button("Answer", on_click=update, args=(st.session_state.question, ))

