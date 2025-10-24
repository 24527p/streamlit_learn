import streamlit as st

video_url = [
    {'path': 'videoDir/1.mp4',
     'title': '熊出没之丛林总动员',
     'episode': '第1集'
        },
    {'path':'videoDir/2.mp4',
     'title': '熊出没之丛林总动员',
     'episode': '第2集'
        },
    {'path': 'videoDir/3.mp4',
     'title': '熊出没之丛林总动员',
     'episode': '第3集'
        }
    ]
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

st.title(video_url[st.session_state['ind']]['title']+'-'+video_url[st.session_state['ind']]['episode'])
st.video(video_url[st.session_state['ind']]['path'])
introduction = '''
介绍：
《熊出没之丛林总动员》是动画片《熊出没》系列的第3季作品，由深圳华强文化科技集团出品的喜剧动画片，林永长、林汇达导演，徐芸、江波、叶天龙、林汇达编剧 [5]。共104集，网络播放版89集 [4]。
动画片《熊出没之丛林总动员》讲述的是熊大和熊二周游世界后重新回到丛林，再次见到丛林的朋友们。光头强追着两熊也来到丛林，再次成为伐木工，在已经规划为自然保护区的丛林里盗砍盗伐树木。为了阻止光头强破坏森林，以熊大熊二为首的丛林动物们和光头强再次展开一幕幕搞笑的较量。
该剧已于2013年7月13日在CCTV-14播出。
'''
st.text(introduction)
def play(arg):
    st.session_state['ind'] = int(arg)

for i in range(len(video_url)):
    st.button('第'+str(i+1)+'集', use_container_width = True, on_click = play, args = ([i]))
