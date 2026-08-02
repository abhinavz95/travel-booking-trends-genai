# ✈️ Travel Booking Trends + GenAI Insights

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-EDA-150458)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A **data analysis project** exploring travel and hotel booking trends (MakeMyTrip-style datasets), enhanced with a **Generative AI layer** that produces natural-language recommendations and insight summaries for travelers and business stakeholders.

## 📌 Project Goals
- Perform exploratory data analysis on flight/hotel booking data (pricing, seasonality, cancellations, demand)
- Visualize booking patterns across cities, months, and customer segments
- Build a Gen-AI assistant that answers natural-language questions about the dataset and summarizes key trends
- Demonstrate a complete, reproducible data analysis workflow for portfolio/application purposes

## 🗂️ Dataset
Public travel/flight/hotel booking dataset (route, price, travel dates, booking lead time, customer ratings). Source noted in `/data/README.md` (Kaggle travel booking datasets).

## 🧰 Tech Stack
| Layer | Tools |
|---|---|
| Data wrangling | Python, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Gen-AI Insights | OpenAI API / Gemini API, LangChain |
| Notebook | Jupyter |
| Version control | Git & GitHub |

## 📊 Analysis Covered
1. Data cleaning and preprocessing of booking records
2. Price trend analysis by season, route, and lead time
3. Cancellation rate and customer segment analysis
4. Demand hotspots by destination city
5. Correlation between booking lead time and price
6. **Gen-AI Insight Generator**: summarizes EDA findings into a natural-language report and answers ad-hoc questions about the data

## 🖼️ Sample Output
> Visualizations and the Gen-AI generated summary report are saved to the `/outputs` folder after running the notebooks.

## 🚀 How to Run
```bash
git clone https://github.com/abhinavz95/travel-booking-trends-genai.git
cd travel-booking-trends-genai
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

## 📁 Repository Structure
```
travel-booking-trends-genai/
├── data/              # raw & processed datasets
├── notebooks/         # Jupyter notebooks for EDA
├── src/               # reusable python scripts
├── outputs/           # generated charts & GenAI reports
├── requirements.txt
└── README.md
```

## 🔮 Future Improvements
- Deploy an interactive Streamlit dashboard
- Add price-prediction ML model
- Expand Gen-AI assistant to support multi-turn Q&A over the dataset

## 👤 Author
Built by **Abhinav** as part of a data analysis portfolio for job & Master's program applications.

## 📄 License
This project is released under the MIT License.
