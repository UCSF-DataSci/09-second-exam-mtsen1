# Final Exam

## Question 1

The `prepare.sh` file runs the `generate_dirty_data.py` to create the original data. It then removes empty lines, comments, and extra commas and keeps only the essential columns. The cleaned data is saved into `ms_data.csv`. It also creates the `insurance.lst` file with the insurance tiers. Lastly, it displays the number of rows in the data and print the first 5 rows.

## Question 2

### Part 1

The cleaned data is converted into the correct data type and sorted by patient ID and visit date.

### Part 2

With `random`, an insurance tier is assigned to each unique patient ID. Then, based on the insurance type, a visit cost is generated with some variation. 

### Part 3

With the `groupby` function, the mean walking speed by education and mean visit cost by insurance tier can be found. 

The mean walking speed by education level is as follows:

- Bachelors:       3.972190
- Graduate:        4.500052
- High School:     3.253318
- Some College:    3.623781

The mean visit cost by insurance tier is as follows:

- Basic:       99.933845
- Platinum:    20.026779
- Premium:     50.008352

The correlation coefficient between age and walking speed is found using `corr` in which a coefficient of -0.696 was observed. Therefore, as age increases, walking speed tends to decrease.


## Question 3

### Part 1

First, outliers were removed from walking speed and visit cost. Outliers in walking speed were removed and no outliers were found in visit cost. 

The multiregression model for the relationship between walking speed and age adjusted by educated level is as follows:

`walking_speed = 5.6061 - 0.0303(age) - 0.7805(High School) + 0.4028(Graduate) - 0.3948(Some College)`

with an R^2 valued of 0.804 indicating the model is a moderately good fit for the data. 

The 95% confidence intervals for each variable is as follows:
- Intercept: (5.586, 5.626)
- High school:  (-0.796, -0.765)
- Graduate: (0.387, 0.418)   
- Some college: (-0.410, -0.380) 
- Age: (-0.031, -0.030)

Lastly , each of the variables (age and each education level) have a p-value of approximately 0, indicating each variable has a significant impact on walking speed. 

### Part 2

A one-way ANOVA model is used to analyze the effect of insurance type on visit cost. From this model, we obtain an F-statistic of 253785.91 and a p-value of 0.0 indicating there is at least one insurance type with a significantly different mean visit cost.

`insurance_plot.png` displays the boxplots of visit cost by insurance type with `matplotlib`. Some basic summary statistics: 

| insurance_type | mean      | std       | count |
|----------------|-----------|-----------|-------|
| Basic          | 99.971712 | 5.730249  | 5147  |
| Platinum       | 19.965499 | 5.741754  | 5005  |
| Premium        | 49.953354 | 5.701578  | 5286  |

Lastly, the effect sizes were calculated with Cohen's d. The output of this is as follows:

- Basic vs Premium: 8.7507
- Basic vs Platinum: 13.9481
- Premium vs Platinum: 5.2411

The effect size analysis along with the boxplots reveal the greatest visit cost difference is between the Basic and Platinun plan which is expected. 


## Question 4

Each plot is made with `matplotlib` and some with the addition of `seaborn`. 