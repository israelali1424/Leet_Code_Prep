import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import calendar

# Sample Data (Replace with your actual data)
data = {
    'Date': pd.to_datetime(['2024-07-15', '2024-07-16', '2024-07-17', '2024-07-18', '2024-07-19', '2024-07-20', '2024-07-21', '2024-07-22', '2024-07-23', '2024-07-24', '2024-07-25']),
    'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
}
df = pd.DataFrame(data)

# Sidebar for Date Range Filter
st.sidebar.header("Date Range Filter")

# Date Picker for Start Date
start_date = st.sidebar.date_input("Start Date", min_value=df['Date'].min(), max_value=df['Date'].max(), value=df['Date'].min())

# Date Picker for End Date
end_date = st.sidebar.date_input("End Date", min_value=df['Date'].min(), max_value=df['Date'].max(), value=df['Date'].max())

# Convert to datetime objects and adjust end_date
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date) + timedelta(days=1) - timedelta(seconds=1)

# Filter the DataFrame
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Display the Filtered Data
st.header("Filtered Data")
st.dataframe(filtered_df)

# Calendar View (Improved)
st.subheader("Calendar View")

def display_calendar(year, month, data):
    cal = calendar.monthcalendar(year, month)
    st.write(f"### {calendar.month_name[month]} {year}")  # Month and Year header
    cols = st.columns(7)  # Create columns for the days of the week
    for day in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
        cols[0].write(day) #Write the day name only once
        cols = cols[1:] #Shift columns to the next one

    for week in cal:
        cols = st.columns(7)
        for day in week:
            if day == 0:  # Empty cell for days outside the month
                cols[0].write("")
            else:
                date_str = f"{year}-{month:02}-{day:02}"  # Create date string
                date_obj = pd.to_datetime(date_str)
                value = data.loc[data['Date'] == date_obj, 'Value'].iloc[0] if date_obj in data['Date'].values else None
                display_text = str(day)
                if value is not None:
                  display_text += f" ({value})"
                cols[0].write(display_text)

            cols = cols[1:]


# Display calendar for each month in the selected range
for dt in pd.date_range(start=start_date, end=end_date, freq='MS'):  # 'MS' for month start frequency
    year = dt.year
    month = dt.month
    month_data = filtered_df[(filtered_df['Date'].dt.year == year) & (filtered_df['Date'].dt.month == month)]
    display_calendar(year, month, month_data)


# Chart of Filtered Data
st.subheader("Chart of Filtered Data")
st.line_chart(filtered_df.set_index('Date')['Value'])