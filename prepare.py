import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats

from sklearn.model_selection import train_test_split

def pull_csv():
    
    '''
    Pulls the hr attrition csv and cleans up the dataframe to be used later for exploration and modeling
    '''
    
    df = pd.read_csv('hr_attrition.csv')
    
    df.columns = df.columns.str.lower()
    
    df = df.drop(columns = ['over18', 'employeecount', 'employeenumber', 'standardhours', 'dailyrate','businesstravel', 'distancefromhome',\
                            'education', 'employeenumber', 'hourlyrate', 'jobinvolvement', 'jobrole', 'jobsatisfaction', 'monthlyrate', 'overtime',\
                            'relationshipsatisfaction', 'worklifebalance', 'yearsincurrentrole', 'yearssincelastpromotion',])
    
    df['attrition'] = df.attrition.map({'Yes' : 1, 'No' : 0})
    df['maritalstatus'] = df.maritalstatus.map({'Divorced' : 0, 'Single': 1, 'Married': 2})
    df['department'] = df.department.map({'Research & Development' : 0, 'Sales' : 1, 'Human Resources' : 2})
    df['educationfield'] = df.educationfield.map({'Other' : 0, 'Life Sciences' : 1, 'Medical': 2, 'Marketing' : 3, 'Technical Degree' : 4,\
                                                 'Human Resources' : 5})
    
    df.info()
    
    return df

def my_train_test_split(df, target):
    
    '''
    Takes in a dataframe and preforms a split on it returning a train, validate and test set for exploration
    and modeling
    '''
    
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])
    
    return train, validate, test



def dtypes_to_list(df):
    
    '''
    Takes in a dataframe and returns a list of numerical features and a list of categorical features.
    '''
    
    num_list , cat_list = [], []

    for column in df:
        col_type = df[column].dtype
        if col_type == 'object':
            cat_list.append(column)
        if np.issubdtype(df[column], np.number) and \
             ((df[column].max() + 1) / df[column].nunique())  == 1 :
            cat_list.append(column)
        if np.issubdtype(df[column], np.number) and \
            ((df[column].max() + 1) / df[column].nunique()) != 1 :
            num_list.append(column)
    return num_list, cat_list

def hr_vis(train, col):
    plt.title('Relationship of attrition rate and '+col)
    sns.countplot(x=col, hue ='attrition', data=train)
    att_rate = train.attrition.mean()
    plt.axhline(att_rate, label='attrition rate')
    plt.xlabel(col)
    plt.show()

def hr_test(train, col):
    alpha = 0.05
    null_hyp = col+' and attrition rate are independent'
    alt_hyp = 'There is a relationship between attrition rate and '+col
    observed = pd.crosstab(train.attrition, train[col])
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis that', null_hyp)
        print(alt_hyp)
    else:
        print('We fail to reject the null hypothesis that', null_hyp)
        print('There appears to be no relationship between attrition rate and '+col)

def hr_analysis(train, col):
    '''
    Takes in the train set and specific column to be examined.  Returns a countplot and a chi square test for the 
    specific feature.    
    '''
    hr_vis(train, col)
    hr_test(train, col)
    

def model_prep(train, validate, test):
    '''
    Takes in the train, validate, and test split sets and returns the features and target variables that will be used in 
    model creation.
    '''
    
    
    X_train = train.drop(columns=(['attrition', 'gender', 'educationfield']))
    y_train = train.attrition
    X_validate = validate.drop(columns=(['attrition', 'gender', 'educationfield']))
    y_validate = validate.attrition
    X_test = test.drop(columns=(['attrition', 'gender', 'educationfield']))
    y_test = test.attrition
    
    print(f"The baseline accuracy for retained employees in all cases within the hr_analytics dataset is {(y_train == ).mean():.2}")
    
    return X_train, X_validate, X_test, y_train, y_validate, y_test
    