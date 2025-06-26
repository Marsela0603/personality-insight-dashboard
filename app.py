import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Personality Insight Dashboard", page_icon="🧠", layout="wide")

# Load dataset dari file CSV
df = pd.read_csv("personality_synthetic_dataset.csv")

# Sidebar navigasi
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "📎 About Dataset",
    "📊 Personality Distribution",
    "📈 Trait Comparison",
    "📉 Trait Boxplot",
    "🔍 Correlation Analysis",
    "🔎 Scatter Plot"
])

# Halaman Home
if menu == "🏠 Home":
    # Menampilkan judul dan deskripsi beranda
    st.title("🧠 Personality Insight Dashboard")
    st.markdown("""
    Welcome to the **Personality Insight Dashboard**!

    This synthetic dataset simulates three main personality types:
    **Introvert**, **Extrovert**, and **Ambivert**, based on behavioral and psychological traits.

    Discover how each personality type exhibits unique patterns through interactive visualizations.
    """)
    
    # Informasi kelompok pembuat
    st.markdown("---")
    st.markdown("#### 👥 Created by Group 9 - Data Visualization Project")
    st.markdown("""
    - Marsela (0110223120)  
    - Rifa Fradita Safara (0110223118)  
    - Sri Lusiana (0110223129)
    """)

# Halaman Tentang Dataset
elif menu == "📎 About Dataset":
    # Menampilkan penjelasan tentang isi dataset
    st.header("📎 About the Dataset")
    st.markdown("""
    This dataset contains **20,000 entries** and **30 columns**:
    
    - **Target Column**: `personality_type` (Introvert, Extrovert, Ambivert)
    - **30 Feature Columns**: Various personality traits such as:
        - `social_energy`, `talkativeness`, `empathy`, `creativity`, `organization`, etc.
    
    The dataset is ideal for:
    - Personality classification
    - Clustering similar personality profiles
    - Behavioral analysis
    - Feature importance studies
    """)

# Halaman Distribusi Kepribadian
elif menu == "📊 Personality Distribution":
    # Menampilkan pie chart untuk distribusi tipe kepribadian
    st.header("📊 Personality Type Distribution")
    fig = px.pie(df, names='personality_type', title='Distribution of Personality Types')
    st.plotly_chart(fig)

# Halaman Perbandingan Trait
elif menu == "📈 Trait Comparison":
    # Menampilkan bar chart rata-rata trait berdasarkan tipe kepribadian
    st.header("📈 Average Trait by Personality Type")
    selected_trait = st.selectbox("Select a Trait:", df.columns[1:-1])
    avg_df = df.groupby("personality_type")[selected_trait].mean().reset_index()
    fig = px.bar(avg_df, x='personality_type', y=selected_trait, color='personality_type', title=f"Average {selected_trait} by Personality Type")
    st.plotly_chart(fig)

# Halaman Boxplot Trait
elif menu == "📉 Trait Boxplot":
    # Menampilkan boxplot distribusi trait untuk masing-masing tipe kepribadian
    st.header("📉 Trait Distribution by Personality Type (Boxplot)")
    selected_trait = st.selectbox("Select a Trait to Explore:", df.columns[1:-1], key="boxplot_trait")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x='personality_type', y=selected_trait, data=df, palette='Set2')
    plt.title(f'{selected_trait} Distribution by Personality Type')
    st.pyplot(fig)

# Halaman Korelasi
elif menu == "🔍 Correlation Analysis":
    # Menampilkan heatmap korelasi antar trait numerik
    st.header("🔍 Correlation Heatmap")
    numeric_df = df.drop("personality_type", axis=1)
    corr = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, cmap='coolwarm', annot=False)
    st.pyplot(fig)

# Halaman Scatter Plot
elif menu == "🔎 Scatter Plot":
    # Menampilkan scatter plot dua trait berdasarkan tipe kepribadian
    st.header("🔎 Scatter Plot of Two Traits")
    st.markdown("Select two traits below to see their relationship and how they are spread across personality types.")

    col1, col2 = st.columns(2)
    with col1:
        x_trait = st.selectbox("X-axis Trait", df.columns[1:-1], key="scatter_x")
    with col2:
        y_trait = st.selectbox("Y-axis Trait", df.columns[1:-1], key="scatter_y")

    fig = px.scatter(
        df,
        x=x_trait,
        y=y_trait,
        color="personality_type",
        title=f"{x_trait} vs {y_trait} by Personality Type",
        opacity=0.6,
        symbol="personality_type"
    )
    st.plotly_chart(fig)
