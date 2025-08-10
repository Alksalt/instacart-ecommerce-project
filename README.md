# Instacart Grocery Analysis: Uncovering Customer Behavior

This project performs an in-depth exploratory data analysis (EDA) on over 3 million grocery orders from the Instacart dataset. The goal is to uncover actionable insights into customer purchasing habits, product popularity, and temporal trends to inform business strategy. The analysis covers data cleaning, feature engineering, and a market basket analysis to identify which products are frequently purchased together.

---
## Key Findings & Visuals

A few key insights from the analysis include:

1.  **Peak Ordering Times:** Shopping is heavily concentrated on weekends (Days 0 and 6), particularly in the early afternoon between 1 PM and 4 PM. This suggests promotions, server capacity, and shopper availability should be scaled up during these peak periods.
    *(Example visual to include from your `visuals` folder)*
    `![Order Heatmap](visuals/orders_heatmap.png)`

2.  **Top Product Categories:** **Produce** and **Dairy & Eggs** are the dominant departments, indicating that customers primarily use the service for fresh groceries and everyday essentials. Bananas are consistently the single most purchased item.
    *(Example visual to include from your `visuals` folder)*
    `![Top Departments](visuals/top_departments.png)`

3.  **Strong Customer Loyalty:** The platform has a very healthy repeat purchase rate of over 96%. Analysis of `days_since_prior_order` reveals clear weekly (7-day) and monthly (30-day) purchasing cycles, which can be leveraged for targeted marketing and subscription-style reminders.

4.  **Actionable Product Associations:** Market basket analysis revealed strong affinities between specific products. For example, there's a high lift between various organic fruits and vegetables, suggesting customers who buy one organic item are very likely to purchase another.
    *Example Rule: {Organic Hass Avocado} -> {Organic Strawberries}*

---
## Repository Structure

The project is organized into a clean, reproducible structure:

├── data/
│   └── (Raw and processed .csv files - not tracked by Git)
├── notebooks/
│   └── eda.ipynb           # Main analysis notebook with visualizations and insights.
├── scripts/
│   └── ingestion_sanitation.py # Python script to clean and prepare raw data.
├── visuals/
│   └── orders_heatmap.png  # Saved, high-quality visualizations from the EDA.
│   └── ...
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

---
## Methodology & Tools

The analysis was conducted in distinct phases, moving from data preparation to insight generation.

1.  **Data Ingestion & Sanitation:** The initial phase involved loading the raw datasets using **pandas**. A dedicated script (`scripts/ingestion_sanitation.py`) was used to optimize data types for memory efficiency, check for null values, and verify data integrity across tables.

2.  **Exploratory Data Analysis (EDA):** In the main notebook (`notebooks/eda.ipynb`), I investigated core business questions related to temporal patterns, product and department performance, and customer behavior metrics like order frequency and reorder rates.

3.  **Advanced Analysis:** A market basket analysis was performed using the **Apriori** algorithm from the **`mlxtend`** library. Due to computational constraints on a local machine, the analysis was focused on the top 500 most frequent products, which was sufficient to uncover strong and significant association rules.

4.  **Tools & Libraries:**
    * **Data Manipulation:** `pandas`, `numpy`
    * **Visualization:** `matplotlib`, `seaborn`, `plotly`
    * **Association Rule Mining:** `mlxtend`

---
## Instructions for Local Execution

To reproduce this analysis on your local machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url>
    cd <repository_name>
    ```

2.  **Set Up a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the Data:**
    The dataset is from the [Instacart Market Basket Analysis competition on Kaggle](https://www.kaggle.com/c/instacart-market-basket-analysis/data). Download the `.csv` files and place them in the `data/` directory.

5.  **Run the Project:**
    * First, run the data cleaning script from your terminal to generate the processed files:
        ```bash
        python scripts/ingestion_sanitation.py
        ```
    * Then, launch Jupyter Notebook or your preferred IDE and open `notebooks/eda.ipynb`. You can now run the cells sequentially to see the full analysis.

---
## Data Source

This project uses the Instacart Online Grocery Shopping Dataset, which contains a sample of over 3 million anonymized grocery orders from more than 200,000 users.

-   **License:** The data is released under the CC0: Public Domain license.
-   **Context:** Online retail (grocery e-commerce).

---
## License

This project is released under the MIT License. See the `LICENSE` file for more details.