import streamlit as st

images = [
    {'url': 'https://image.petmd.com/files/styles/863x625/public/2022-10/beagle-dog.jpg',
     'parm': '狗'
        },
    {'url': 'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
     'parm': '鸟'
     },
    {'url': 'https://blog.theaga.org/wp-content/uploads/2019/12/SCT-ZhangJS-4-1024x683.jpg',
    'parm': '老虎'
     }
    ]

if 'num' not in st.session_state:
    st.session_state['num'] = 0

def nextImg():
    st.session_state['num'] = (st.session_state['num'] + 1) % len(images)

def lastImg():
    st.session_state['num'] = (st.session_state['num'] - 1) % len(images)
st.image(images[st.session_state['num']]['url'], caption = images[st.session_state['num']]['parm'])

c1, c2 = st.columns(2)

with c1:
    st.button('上一张', on_click = lastImg, use_container_width = True)

with c2:
    st.button('下一张', on_click=nextImg, use_container_width = True)

