# 🎬 Netflix Data Analysis (EDA + Power BI Dashboard)

This project includes a **Python-based Exploratory Data Analysis (EDA)** and a **Power BI interactive dashboard** on the Netflix Movies & TV Shows dataset.  
The goal is today's Netflix content patterns like **Movies vs TV Shows distribution**, **country-wise content**, **popular genres**, **ratings**, and **year-wise trends** using clean visualizations and a premium dark-themed dashboard.

---

##  What I did in this project

### Python EDA (Jupyter Notebook)
- Loaded and explored the dataset
- Cleaned missing values and formatted important columns (especially `date_added`)
- Created useful features like `year_added`
- Performed EDA and visualization using Matplotlib/Seaborn
- Wrote key insights based on trends (countries, genres, ratings, duration)

### Power BI Dashboard (Interactive)
- Built a **Netflix Content Dashboard** with modern dark UI (HR reference style)
- Created KPI cards for quick insights
- Developed DAX measures for extracting top rating/genre
- Added slicers for filtering by **Type** and **Country**
- Designed the dashboard with a clean layout and Netflix branding

---

## Dataset

The dataset is a CSV file containing Netflix titles with metadata such as:  
`type`, `title`, `director`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`.

---

## Tools used

### Python Tools
- Python
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib, Seaborn

### Power BI Tools
- Power BI Desktop
- DAX (Measures & Calculated Columns)
- Dashboard UI/UX Design (Dark Theme)

---

## Main graphs included (Python)

- Movies vs TV Shows distribution  
- Titles released over the years  
- Top 10 content producing countries  
- Ratings distribution  
- Top 10 genres on Netflix  
- Movie duration distribution  

(Charts are saved inside the `images/` folder.)

---

## Key takeaways (Python EDA)

- Netflix has more Movies than TV Shows in this dataset.
- Content releases increased heavily after 2015.
- USA and India contribute a major portion of Netflix content.
- TV-MA and TV-14 are the most common ratings.
- Genres like International Movies, Dramas, and Comedies appear frequently.
- Most Netflix movies fall between 80–120 minutes duration.

---

## Challenges I faced

- Missing values in columns like `director`, `country`, and `rating`
- Converting `date_added` into datetime format for time-based analysis
- The genre column contains multiple values, so splitting + exploding was required
- Duration column had mixed formats (minutes for movies and seasons for TV shows)

---

##  Project Structure

Netflix-Data-Analysis/
│── Powerbi_Dashboard/
│── notebook/
│── data/
│── images/
│── requirements.txt
│── README.md

---

# Power BI Dashboard

## 📸 Dashboard Preview
![Power BI Dashboard](Powerbi_Dashboard/netflix_dashboard.png)

---

## 📌 Power BI File
- `Powerbi_Dashboard/Netflix_Dashboard.pbix`

---

## Author

**Aparna Patel**
  




