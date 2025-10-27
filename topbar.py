import streamlit as st

st.title("选项卡简单示例")
tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["光头强数字档案", "南宁美食地图", "相册", '个人简历生成器', '视频播放器', '视频播放器'])

with tab1:
    st.header("这是第一个选项卡")
    st.markdown("#### 第一个选项卡的内容")
    st.title('熊出没不同光头强实力排行')

    st.header('大力士')
    st.image('imageDir/1.jpg', caption='大力士')
    st.text('这是第一季光头强不甘被两头臭狗熊欺负，刻苦锻炼的结果。此时，他能凭借蛮力和熊二硬碰硬，最后将其撂倒。但最后被胸大用猎枪击退。')

    st.header('黑锅侠')
    st.image('imageDir/2.jpg', caption='黑锅侠')
    st.text('此时来到第3季丛林总动员，这也是我认为熊出没系列最好看的一部。光头强收到了李老板寄来的国外采购的高科技，光头强用一口铁锅变身黑锅侠，三下五除二就打败了两头狗熊，但最后被启动了自毁程序，惨遭剧情杀。')

    st.header('疯狂科学家')
    st.image('imageDir/3.jpg',caption='疯狂科学家')
    st.text('猫头鹰得了预知梦，得知光头强智商爆发，变成科学怪人。科学怪人光头强不仅一身强壮的肌肉，而且擅长使用生化武器。手段变化多端。')

    st.header('腐朽国王')
    st.image('imageDir/4.jpg', caption='腐朽国王')
    st.text('这个形态拥有强大的黑暗力量，还有专属大鸟坐骑')

    st.header('古神瑞兹')
    st.image('imageDir/5.jpg', caption='古神瑞兹')
    st.text('能驱使蝗虫，并掌握雷电法术')

    st.header('吞噬者形态')
    st.image('imageDir/6.jpg', caption='吞噬者')
    st.text('能召唤出熊出没电影出现过的所有反派，其中天火这个战争机器破坏力超强')

    st.header('金色s1形态')
    st.image('imageDir/7.jpg', caption='金色光头强')
    st.text('光头强变回s1伐木工形象，散发着耀眼金光，专武电锯更是能斩断一切。')

with tab2:
    st.header("这是第二个选项卡")
    st.markdown("#### 第二个选项卡的内容")
    import pandas as pd
    import numpy as np

    restaurants_data = {
        
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }

    df= pd.DataFrame(restaurants_data)

    index = pd.Series(["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"], name = "餐厅")
    df.index = index
    col_1 = ['latitude', 'longitude']




    st.header('地图')
    st.map(df[col_1])

    st.header('餐厅评分')
    st.bar_chart(df['评分'])

    st.header('不同类型餐厅价格')
    st.line_chart(df['人均消费(元)'])

    place = {
        '星艺会尝不忘': [120,125,251, 252, 151, 152, 152, 125, 123, 121,142,125],
        "高峰柠檬鸭": [111,125,121, 132, 151, 152, 152, 125, 123, 121,152,125],
        "复记老友粉": [117,125,231, 212, 151, 121, 112, 125, 123, 121,142,128],
        "好友缘": [122,125,251, 252, 151, 152, 152, 125, 123, 121,131,125],
        "西冷牛排店": [139,125,251, 252, 151, 125, 142, 125, 123, 121,142,129],
        
    }

    st.header('各餐厅全年价格走势')
    df2 = pd.DataFrame(place)
    index = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12], name = '月份')
    df2.index = index
    st.line_chart(df2)

with tab3:
    st.header("这是第三个选项卡")
    st.markdown("#### 第三个选项卡的内容")
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

with tab4:
    st.header("这是第三个选项卡")
    st.markdown("#### 第三个选项卡的内容")
    from datetime import datetime

    st.set_page_config(
        page_title="个人简历生成器",
        page_icon="📝",
        layout="wide"
    )

    st.title("📝 个人简历生成器")
    st.markdown("> 使用 streamlit 创建您的个性化简历")
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("个人信息表单")

        name = st.text_input("👤 姓名")
        position = st.text_input("🎯 职位")
        phone = st.text_input("📞 电话")
        email = st.text_input("✉️ 邮箱")
        birth_date = st.date_input("🎂 出生日期", min_value=datetime(1970, 1, 1))

        gender_options = ("男", "女", "其他")
        gender = st.radio("ጾ 性别", gender_options, horizontal=True)
        
        education_options = ["小学", "初中", "高中", "大专", "本科", "硕士", "博士"]
        education = st.selectbox("🎓 学历", options=education_options)
        
        language_options = ["英语四级", "英语六级", "专八", "日语N1", "德语B2", "无"]
        language_ability = st.selectbox("🌐 语言能力", options=language_options)
        
        skill_options = ["Python", "Streamlit", "Pandas", "数据分析", "机器学习", "深度学习", "SQL", "Git", "Docker", "挖矿", "盗窃"]
        skills = st.multiselect("🛠️ 技能 (可多选)", options=skill_options)
        
        experience = st.slider("💼 工作经验 (年)", 0, 30, 0)
        salary_range = st.slider("💰 期望薪资范围 (元)", 5000, 50000, (10000, 20000), 1000)

        profile_placeholder = "请简要介绍您的专业背景、职业目标和个人特点..."
        profile = st.text_area("📝 个人简介", height=200, placeholder=profile_placeholder)

        contact_time_options = ["09:00 - 12:00", "14:00 - 18:00", "19:00 - 21:00", "全天均可"]
        best_contact_time = st.selectbox("⏰ 最佳联系时间", options=contact_time_options)

        uploaded_photo = st.file_uploader("🖼️ 上传个人照片", type=['png', 'jpg', 'jpeg'])


    with col2:
        st.subheader("简历实时预览")
        st.divider()

        if uploaded_photo:
            st.image(uploaded_photo, width=200, caption="个人照片")

        st.markdown(f"## {name or '您的姓名'}")
        st.markdown(f"### {position or '期望职位'}")
        st.divider()

        preview_col1, preview_col2 = st.columns(2)

        with preview_col1:
            st.markdown(f"**电话:** {phone or '未填写'}")
            st.markdown(f"**邮箱:** {email or '未填写'}")
            st.markdown(f"**出生日期:** {birth_date.strftime('%Y/%m/%d')}")
            st.markdown(f"**最佳联系时间:** {best_contact_time}")

        with preview_col2:
            st.markdown(f"**性别:** {gender}")
            st.markdown(f"**学历:** {education}")
            st.markdown(f"**工作经验:** {experience} 年")
            st.markdown(f"**期望薪资:** {salary_range[0]} - {salary_range[1]} 元")
            st.markdown(f"**语言能力:** {language_ability}")
            
        st.divider()

        st.markdown("### 个人简介")
        if not profile or profile == profile_placeholder:
            st.warning("这个人很神秘, 没有留下任何介绍...")
        else:
            st.markdown(profile)
        
        st.divider()

        st.markdown("### 专业技能")
        if skills:
            cols = st.columns(3)
            for i, skill in enumerate(skills):
                with cols[i % 3]:
                    st.button(skill, use_container_width=True)
        else:
            st.info("暂未填写技能。")
            
with tab5:
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
            
with tab6:
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