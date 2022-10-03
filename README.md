# Individual Project Summary

## Project Goals

> - Work on an individual data science project that touches the full DS pipeline (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), provide findings, and offer key takeaways.
> - Create modules (prepare.py) that make my process repeateable and my report (notebook) easier to read and follow.
> - Ask exploratory questions of my data that will help me understand more about the attributes and drivers of attrition at the mystery company. Answer questions through charts and statistical tests.
> - Construct a model to predict attrition rate for employees at the mystery company.
> - Make recommendations to a data science team about how to improve predictions.
> - Refine my work into a report, in the form of a jupyter notebook, that I will be reviewed by my peers.

## Project Description

### Deliverables

> - **Readme (.md)**
> - **Prepare Modele (.py)**
> - **Final Notebook (.ipynb)**

## Data Dictionary

|Target|Definition
|:-------|:----------|
|attrition|Whether an employee has left the company through attrition or not|

|Feature|Definition|
|:-------|:----------|
|age                     |How old the employee currently is|
|department              |What department in the company the employee works under|
|educationfield          |What field of study the employee committed themselves to in school|
|environmentsatisfaction |On a scale from 1 to 4, how well the employee rates the work environment|
|gender                  |Whether the employee is male or female| 
|joblevel                |Level of seniority of the employee|
|maritalstatus           |Is the employee single, married or divorced|
|monthlyincome           |The monthly income of the employee in dollars|
|numcompaniesworked      |How many companies the employee has worked for|
|percentsalaryhike       |The percentage of increase in pay for the employee|
|performancerating       |How well the employee's performance was rated (3 or 4)|
|stockoptionlevel        |The level of stock options offered to the employee (added monetary benefits)|
|totalworkingyears       |Total numbers of years the employee has worked in the workforce as a whole|
|trainingtimeslastyear   |How many times the employee participated in training last year|
|yearsatcompany          |How long the employee has worked for this company|
|yearswithcurrmanager    |How long the employee has worked for their current manager|

## Initial Hypotheses
- My thought process going into this project is that the individauls who have a weaker incentive to stay monetarily are the ones who incur higher turnover.

## Executive Summary - Key Findings and Recommendations
> 1. Utilizing the features that showed distinct influence on our target variable ('attrition') allowed for a decent mvp model with lack of detailed information and a small dataset compared to most.

> 2. My recommendations are that the company focuses on employees that are new to the workforce and are new to the company and are between the ages 25-36.  These are the individuals who have high attrition rates for whatever reason.

> 3. Next steps at this company are to find out why younger employees new to the workforce and/or to the company are deciding to the leave the company.  Much of the other categories that were given didn't give great insight into a distinct shift in attrition rate and even more so a lot of the categories didn't have great descriptions to start off with.  I would probably send out questionnaires or do 1v1 interviews with a sample population of the aforementioned target groups.  My model was not able to add enough value to baseline predictions thus we need to explore further into the data and attempt to find more meaningful information on why employees may quit.

## Project Plan

### Planning Phase

> - Created a README.md file
> - Imported all of my tools and files needed to properly conduct the project.

### Acquire Phase

> - Utilized my prepare file to pull the HR analytics data from a csv offered on Kaggle.

### Prepare Phase

> - Utilized my prepare file to clean up my HR analytics dataset.
> - Split the overall dataset into my train, validate, and test datasets.

### Explore Phase

> - Created visualizations via pairplots and heatmaps to see the correlation between each feature within my train dataset.
> - Asked clear questions about that data such as how each salary based feature affected attrition rate.
> - Created visuals and utilized hypothesis testing (chi-square method) to best answer and provide insight into my aformentioned questions.

### Model Phase

> - Set up the baseline prediction for future models to base their success on.
> - Trained multiple models for each type of Classification technique ()
> - Validated all models to narrow down my selection to the best performing model.
> - Chose the MVP of all created models and used the test data set to ensure the best model worke entirely to expectations

### Deliver Phase

> - Prepped my final notebook with a clean presentation to best present my findings and process to my peers and instructors.

## How To Reproduce My Project

> 1. Read this README.md
> 2. Download the prepare.py and final_report_HR.ipynb files into your directory along with the hr_attrition.csv
> 3. Run my final_report.ipynb notebook
> 4. Congratulations! You can predict attrition at mystery company!