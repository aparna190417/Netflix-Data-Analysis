# 🎬 Netflix Data Analysis & Dashboard

A complete end-to-end **data analysis and visualization project** exploring Netflix Movies and TV Shows using **Python (EDA)** and **Power BI (Dashboarding)**.

This project uncovers insights about content trends, genres, countries, ratings, and movie durations to understand Netflix’s content strategy.

---

## 📌 Project Overview

Netflix has thousands of titles across different countries, genres, and audience ratings.  
This project analyzes the dataset to answer questions like:

- Does Netflix have more Movies or TV Shows?
- How has content production changed over time?
- Which countries produce the most Netflix content?
- What are the most popular genres?
- What type of audience does Netflix mostly target?

---

## 🧹 Data Cleaning

The dataset required preprocessing before analysis:

- Removed duplicate records  
- Filled missing values in:
  - `director` → *Not Available*
  - `country` → *Unknown*
  - `rating` → *Not Rated*
- Converted `date_added` to datetime format
- Extracted `year_added` for time-based analysis
- Split `duration` into:
  - **duration_value** (numeric)
  - **duration_unit** (minutes / seasons)

---

## 📊 Exploratory Data Analysis (Python)

Performed using **Pandas, Matplotlib, and Seaborn**

### Key Visualizations:

✔ Movies vs TV Shows distribution  
✔ Content release trend over the years  
✔ Top 10 content-producing countries  
✔ Rating distribution  
✔ Top genres on Netflix  
✔ Movie duration analysis  
✔ India Movies vs TV Shows comparison  

All plots are saved in the **`images/`** folder.

---

## 📈 Power BI Dashboard

An interactive dashboard was built to present business-level insights visually.

### Dashboard Highlights:
- 🎬 Content Type | Movies dominate, but TV Shows drive engagement |
- 📅 Release Trend | Rapid growth after 2015 |
- 🌍 Top Countries | USA and India lead content production |
- 🎭 Top Genres | Drama and International content are most common |
- ⭐ Ratings | Majority content is TV-MA and TV-14 |

📁 Dashboard file: `powerbi_dashboard/Netflix_Dashboard.pbix`

## 📊 Powerbi Dashboard preview

![PowerBi Dashboard](powerbi_dashboard/Netflix-dashboard.png)

---

## 🌐 Python Interactive Dashboard (Streamlit)

An interactive Netflix analytics dashboard built using Streamlit with dynamic filtering and visual storytelling.

### Features
- Animated KPI counters
- Filters for Type, Country, Rating & Genre
- Professional donut & trend charts
- Download filtered dataset

### Run the Dashboard
streamlit run app.py

## 🖥️ Streamlit Dashboard Preview

![Python Dashboard](images/python_dashboard.png)

---

## 🧠 Key Insights

- Netflix hosts **more Movies than TV Shows**
- Content production **increased sharply after 2015**
- **United States and India** are the top contributors
- Netflix focuses heavily on **mature and teen audiences**
- **Drama** is the most dominant genre
- Most movies follow **standard feature-length duration**

---

## 🗂 Project Structure

Netflix-Data-Analysis/
│
├── data/
│ └── netflix1.csv
│
├── notebook/
│ └── Netflix_Analysis.ipynb
│
├── images/
│ ├── 01_movies_vs_tvshows.png
│ ├── 02_release_trend.png
│ ├── 03_top_countries.png
│ ├── 04_ratings_distribution.png
│ ├── 05_top_genres.png
│ ├── 06_movie_duration.png
│ ├── 07_movies_tv_trend.png
│ └── 08_india_movies_vs_tvshows.png
│
├── powerbi_dashboard/
│ ├── Netflix_Dashboard.pbix
│ └── Netflix-dashboard.png
│
└── requirements.txt


---

## ⚙️ Tools & Technologies

| Skill | Proof in Repo |
|------|----------------|
| Python EDA | Jupyter Notebook |
| Data Cleaning | Notebook Code |
| Data Visualization | Python + Seaborn |
| BI Dashboard | Power BI file |
| Web App Dashboard | Streamlit app.py |
| Documentation | Professional README |

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

git clone https://github.com/your-username/Netflix-Data-Analysis.git
cd Netflix-Data-Analysis

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run the Jupyter Notebook
jupyter notebook


Open Netflix_Analysis.ipynb to see full analysis.

### 4️⃣ Open Power BI Dashboard

Open Netflix_Dashboard.pbix using Power BI Desktop.

### 📷 Dashboard Preview

Add your dashboard screenshot here

### 🎯 Project Outcome

This project demonstrates:

- Real-world data cleaning
- Exploratory data analysis
- Insight generation
- Business storytelling through dashboards
- Combining Python + Power BI skills

## 👩‍💻 Author

**Aparna Patel**

