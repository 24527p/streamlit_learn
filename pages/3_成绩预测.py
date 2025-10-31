# pages/3_成绩预测.py

import streamlit as st
import pandas as pd
import joblib

# 设置页面配置
st.set_page_config(
    page_title="期末成绩预测",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 期末成绩预测")

# --- 加载模型和编码器 ---
@st.cache_resource # 使用缓存加载，避免重复加载
def load_model_and_encoders():
    try:
        model = joblib.load('../model.joblib')
        le_gender = joblib.load('../gender_encoder.joblib')
        le_major = joblib.load('../major_encoder.joblib')
        return model, le_gender, le_major
    except FileNotFoundError:
        st.error("错误：找不到模型或编码器文件。请先运行 train_model.py 脚本生成这些文件。")
        return None, None, None

model, le_gender, le_major = load_model_and_encoders()

if model and le_gender and le_major:
    # --- 用户输入表单 ---
    st.header("请输入学生信息进行预测")
    
    # 从原始数据中获取专业的唯一列表
    # 这样做可以确保下拉菜单中的选项与训练时一致
    try:
        df = pd.read_csv('../student_data_adjusted_rounded.csv')
        major_options = df['专业'].unique().tolist()
    except FileNotFoundError:
        st.error("无法加载原始数据文件以获取专业列表。")
        major_options = [] # 如果文件不存在，则提供一个空列表

    with st.form("prediction_form"):
        # 将输入框分组
        col1, col2, col3 = st.columns(3)

        with col1:
            student_id = st.text_input("学号", "2023001")
            gender = st.selectbox("性别", le_gender.classes_, index=0)
            major = st.selectbox("专业", major_options, index=0)

        with col2:
            study_hours = st.slider("每周学习时长（小时）", 1, 40, 15)
            attendance_rate = st.slider("上课出勤率 (%)", 0, 100, 95)

        with col3:
            midterm_score = st.slider("期中考试分数", 0, 100, 80)
            assignment_rate = st.slider("作业完成率 (%)", 0, 100, 90)

        # 提交按钮
        submit_button = st.form_submit_button(label='🚀 预测期末成绩')

    # --- 预测逻辑 ---
    if submit_button:
        # 1. 将用户输入转换为 DataFrame
        # LabelEncoder 和模型期望的是数字，所以我们需要转换
        try:
            gender_encoded = le_gender.transform([gender])[0]
            major_encoded = le_major.transform([major])[0]

            input_data = pd.DataFrame({
                '性别': [gender_encoded],
                '专业': [major_encoded],
                '每周学习时长（小时）': [study_hours],
                '上课出勤率': [attendance_rate],
                '期中考试分数': [midterm_score],
                '作业完成率': [assignment_rate]
            })
            
            # 确保列的顺序和训练时一致
            # 特征顺序在 train_model.py 中定义过
            features_order = ['性别', '专业', '每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率']
            input_data = input_data[features_order]

            # 2. 进行预测
            with st.spinner('正在分析数据，请稍候...'):
                prediction = model.predict(input_data)
                predicted_score = prediction[0]

            # 3. 展示预测结果
            st.header("📈 预测结果")
            st.success(f"**预测的期末成绩为: {predicted_score:.2f} 分**")

            # 4. 根据分数显示不同的图片和信息
            passing_score = 60
            if predicted_score >= passing_score:
                st.balloons()
                st.image('../congratulations.jpg', caption='恭喜！预测成绩及格，请继续保持！')
            else:
                st.warning("预测成绩未及格，仍需努力！")
                st.image('../encouragement.jpg', caption='别灰心，调整学习方法，你一定可以的！')
        
        except Exception as e:
            st.error(f"预测过程中发生错误: {e}")
            st.error("请检查输入的数据或模型文件是否正确。")
else:
    st.info("模型正在加载中或加载失败，请稍候或检查文件。")