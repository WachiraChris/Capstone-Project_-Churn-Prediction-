🚀Telco Customer Churn Prediction🚀
Table of Contents
Project Overview
Summary
Getting Started
Data
Contact
Project Overview
The telecommunications industry is losing customers at an alarming rate. To address this issue, we are using machine learning and data analysis to predict which customers are most likely to churn. This will allow us to proactively retain customers by identifying potential churners and taking targeted actions to keep them.

The project will use a variety of data sources, including customer history, usage patterns, and demographics. This data will be used to train machine learning models that can predict the likelihood of a customer churning. Once the models are trained, they will be used to identify potential churners. These customers will then be contacted and offered special incentives to stay with the company.

Project Objective
The main goal of this project is to develop machine learning models that can accurately predict customer churn. We will do this by analyzing historical customer data to identify patterns and factors that contribute to churn. This information will then be used by the telecom company to develop strategies to reduce churn rates. Specifically, we will use a variety of machine learning algorithms, including logistic regression, decision trees, and random forests. We will also use feature engineering techniques to improve the accuracy of the models. We believe that this project will be a valuable tool for the telecom company. It will help them to identify customers who are at risk of churning and take steps to prevent them from leaving. This will save the company money and improve customer satisfaction.

Summary
Code	Name	Published Article	Deployed App
Capstone	Telco Customer Churn Prediction	Medium Article	Streamlit App
Project Setup
To set up the project environment, follow these steps:

Clone the repository:
git clone my_github

https://github.com/slickHnaa/Telco-Customer-Churn.git
Install the required dependencies:
pip install -r requirements.txt
Create a virtual environment:
Windows:

python -m venv venv
venv\Scripts\activate
Linux & MacOS:

python3 -m venv venv
source venv/bin/activate
You can copy each command above and run them in your terminal to easily set up the project environment.

Data
The data used in this project consists of a diverse collection of sepsis cases obtained from Zindi.

Data Fields
Column Name	Data Features	Description
REGION	Categorical	The location of each client
TENURE	Numeric	Duration with the network
MONTANT	Numeric	Top-Up Amount
FREQUENCE_RECH	Numeric	The number of times a customer refilled
REVENUE	Numeric	Monthly income of each client
ARPU_SEGMENT	Numeric	Income over 90 days divided by 3
FREQUENCE	Numeric	Number of times the client has made an income
DATA_VOLUME	Numeric	Number of connections
ON_NET	Numeric	Inter Expresso call
ORANGE	Numeric	Calls to Orange
TIGO	Numeric	Calls to Tigo
ZONE1	Numeric	Calls to Zone1
ZONE2	Numeric	Calls to Zone2
MRG	Categorical	A client who is going
REGULARITY	Numeric	Number of times the client is active for 90 days
TOP_PACK	Categorical	The most active packs
FREQ_TOP_PACK	Numeric	Number of times the client has activated the top pack packages
CHURN	Binary	Target variable to predict - Churn (Positive: customer will churn, Negative: customer will not churn)

Contributing Authors
Christopher Wachira, Tyokase Orseer, Henry Nii Ayitey-Adjin, UWIRINGIYIMANA Eliere
