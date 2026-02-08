### libraries 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import os

os.makedirs("fig", exist_ok=True)

# loading the data 
def loading_data():
    df = pd.read_csv("shopping_behavior_updated (1).csv")
    return df

df = loading_data()

def understanding_data(df):
    print("Column Names :")
    print(df.columns)
    print("\nInfo:")
    print(df.info())
    print("\nDescribe:")
    print(df.describe())
    print("\nNull values:")
    print(df.isnull().sum())
    print("\nDuplicate values:")
    print(df.duplicated().sum())

understanding_data(df)

def cleaning_data(df):
    df['Purchase Amount (USD)'] = (
    df['Purchase Amount (USD)']
    .replace('[\$,]', '', regex=True)
    .astype(float)
)

    bins = [0,18,25,35,45,55,65,100]
    labels = ['<18','18-25','26-35','36-45','46-55','56-65','65+']
    df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels)

cleaning_data(df)

def preprocessing_data(df):

    Age_Gender_by_Amount = (
        df.groupby(['age_group','Gender'], observed=True)['Purchase Amount (USD)']
        .mean()
        .reset_index()
    )

    Age_gender_by_Category = (
        df.groupby(['age_group','Gender'], observed=True)
        .size()
        .reset_index(name='count')
    )

    Purchases_analysis = (
        df.groupby(['Item Purchased','Size'])
        .size()
        .reset_index(name='count')
    )

    Category_by_location = (
        df.groupby(['Category','Location'])['Purchase Amount (USD)']
        .mean()
        .reset_index()
    )

    Location_by_Size = (
        df.groupby(['Location','Size'])
        .size()
        .reset_index(name='count')
    )

    Subscription_by_location = (
        df.groupby(['Subscription Status','Location'])
        .size()
        .reset_index(name='count')
    )

    Location_by_Frequency = (
        df.groupby(['Location','Frequency of Purchases'])
        .size()
        .reset_index(name='count')
    )

    Season_by_Frequency = (
        df.groupby(['Season','Frequency of Purchases'])
        .size()
        .reset_index(name='count')
    )

    Iteam_Purchased_by_Review_Rating = (
        df.groupby(['Item Purchased','Review Rating'])
        .size()
        .reset_index(name='count')
    )

    Iteam_Purchased_by_FP = (
        df.groupby(['Item Purchased','Frequency of Purchases'])
        .size()
        .reset_index(name='count')
    )

    Age_Frequency_Spending = (
        df.groupby('age_group', observed=True)[
            ['Purchase Amount (USD)','Previous Purchases']
        ].mean()
    )

    Payment_Method_by_spending = (
        df.groupby('Payment Method')
        .size()
        .reset_index(name='count')
    )

    Discount_applied_by_Spending = (
        df.groupby('Discount Applied')
        .size()
        .reset_index(name='count')
    )

    Review_rating_by_RP = (
        df.groupby(['Review Rating','Previous Purchases'])
        .size()
        .reset_index(name='count')
    )

    Subscription_Frequency_Spending = (
        df.groupby('Subscription Status')[
            ['Purchase Amount (USD)','Previous Purchases']
        ].mean()
    )

    Coulour_by_gender_age = (
        df.groupby(['Color','Gender','age_group'], observed = True)
        .size()
        .reset_index(name='count')
    )

    loction_by_loyalty = (
        df.groupby(['Location','Subscription Status'])
        .size()
        .reset_index(name='count')
    )

    return (
        Age_Gender_by_Amount,
        Age_gender_by_Category,
        Purchases_analysis,
        Category_by_location,
        Location_by_Size,
        Subscription_by_location,
        Location_by_Frequency,
        Season_by_Frequency,
        Iteam_Purchased_by_Review_Rating,
        Iteam_Purchased_by_FP,
        Age_Frequency_Spending,
        Payment_Method_by_spending,
        Discount_applied_by_Spending,
        Review_rating_by_RP,
        Subscription_Frequency_Spending,
        Coulour_by_gender_age,
        loction_by_loyalty
    )

(
Age_Gender_by_Amount,
Age_gender_by_Category,
Purchases_analysis,
Category_by_location,
Location_by_Size,
Subscription_by_location,
Location_by_Frequency,
Season_by_Frequency,
Iteam_Purchased_by_Review_Rating,
Iteam_Purchased_by_FP,
Age_Frequency_Spending,
Payment_Method_by_spending,
Discount_applied_by_Spending,
Review_rating_by_RP,
Subscription_Frequency_Spending,
Coulour_by_gender_age,
loction_by_loyalty
) = preprocessing_data(df)
print(preprocessing_data(df))

def Visulization_analytics():
    plt.figure(figsize=(8,5))
    for gender in Age_Gender_by_Amount['Gender'].unique():
        temp = Age_Gender_by_Amount[Age_Gender_by_Amount['Gender']==gender]
        plt.bar(temp['age_group'], temp['Purchase Amount (USD)'], label=gender)
    plt.legend()
    plt.title('Average Spending by Age Group and Gender')
    plt.savefig('fig/Average_spending_by_age_gender.png')

    plt.figure(figsize=(10,5))
    plt.bar(Purchases_analysis['Item Purchased'], Purchases_analysis['count'])
    plt.xticks(rotation=90)
    plt.title('Purchases Analysis')
    plt.savefig('fig/Purchased_analysis.png')

    plt.figure(figsize=(8,5))
    plt.plot(Age_Frequency_Spending.index, Age_Frequency_Spending['Purchase Amount (USD)'])
    plt.plot(Age_Frequency_Spending.index, Age_Frequency_Spending['Previous Purchases'])
    plt.title('Age Group vs Spending & Previous Purchases')
    plt.savefig('fig/AG_by_Spending.png')

    plt.figure(figsize=(8,5))
    plt.bar(Payment_Method_by_spending['Payment Method'], Payment_Method_by_spending['count'])
    plt.title('Payment Method Usage')
    plt.savefig('fig/Payment_method_usage.png')

    plt.figure(figsize=(6,4))
    plt.bar(Discount_applied_by_Spending['Discount Applied'], Discount_applied_by_Spending['count'])
    plt.title('Effect of Discount')
    plt.savefig('fig/Effect_of_discount.png')

    plt.figure(figsize=(8,5))
    plt.bar(loction_by_loyalty['Location'], loction_by_loyalty['count'])
    plt.title('Customer Loyalty by Location')
    plt.savefig('fig/loyalty_by_location.png')

Visulization_analytics()
