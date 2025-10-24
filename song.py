import streamlit as st

st.set_page_config(page_title = '音乐播放器', page_icon = '🎵')


songs = [
    {'url': 'https://music.163.com/song/media/outer/url?id=2659905369.mp3',
     'name': '这里是神奇的赛尔号',
     'image':'https://p2.music.126.net/ZC7Qbic233GIv5Tuc9XgYA==/109951170309548088.jpg?param=450y400',
     'singer':'歌手: 张杰'
     
        },
    {'url': 'https://music.163.com/song/media/outer/url?id=33340727.mp3',
     'name': 'Soaring',
     'image':'https://p1.music.126.net/B1Ycql6Qir5UtepTAuH6bg==/7984653442306264.jpg?param=450y400',
     'singer':'歌手: TomLeevis'
     },
    {'url': 'https://music.163.com/song/media/outer/url?id=2735908694.mp3',
    'name': '乘风破浪',
     'image':'https://p2.music.126.net/c406IKOXIBjEZUiehQVtCw==/109951171855581805.jpg?param=450y400',
     'singer':'歌手: 锋速战警'
     }
    ]

if 'num' not in st.session_state:
    st.session_state['num'] = 0

def nextSong():
    st.session_state['num'] = (st.session_state['num'] + 1) % len(songs)

def lastSong():
    st.session_state['num'] = (st.session_state['num'] - 1) % len(songs)
    
a1, a2 = st.columns([1, 2])


with a1:
    st.image(songs[st.session_state['num']]['image'])

    
with a2:
    st.subheader(songs[st.session_state['num']]['name'])
    st.text(songs[st.session_state['num']]['singer'])
    st.audio(songs[st.session_state['num']]['url'])
    c1, c2 = st.columns(2)
    with c1:
        st.button('上一首', on_click = lastSong, use_container_width = True)
    with c2:
        st.button('下一首', on_click=nextSong, use_container_width = True)


    


    
