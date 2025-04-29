
# Dice Jobs Market Analysis 📊

**Project Title:** Breaking Into the Market – A Pre-Grad Deep Dive into Job Trends  
**Author:** Manan Upadhyay  
**Goal:** This project analyzes real-time job data scraped from Dice.com to understand hiring trends, employment types, in-demand roles, skill distributions, and job posting patterns — especially for new grads entering the data/tech job market.

---

## 🧠 Why This Project?
With graduation around the corner, I didn’t want to apply blindly. I scraped and analyzed thousands of job listings to see what’s really happening in the job market. This repo shares everything — the code, the visuals, the insights.

---

## 📁 Repository Structure

```bash
📦dice-job-analysis/
├── 📄 Data-Analysis.ipynb         # Jupyter Notebook with full data processing, analysis, and visualizations
├── 📄 DATA_ANALYTICS_DIC_JOBS_ANALYSIS.pdf  # PDF report summarizing key findings
├── 📁 scraped_files/              # CSV files or raw scraped data used in analysis
├── 📄 README.md                   # This file
```

---

## 📌 Highlights from the Report

- **3,900+ Contract Jobs vs. 800 Full-time Jobs**: Major trend toward contract roles.
- **Top Cities**: Dallas, NY, Austin lead job count. San Jose & SF close behind.
- **In-Demand Roles**: Data Engineer, ML Engineer, Cloud Architect, and Azure Developer top the charts.
- **Internship Hotspots**: San Jose and New York are gold mines for internships.
- **Timing Is Key**: 265% increase in postings in the last 30 days vs. previous month.

---

## 🔧 Technologies Used

- **Web Scraping**: `BeautifulSoup`, `requests`
- **Data Cleaning/Analysis**: `pandas`, `NumPy`
- **Visualization**: `matplotlib`, `seaborn`, `wordcloud`
- **NLP for Skills Extraction**: `spaCy`

---

## 📈 Key Visualizations

- Employment type distribution
- City-wise job counts
- Word cloud of top job titles
- Top companies by location
- Weekly posting trends
- Skills required per job domain

---

## 📋 Report Summary

The [PDF report](./DATA_ANALYTICS_DIC_JOBS_ANALYSIS.pdf) includes detailed insights with graphs and interpretations across:
- Job Types
- Locations
- Time-Based Trends
- Skill Demands
- Company Dominance in Hiring

---

## 🚀 Run It Yourself

1. Clone this repo
2. Open `Data-Analysis.ipynb` in Jupyter or Colab
3. Replace the data path with your own if needed
4. Run all cells for full analysis + visualizations

---

## 💡 What's Next?

- Integrating salary predictions
- Building an interactive dashboard with `Streamlit`
- Comparing trends across multiple job platforms

---

## 📬 Contact

Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/mananupadhyay2000/) for collaboration or feedback.

---

