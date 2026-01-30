import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

st.set_page_config(page_title="Netflix Analytics Dashboard", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
body {background-color: #0e1117;}
h1, h2, h3 {color: #E50914;}

.kpi-card {
    background: linear-gradient(135deg, #141E30, #243B55);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
}
.kpi-title {font-size: 16px; color: #AAAAAA;}
.kpi-value {font-size: 32px; font-weight: bold; color: #FFFFFF;}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
df = pd.read_csv("data/netflix1.csv")

df.drop_duplicates(inplace=True)
df['director'].fillna('Not Available', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['duration_value'] = df['duration'].str.extract('(\d+)').astype(float)

# ---------- SIDEBAR FILTERS ----------
st.sidebar.title("🎛 Filters")

type_filter = st.sidebar.multiselect("Content Type", df['type'].unique(), default=df['type'].unique())
country_filter = st.sidebar.multiselect("Country", df['country'].unique(), default=df['country'].unique())
rating_filter = st.sidebar.multiselect("Rating", df['rating'].unique(), default=df['rating'].unique())

# Genre extraction
all_genres = sorted(set(g.strip() for sublist in df['listed_in'].dropna().str.split(',') for g in sublist))
genre_filter = st.sidebar.multiselect("Genre", all_genres, default=all_genres)

filtered_df = df[
    (df['type'].isin(type_filter)) &
    (df['country'].isin(country_filter)) &
    (df['rating'].isin(rating_filter))
]

filtered_df = filtered_df[
    filtered_df['listed_in'].apply(lambda x: any(g in str(x) for g in genre_filter))
]

# ---------- TITLE ----------
st.title("🎬 Netflix Analytics Dashboard")

# ---------- ANIMATED KPI FUNCTION ----------
def animated_kpi(title, value):
    placeholder = st.empty()
    for i in range(0, value+1, max(1, value//30)):
        placeholder.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-title'>{title}</div>
            <div class='kpi-value'>{i}</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.01)
    placeholder.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-title'>{title}</div>
            <div class='kpi-value'>{value}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------- KPI ROW ----------
k1, k2, k3, k4 = st.columns(4)

with k1:
    animated_kpi("Total Titles", len(filtered_df))
with k2:
    animated_kpi("Movies", len(filtered_df[filtered_df['type']=="Movie"]))
with k3:
    animated_kpi("TV Shows", len(filtered_df[filtered_df['type']=="TV Show"]))
with k4:
    animated_kpi("Countries", filtered_df['country'].nunique())

st.markdown("---")

# ---------- CHARTS ROW 1 ----------
c1, c2 = st.columns(2)

with c1:
    st.subheader("Movies vs TV Shows Distribution")
    counts = filtered_df['type'].value_counts()
    colors = ["#70CDDE", "#F488BE"]

    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=counts.index, autopct='%1.1f%%',
            startangle=90, colors=colors,
            wedgeprops={'width':0.4, 'edgecolor':'white'})
    ax1.text(0, 0, "Content\nSplit", ha='center', va='center', fontsize=12, fontweight='bold')
    st.pyplot(fig1)

with c2:
    st.subheader("Content Release Trend")
    trend = filtered_df.groupby(['release_year', 'type']).size().reset_index(name='count')

    fig2, ax2 = plt.subplots()
    sns.lineplot(data=trend, x='release_year', y='count', hue='type',
                 palette=["#69F39B", "#00BFFF"], linewidth=2.5, ax=ax2)
    ax2.set_xlabel("Release Year")
    ax2.set_ylabel("Number of Titles")
    ax2.grid(alpha=0.2)
    st.pyplot(fig2)

st.markdown("---")

# ---------- CHARTS ROW 2 ----------
c3, c4 = st.columns(2)

with c3:
    st.subheader("Top Content Producing Countries")
    top_countries = filtered_df['country'].value_counts().head(10)

    fig3, ax3 = plt.subplots()
    sns.barplot(x=top_countries.values, y=top_countries.index, palette="Reds_r", ax=ax3)
    st.pyplot(fig3)

with c4:
    st.subheader("Ratings Distribution")
    fig4, ax4 = plt.subplots()
    sns.countplot(data=filtered_df, y='rating',
                  order=filtered_df['rating'].value_counts().index,
                  palette="coolwarm", ax=ax4)
    st.pyplot(fig4)

st.markdown("---")

# ---------- MOVIE DURATION ----------
st.subheader("Movie Duration Distribution")
movies = filtered_df[filtered_df['type']=="Movie"]

fig5, ax5 = plt.subplots()
sns.histplot(movies['duration_value'], bins=20, color="#4292c6", ax=ax5)
ax5.set_xlabel("Duration (minutes)")
st.pyplot(fig5)

st.markdown("---")

# ---------- DOWNLOAD BUTTON ----------
st.markdown("### 📥 Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download CSV",
    data=csv,
    file_name='filtered_netflix_data.csv',
    mime='text/csv',)