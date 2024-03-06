import pandas as pd
import matplotlib.pyplot as plt

# Define a custom color palette for better accessibility
custom_palette = ['skyblue', 'lightcoral', 'gold', 'purple', 'green']

# Read the hotel bookings data 
df = pd.read_csv('hotel_bookings.csv')

# Function to create a pie chart with clear labels and equal aspect ratio
def create_pie_chart(data, labels, title, startangle=90):
    plt.figure(figsize=(8, 8))
    patches, texts, autotexts = plt.pie(data, autopct='%1.1f%%', labeldistance=0.8, startangle=startangle, colors=custom_palette)
    plt.title(title)
    plt.axis('equal')

    # Remove autopct labels
    for autotext in autotexts:
        autotext.set_visible(False)

    # Adjust legend position to the right of the pie chart
    plt.legend(patches, labels, loc="best", fontsize=10)


    plt.show()

# Analyze hotel distribution
hotel_counts = df['hotel'].value_counts()

# Create pie chart for hotel distribution
create_pie_chart(hotel_counts, hotel_counts.index, 'Hotel Distribution')

# Analyze popular arrival months
arrive_month_counts = df['arrival_date_month'].value_counts()

# Create bar chart for popular arrival months
plt.figure(figsize=(10, 6))
arrive_month_counts.plot(kind='bar', color=custom_palette)  
plt.title('Popular Arrival Months')
plt.xlabel('Arrival Date Month')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Analyze stay nights in week and weekend (first 20 days)
stay_nights_in_week = df['stays_in_week_nights'].value_counts()
stay_nights_in_weekend = df['stays_in_weekend_nights'].value_counts()

# Create histogram for stay nights distribution
plt.figure(figsize=(10, 6))
plt.hist(
    [stay_nights_in_week, stay_nights_in_weekend],
    bins=range(11),
    alpha=0.7,
    label=['Week Nights', 'Weekend Nights'],
    align='left',
    color=custom_palette[:2]  
)
plt.xticks(range(11)) 
plt.title('Stay Nights Distribution (First 10 Days)')
plt.xlabel('Number of Nights')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

# Analyze total number of adults, children, and babies
sum_people = df[['adults', 'children', 'babies']].sum()

# Create pie chart for total number of people
create_pie_chart(sum_people, sum_people.index, 'People Distribution')

# Analyze booking distribution channels by country (top 5)
booking_distribution = df.groupby('country')['distribution_channel'].value_counts().unstack().fillna(0)
top_5_highest = booking_distribution.stack().nlargest(10)

# Create bar chart for booking distribution channels by country (top 5)
plt.figure(figsize=(10, 6))
top_5_highest.plot(kind='bar', color=custom_palette[:5])  
plt.title('Top Booking Distribution Channels by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
