This repository documents my 6–8 month journey to becoming a production-ready ML engineer.
Focus: fundamentals, failure modes, and real-world ML systems.

28/02/2026-EDA Project: E-commerce Customer Behavior

Project Overview
This project is an Exploratory Data Analysis (EDA) step conducted as part of a data science / machine learning workflow.
The objective was to deeply understand the dataset, identify patterns, validate assumptions, and extract signals that could later be used for feature engineering and predictive modeling.
Dataset: E-commerce Customer Behavior - Sheet1.csv
Size: 350 records
Domain: E-commerce customer behavior
Potential Extensions: Customer segmentation, churn prediction, recommendation systems

**What I worked on**
1. Performed data exploration, distribution analysis, and relationship analysis to understand underlying patterns.
2. Focused on identifying features that could influence customer satisfaction and spending behavior.
3. Formulated assumptions and tested them against data to understand signal vs noise, a key step before modeling.
4. Used minimal AI assistance, relying primarily on first-principles reasoning, statistics, and domain intuition.
5. Treated EDA as a foundation for ML, not an end goal.

**Assumptions Tested (Pre-Modeling Thinking)**
1. Absence of an explicit discount value may indicate a low or implicit discount (dataset does not confirm this).
2. Higher membership tiers were expected to correlate with higher discounts, which was not supported by data.
   These failed assumptions helped refine feature relevance for downstream ML tasks.

**Key Insights (Useful for ML Feature Engineering)** 
1. Membership level shows a strong relationship with customer satisfaction.
2. High-tier members spend more, making membership level a strong candidate feature for:
3. Revenue prediction
4. Customer lifetime value modeling

**Signals Worth Modeling Further**
1. Customers in lower membership tiers show higher dissatisfaction → possible churn signal.
2.Customers inactive for 30–45 days exhibit elevated dissatisfaction → strong candidate feature for churn prediction models.

09/03/2026
**Exploring the fundamentals of python**
This week analysed the use of python at a production level via FastApi source code 
According to me 
1. In production level it is always preferred to write code which understandable by anyone using it in python we can do this using type hints like annotated so that extra info can be added regarding the meta data
2. We focus on having minimal amount of code and focus is more on reusability we do that by using decorators which helps in modifying the behaviour of function by simpliy wrapping them by accepting them as parameters this is possible in python as python treats function as first class object which allows functions to be passed as parameters and returned  as values.
3. In production level environment, we focus on error handling so that the most unexpected error can be handled easily via custom exceptions invocation and exception handling mechanisms.
 


Check The WEEK1_DAY3&DAY4 notebook to see the code of the project
**Next ML-Oriented Steps**
1. Feature engineering using membership level, recency, and satisfaction
2. Customer segmentation using clustering
3. Supervised models for churn or spend prediction
