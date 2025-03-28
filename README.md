# 🛍️ Mall Customer Segmentation & Spending Score Analysis

This project analyzes customer behavior using the Mall_Customers dataset. The focus is on understanding **spending score patterns** across different age groups, income levels, and genders, and clustering customers for targeted strategies.

## 🚀 Technologies Used
- **PySpark**: For distributed data processing
- **VS Code**: Local development
- **Pandas & Matplotlib** (optional): For local plotting
- **scikit-learn**: KMeans clustering
- **Word**: Final report documentation

## 📂 Project Structure

Mall_Customers_Analysis/
│
├── data/
│   └── Mall_Customers.csv              # Raw dataset
│
├── notebooks/
│   └── mall_analysis.ipynb             # Jupyter Notebook with full analysis
│
├── src/
│   ├── __init__.py
│   ├── load_data.py                    # Script to load data using PySpark
│   ├── analyze_spending.py            # Script for spending score analysis
│   └── clustering.py                   # K-Means or other ML analysis
│
├── reports/
│   ├── Analysis_Report.docx            # Word report (final)
│   └── Challenges_Faced.docx           # Problems you encountered
│
├── outputs/
│   ├── charts/                         # All generated charts/images
│   └── cleaned_data.csv                # Any exported or cleaned data
│
├── requirements.txt                    # List of Python + PySpark dependencies
├── README.md                           # Project overview, steps, insights
└── .gitignore                          # Optional, if pushing to GitHub


## 🧠 Analysis Focus
- Spending Score vs. Age
- Spending Score vs. Income
- Gender-based patterns
- Customer clustering using K-Means

## 📈 Deliverables
- Cleaned dataset (optional)
- Visualizations
- Word report on insights & challenges
- Jupyter notebook (.ipynb)

## 📝 Author
**Your Name**  
Intern - Mall Customer Segmentation Project

## 🗃️ Data Source
[Dataset Link](https://drive.google.com/file/d/1k6A8r1cCdt0Ft0mPtvnYckruaTn2XXz0/view?usp=share_link)
