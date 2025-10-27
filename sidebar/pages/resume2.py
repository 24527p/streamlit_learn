import streamlit as st
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
