# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 00:21:55 2020

@author: rinor
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#Salary parsing

df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Emplyer Provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)


df = df[df['Salary Estimate'] != '-1'] #Removing -1 Salary Estimate
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0]) #Removing salary description
rm_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', '')) #Replacing K and $ with empty space

min_hr = rm_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2

#Company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-1], axis = 1)


#State field

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
print(df.job_state.value_counts())


df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#Age of company

df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

#Parsing of job description (python, spark, aws, excel)

df['Job Description']

df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('salary_data_cleaned', index = False)




