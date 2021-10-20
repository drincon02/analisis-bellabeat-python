# Bellabeat Data Analysis

## Basic Information:

This is the data analysis documentation for Bellabeat, a company that develops health-focused devices for women.
Bellabeat is a successful small company, but they want to become one of the biggest smart device competitors on the market.
As an analyst I have been asked to analyze one of their products to know how consumers are using their products.

The main products of the company are the following:
• Bellabeat App: An application that provides users with information related to their sleep, stress, activity, menstrual cycle, etc. With this information the user can make healthier decisions. The app connects with the smart product line.
• Leaf: A smart bracelet, necklace or clip that connects to the Bellabeat App to obtain user information.
• Clock: A smart watch that also connects to the Bellabeat App to provide information about the user
• Spring: A smart water bottle that measures the liters of water you have consumed, connects to the Bellabeat App to measure, and track your hydration levels.
• Bellabeat Membership: A membership program that guides the user in nutrition, sleep, health, and beauty based on their goals and lifestyle.

The marketing department has asked us to analyze smart products from another company and then apply that knowledge learned to one of Bellabeat's products.
For this, marketing needs to know the answer to 3 key questions:
1. What are the trends in the use of these smart devices?
2. How can these trends be applied to Bellabeat products?
3. How can these trends influence Bellabeat's marketing strategy?
To solve these questions, I am recommended to use the following public data from the company FitBit.
https://www.kaggle.com/arashnic/fitbit 
But we could consider adding another data source.

## Data Source:
For this analysis we were recommended to use an specific dataset on the kaggle.com page which comes from surveys conducted by Amazon Mechanical Turk between 12/03/2016 and 12/05/2016, 30 users gave their consent to give their FitBit data.
This is not an appropriate data source to perform the analysis because it comes from a third party that is not entirely reliable and the sample is only 30 users, which is too small to represent the entire population of users of smart products in addition to be dating from 2016 which may not represent the reality of today.
For this reason, treat this analysis with caution and the results of this analysis should not be taken as a true result.

## Data Manipulation:
Considering that some of the dataset files have millions of rows or records, we could use various tools such as Excel with Power Pivot and Access, SQL and a database, Python or R.
For this case we are going to use the Python programming language both to manipulate and graph the data.
If you want to know how I manipulated the data, I recommend you to go to the file called main.py

## Final Analysis:
For this analysis my main objective is to gather insights, trends on the usage of FitBit products and how these insights can be applied to Bellabeat
To begin with this analysis, the first thing I want to know is who are FitBit’s users so let’s find out what is FitBit users physical state.

![image](https://user-images.githubusercontent.com/87548196/138177535-24d41eef-1541-413b-9968-4ffbc9c519a3.png)

With this graph I can see that most users are overweight or normal weight while very few users are obese. An important factor that could influence the physical state of a user 
is sleep, or the number of hours they sleep a day.

So, the following graph will illustrate the number of users who sleep certain hours a day.

![image](https://user-images.githubusercontent.com/87548196/138177614-a27f8344-0722-4e75-86f7-4c6be8f570ee.png)

With this I see that most users sleep from 5 to 8 hours a day while very few sleep more than 8 hours a day.
Knowing this I want to know what variables influence the number of hours asleep and the physical state for this we will make a pearson correlation graph

![image](https://user-images.githubusercontent.com/87548196/138177647-9e2bea31-bdfa-4276-a3a7-3d7628a02696.png)

There are many interesting things that we can take out of this graph, such as that the more times you sleep a day, the worse health status the person has since it has a positive correlation of 0.93 between Normal_Count and TotalSleepRecords and 0.66 between BMI and TotalSleepRecords but in terms of the number of minutes or hours asleep there is no visible correlation.
I can also observe that there is a positive correlation between calories burned and very active minutes of 0.63.

For the BMI or Normal Count there is a negative correlation with all the variables relating to distance and training time, while there is a positive relationship with sedentary minutes.

Now that I know the relationship between the variables, I want to know what difference exists between each group of users.

![image](https://user-images.githubusercontent.com/87548196/138177736-1613b549-a9e7-456f-b619-c8a18640fb54.png)

Overweight and Normal Weight share some similarities in some habits and have some difference in another but there is a huge difference in habits with Obese Users
Now that I need to know in depth user’s habits, so I am going to find out when do users exercise.
The following table compares the calories burned with each day of the week.

![image](https://user-images.githubusercontent.com/87548196/138177767-8c0762d5-aea6-4f4a-b91a-5d247688f550.png)

As we see, on average, there is no day that stands out more than another in terms of calories burned. So, let's see if there is any difference in training hours.

![image](https://user-images.githubusercontent.com/87548196/138177782-a434a5a0-b953-43e9-9177-20d76eb71dab.png)

Here we can see that most of the calories are burned between 5 and 7 p.m.

## Conclusions and recommendations:
Based on the analysis, no strong conclusions or recommendations can be made due to the origin of the data, but several important points can be learned:
- Most FitBit users are overweight or normal weight, so they are people who pay enough attention to their body to not go into obesity. With this (considering the origin of the data) the BellaBeat company could direct its marketing to people who take time and effort to take care of their body at least to avoid obesity.

- We can also see that most users exercise in the afternoon, so going to gyms to do marketing of this product in the afternoon could be an interesting idea or in which case, being digital marketing before 5:00PM and after from 7:00PM.

- For data collection it could be an option that the device saves data automatically instead of being entered manually.

- Even though most users are healthy, there is still a great difference between user and user, so offering customization options for the different objectives that the user may have could be a good option, especially if BellaBeat wants to capture the attention of obese users.
