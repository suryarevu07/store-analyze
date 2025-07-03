# 🛒 Retail Sales Forecasting and Insights

This project is a **Retail Sales Forecasting and Recommendation System** built using **Flask**, **HTML**, and **CSS**. It predicts department-wide sales for the following year, models the impact of markdowns during holiday weeks, and provides actionable business recommendations to maximize revenue.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Insights & Recommendations](#insights--recommendations)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 📖 Overview

Forecasting retail sales is crucial for inventory planning, marketing, and business strategy. This project uses historical sales, markdowns, and holiday data to build a predictive system for store-department-level sales forecasting.

---

## ❓ Problem Statement

> **The Task:**
- Predict department-wide weekly sales for each store for the following year.
- Model the effects of **markdown events** on **holiday weeks**.
- Provide prioritized **recommendations** based on the insights drawn.

---

## 🎯 Objectives

- Analyze historical sales, markdowns, holidays, and economic indicators.
- Build a robust regression model to forecast future sales.
- Visualize performance metrics and business-impact insights.
- Deploy an interactive web app for real-time predictions.

---

## ⚙️ Tech Stack

| Component     | Technology Used         |
|---------------|--------------------------|
| Backend       | Python, Flask            |
| Frontend      | HTML5, CSS3              |
| Data Handling | pandas, NumPy            |
| Modeling      | scikit-learn (RandomForest, DecisionTree) |
| Visualization | Chart.js, matplotlib     |
| Deployment    | Flask local server / Render |

---

## ✨ Features

- 🔮 Predict sales by store, department, week, and holiday status
- 📈 Model markdown impact on sales
- 📊 Show evaluation metrics (R², RMSE, MAE)
- ✅ Upload data, preprocess, and auto-forecast
- 📂 Export predictions to CSV
- 💡 Actionable business insights and strategy suggestions

---

## 🏗️ Project Structure

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/retail-sales-forecast.git
cd retail-sales-forecast

