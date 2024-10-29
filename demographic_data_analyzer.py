import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=0, sep=',', names=['age','workclass','fnlwgt','education','education-num',
                                                       'marital-status','occupation','relationship','race','sex',
                                                       'capital-gain','capital-loss','hours-per-week','native-country','salary'])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    total_count = df.shape[0]
    count_bachelors = df.loc[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((count_bachelors / total_count) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.query('education in ["Bachelors", "Masters", "Doctorate"]')
    lower_education = df.query('education not in ["Bachelors", "Masters", "Doctorate"]')

    total_advanced_educ = higher_education.shape[0]
    make_more = higher_education.loc[df['salary'] == '>50K'].shape[0]

    total_not_ad = lower_education.shape[0]
    make_more_2 = lower_education.loc[df['salary'] == '>50K'].shape[0]

    # percentage with salary >50K
    higher_education_rich = round((make_more/total_advanced_educ) * 100, 1)
    lower_education_rich = round((make_more_2/total_not_ad) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    people_min = df.query("`hours-per-week` == 1")
    total_people_min = people_min.shape[0]
    big_salary = people_min.loc[people_min['salary'] == '>50K'].shape[0]

    rich_percentage = round((big_salary / total_people_min) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    rich_countries = df.loc[df['salary'] == ">50K", 'native-country'].value_counts()
    population = df['native-country'].value_counts()
    percnt = (rich_countries / population).sort_values(ascending=False)
    perct_max = percnt.max()
    highest_earning_country = percnt.idxmax() * 100
    highest_earning_country_percentage = round(perct_max, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    people_india = df.query("`native-country` == 'India'")
    indians_more_50 = people_india.query("`salary` == '>50K'")
    occupations = indians_more_50.occupation.value_counts(normalize=True)
    top_IN_occupation = occupations.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
