import pandas as pd
import random

# part 1: load and structure data
data = pd.read_csv("ms_data.csv")

# converting visit dates to datetime
data['visit_date'] = pd.to_datetime(data['visit_date'], errors = 'coerce')

# sort data by id and visit dates
data = data.sort_values(by = ['patient_id', 'visit_date'])


# part 2: add insurance info
insurance_file = "insurance.lst"

with open(insurance_file, "r") as f:
    insurance_tiers = [line.strip() for line in f.readlines()[1:]]

# randomly assinging insurance tiers to each patient
patient_ids = data['patient_id'].unique()
patient_insurance = {pid: random.choice(insurance_tiers) for pid in patient_ids}
data['insurance_type'] = data['patient_id'].map(patient_insurance)

# function generates visit costs based on insurance
def generate_visit_cost(insurance_tiers):
    base_cost = {
        "Basic": 100,
        "Premium": 50,
        "Platinum": 20
    }
    base_cost = base_cost.get(insurance_tiers, 50)  
    variation = random.uniform(-10, 10)  
    return round(max(0, base_cost + variation), 2) 

data['visit_cost'] = data['insurance_type'].apply(generate_visit_cost)


# part 3: calculate summary statistics
# Mean walking speed by education level
ave_speed_by_education = data.groupby("education_level")["walking_speed"].mean()

# Mean costs by insurance type
ave_cost_by_insurnace = data.groupby("insurance_type")["visit_cost"].mean()

# Age effects on walking speed
age_corr_speed = data["age"].corr(data["walking_speed"])



# create new data with insurnace for next part of exam
data.to_csv("ms_data_with_insurance.csv", index=False)

