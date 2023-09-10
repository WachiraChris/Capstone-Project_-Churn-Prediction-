```markdown
# 🚀 Telco Customer Churn Prediction 🚀

## Table of Contents

- [Project Overview](#project-overview)
- [Summary](#summary)
- [Getting Started](#getting-started)
- [Data](#data)
- [Contact](#contact)

## Project Overview

The telecommunications industry is facing a significant challenge with the rapid loss of customers. To tackle this issue, we are employing machine learning and data analysis to predict customer churn. This approach enables us to proactively retain customers by identifying potential churners and taking targeted actions to retain them.

Our project utilizes various data sources, including customer history, usage patterns, and demographics. We leverage this data to train machine learning models capable of predicting customer churn likelihood. Once these models are trained, we deploy them to identify potential churners. Subsequently, these customers are contacted and offered special incentives to encourage them to remain with the company.

## Project Objective

Our primary project objective is to develop highly accurate machine learning models for predicting customer churn. We achieve this by analyzing historical customer data to uncover patterns and factors contributing to churn. The insights gained will enable the telecom company to devise strategies for reducing churn rates. Our approach encompasses a range of machine learning algorithms, such as logistic regression, decision trees, and random forests. We also employ feature engineering techniques to enhance model accuracy. This project is expected to provide substantial value to the telecom company by helping identify at-risk customers and taking preventative measures, resulting in cost savings and improved customer satisfaction.

## Summary

| Code     | Name                          | Published Article | Deployed App    |
| -------- | ----------------------------- | ----------------- | --------------- |
| Capstone | Telco Customer Churn Prediction | Medium Article    | Streamlit App   |

## Project Setup

To set up the project environment, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/slickHnaa/Telco-Customer-Churn.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a virtual environment (Windows):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   Create a virtual environment (Linux & MacOS):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

You can copy and paste each command above into your terminal to easily set up the project environment.

## Data

The data used in this project consists of a diverse collection of sepsis cases obtained from Zindi.

### Data Fields

| Column Name   | Data Features | Description                                      |
| ------------- | ------------- | ------------------------------------------------ |
| REGION        | Categorical   | The location of each client                     |
| TENURE        | Numeric       | Duration with the network                        |
| MONTANT       | Numeric       | Top-Up Amount                                    |
| FREQUENCE_RECH| Numeric       | The number of times a customer refilled         |
| REVENUE       | Numeric       | Monthly income of each client                   |
| ARPU_SEGMENT  | Numeric       | Income over 90 days divided by 3                |
| FREQUENCE     | Numeric       | Number of times the client has made an income   |
| DATA_VOLUME   | Numeric       | Number of connections                            |
| ON_NET        | Numeric       | Inter Expresso call                              |
| ORANGE        | Numeric       | Calls to Orange                                  |
| TIGO          | Numeric       | Calls to Tigo                                    |
| ZONE1         | Numeric       | Calls to Zone1                                   |
| ZONE2         | Numeric       | Calls to Zone2                                   |
| MRG           | Categorical   | A client who is going                            |
| REGULARITY    | Numeric       | Number of times the client is active for 90 days|
| TOP_PACK      | Categorical   | The most active packs                            |
| FREQ_TOP_PACK | Numeric       | Number of times the client has activated the top pack packages |
| CHURN         | Binary        | Target variable to predict - Churn (Positive: customer will churn, Negative: customer will not churn) |

## Contributing Authors

- **Christopher Wachira**
- **Tyokase Orseer**
- **Henry Nii Ayitey-Adjin**
- **UWIRINGIYIMANA Eliere**
```
