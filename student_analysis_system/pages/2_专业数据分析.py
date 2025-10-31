# pages/2_专业数据分析.py

import streamlit as st
import pandas as pd
import plotly.express as px

# 设置页面配置
st.set_page_config(
    page_title="专业数据分析",
    page_icon="📊",
    layout="wide"
)

st.title("📊 专业数据分析")

# --- 数据加载与缓存 ---
@st.cache_data # 使用缓存来避免每次刷新都重新加载数据
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"错误：找不到数据文件 {file_path}。请确保文件已上传并路径正确。")
        return None

df = load_data('student_data_adjusted_rounded.csv')

if df is not None:
    # --- 1. 各专业整体数据概览 ---
    st.header("1. 各专业学习指标对比")
    st.write("下表展示了各个专业在每周平均学习时长、期中和期末平均分上的表现。")

    # 按专业分组计算平均值
    major_summary = df.groupby('专业').agg({
        '每周学习时长（小时）': 'mean',
        '期中考试分数': 'mean',
        '期末考试分数': 'mean'
    }).reset_index()

    # 使用 st.dataframe 展示表格，并设置格式
    st.dataframe(
        major_summary.style
        .format({
            '每周学习时长（小时）': '{:.2f} 小时',
            '期中考试分数': '{:.2f} 分',
            '期末考试分数': '{:.2f} 分'
        })
        .highlight_max(axis=0, subset=['每周学习时长（小时）', '期中考试分数', '期末考试分数'], color='lightgreen'),
        use_container_width=True
    )

    st.markdown("---")

    # --- 2. 各专业男女性别比例 ---
    st.header("2. 各专业男女性别比例")
    col1, col2 = st.columns([2, 1]) # 让图表占2/3，数据表占1/3

    with col1:
        gender_ratio = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
        fig_gender = px.bar(
            gender_ratio,
            barmode='group',
            title='各专业男女性别数量对比',
            labels={'value': '学生人数', '专业': '专业', '性别': '性别'}
        )
        st.plotly_chart(fig_gender, use_container_width=True)

    with col2:
        st.write("**性别比例数据**")
        st.dataframe(gender_ratio, use_container_width=True)

    st.markdown("---")

    # --- 3. 各专业期中与期末成绩对比 ---
    st.header("3. 各专业学习指标对比")
    col1, col2 = st.columns([2, 1])

    with col1:
        exam_scores = major_summary[['专业', '期中考试分数', '期末考试分数']]
        # 为了使用折线图，需要将数据从宽格式转换为长格式
        exam_scores_long = exam_scores.melt(id_vars='专业', var_name='考试类型', value_name='平均分')

        fig_scores = px.line(
            exam_scores_long,
            x='专业',
            y='平均分',
            color='考试类型',
            markers=True,
            title='各专业期中与期末平均分对比',
            labels={'平均分': '平均分数', '专业': '专业'}
        )
        fig_scores.update_traces(line=dict(width=3))
        st.plotly_chart(fig_scores, use_container_width=True)

    with col2:
        st.write("**详细数据**")
        st.dataframe(
            exam_scores.set_index('专业').style.format('{:.2f}'),
            use_container_width=True
        )


    st.markdown("---")

    # --- 4. 各专业出勤率分析 ---
    st.header("4. 各专业出勤率分析")
    col1, col2 = st.columns([2, 1])

    with col1:
        attendance = df.groupby('专业')['上课出勤率'].mean().reset_index().sort_values(by='上课出勤率', ascending=False)
        fig_attendance = px.bar(
            attendance,
            x='专业',
            y='上课出勤率',
            color='专业',
            title='各专业平均上课出勤率',
            labels={'上课出勤率': '平均出勤率 (%)'}
        )
        fig_attendance.update_layout(yaxis_ticksuffix='%')
        st.plotly_chart(fig_attendance, use_container_width=True)

    with col2:
        st.write("**出勤率排名**")
        st.dataframe(
            attendance.set_index('专业').style.format('{:.2f}%'),
            use_container_width=True
        )

    st.markdown("---")

    # --- 5. 大数据管理专业专项分析 ---
    st.header("5. 🔍 大数据管理专业专项分析")

    # 筛选出大数据专业的数据
    big_data_df = df[df['专业'] == '大数据管理']

    if not big_data_df.empty:
        # 计算指标
        avg_attendance_bd = big_data_df['上课出勤率'].mean()
        avg_final_score_bd = big_data_df['期末考试分数'].mean()
        avg_study_hours_bd = big_data_df['每周学习时长（小时）'].mean()

        # 使用 st.metric 创建指标卡
        col1, col2, col3 = st.columns(3)
        col1.metric(label="平均上课出勤率", value=f"{avg_attendance_bd:.2f}%", delta="对比专业平均")
        col2.metric(label="期末平均分", value=f"{avg_final_score_bd:.2f}分", delta="对比专业平均")
        col3.metric(label="每周平均学习", value=f"{avg_study_hours_bd:.2f}小时", delta="对比专业平均")

        # 可视化展示
        col1_chart, col2_chart = st.columns(2)
        with col1_chart:
            st.write("**期末成绩分数分布 (箱线图)**")
            fig_box = px.box(
                big_data_df,
                y='期末考试分数',
                title='大数据管理专业期末成绩分布',
                points='all' # 显示所有数据点
            )
            st.plotly_chart(fig_box, use_container_width=True)

        with col2_chart:
            st.write("**学习时长与期末成绩关系 (散点图)**")
            fig_scatter = px.scatter(
                big_data_df,
                x='每周学习时长（小时）',
                y='期末考试分数',
                title='学习时长与期末成绩关系',
                trendline='ols' # 添加一条回归线
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

    else:
        st.warning("数据中未找到'大数据管理'专业。")