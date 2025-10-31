# 1_项目介绍.py

import streamlit as st
from PIL import Image

# 设置页面配置，这应该是 Streamlit 命令中的第一个
st.set_page_config(
    page_title="学生成绩分析与预测系统 | 项目介绍",
    page_icon="📚",
    layout="wide"
)

# --- 页面内容 ---

st.title("👨‍🎓 学生成绩分析与预测系统")

st.markdown("---")

# 项目概述
st.header("■ 项目概述")
st.write(
    """
    本项目是一个基于 Streamlit 的学生成绩分析平台。通过交互式的可视化技术，帮助教育工作者深入了解学生群体的学习行为与表现。
    此外，平台集成了机器学习模型，能根据学生的各项指标预测其期末成绩，为及早发现学习困难的学生并提供针对性辅导提供了数据支持。
    """
)

# 主要特点
st.subheader("主要特点:")
st.markdown(
    """
    - **数据可视化**: 多维度、交互式地展示学生数据。
    - **专业分析**: 深入对比分析不同专业的学生表现。
    - **智能预测**: 基于学生的学习行为进行期末成绩预测。
    - **友好交互**: 简洁明了的用户界面，操作直观便捷。
    """
)

# 截图展示
st.image('1.png', caption='系统主界面概览', use_column_width=True)

st.markdown("---")

# 项目目标
st.header("🎯 项目目标")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("● 目标一")
    st.info("分析影响学生成绩的关键因素")
    st.markdown("- 识别关键学业指标")
    st.markdown("- 探索学习行为与成绩关联")
    st.markdown("- 提出教学改进建议")

with col2:
    st.subheader("● 目标二")
    st.success("可视化展示学业表现")
    st.markdown("- 专业横向对比")
    st.markdown("- 成绩分布情况")
    st.markdown("- 学时与成绩关系")

with col3:
    st.subheader("● 目标三")
    st.warning("构建预测模型")
    st.markdown("- 预测学生期末成绩")
    st.markdown("- 识别潜在风险学生")
    st.markdown("- 辅助个性化教育")

st.markdown("---")

# 技术架构
st.header("🛠️ 技术架构")
st.write("本项目主要采用以下技术栈构建：")

tech_data = {
    "前端框架": ["Streamlit"],
    "数据处理": ["Pandas", "NumPy"],
    "可视化": ["Plotly", "Matplotlib"],
    "机器学习": ["Scikit-learn"]
}
st.table(tech_data)

st.sidebar.success("请在上方选择一个页面。")