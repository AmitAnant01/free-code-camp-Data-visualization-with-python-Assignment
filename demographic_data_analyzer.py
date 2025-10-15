import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_people = df.shape[0]
    percentage_bachelors = ((bachelors_count / total_people) * 100).round(1)

    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    
    high_edu_df = df[df['education'].isin(advanced_education)]
    
    high_edu_count = high_edu_df.shape[0]
    
    high_edu_rich_count = high_edu_df[high_edu_df['salary'] == '>50K'].shape[0]
    
    higher_education_rich = ((high_edu_rich_count / high_edu_count) * 100).round(1)

    low_edu_df = df[~df['education'].isin(advanced_education)]
    
    low_edu_count = low_edu_df.shape[0]
    
    low_edu_rich_count = low_edu_df[low_edu_df['salary'] == '>50K'].shape[0]
    
    lower_education_rich = ((low_edu_rich_count / low_edu_count) * 100).round(1)

    min_work_hours = df['hours-per-week'].min()

    min_workers_df = df[df['hours-per-week'] == min_work_hours]
    
    num_min_workers = min_workers_df.shape[0]
    
    rich_min_workers = min_workers_df[min_workers_df['salary'] == '>50K'].shape[0]
    
    rich_percentage = ((rich_min_workers / num_min_workers) * 100).round(1)

    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    rich_percentage_by_country = (country_rich_counts / country_counts) * 100
    
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = rich_percentage_by_country.max().round(1)

    india_rich_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    
    top_IN_occupation = india_rich_df['occupation'].mode()[0]
    
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage of people with a Bachelor's degree: {percentage_bachelors}%")
        print(f"Percentage of people with advanced education who earn >50K: {higher_education_rich}%")
        print(f"Percentage of people without advanced education who earn >50K: {lower_education_rich}%")
        print(f"Minimum work hours per week: {min_work_hours} hours/week")
        print(f"Percentage of min workers who earn >50K: {rich_percentage}%")
        print(f"Country with highest percentage of high earners: {highest_earning_country}")
        print(f"Highest percentage of high earners in country: {highest_earning_country_percentage}%")
        print(f"Top occupation in India for high earners: {top_IN_occupation}")

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }