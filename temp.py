import streamlit as st
import pandas as pd
import numpy as np

# Configuration to enable wider layout and right sidebar
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)

# Create two containers for our sidebars
left_sidebar_placeholder = st.sidebar.empty()
right_sidebar_placeholder = st.empty()

# Custom CSS for dual sidebars
st.markdown("""
<style>
    /* Main table styles */
    .stDataFrame {
        height: 400px;
        overflow-y: scroll !important;
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        padding: 10px;
        background-color: white;
    }
    .stDataFrame table {
        text-align: left !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stDataFrame thead tr th {
        position: sticky !important;
        top: 0;
        background: linear-gradient(180deg, #2c5282 0%, #2b6cb0 100%) !important;
        color: white !important;
        font-weight: bold !important;
        padding: 12px 15px !important;
        z-index: 999;
        text-align: left !important;
        border-bottom: 2px solid #e5e7eb !important;
    }
    .stDataFrame tbody tr:nth-child(even) {
        background-color: #f7fafc;
    }
    .stDataFrame tbody tr:nth-child(odd) {
        background-color: #ffffff;
    }
    .stDataFrame tbody tr:hover {
        background-color: #ebf4ff !important;
    }

    /* Right sidebar styling */
    [data-testid="stSidebarContent"] {
        background-color: #f8fafc;
    }
    
    /* Term card styling */
    .term-card {
        background-color: white;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
        border-left: 4px solid #2b6cb0;
    }
</style>
""", unsafe_allow_html=True)

# Create sample data
data = {
    'Name': [f'Person {i}' for i in range(1, 101)],
    'Age': np.random.randint(20, 80, 100),
    'Salary': np.random.randint(30000, 120000, 100),
    'Department': np.random.choice(['HR', 'IT', 'Sales', 'Marketing'], 100),
    'Years of Experience': np.random.randint(1, 20, 100),
    'Performance Score': np.random.uniform(3.0, 5.0, 100).round(2)
}
df = pd.DataFrame(data)

# Left sidebar content
with st.sidebar:
    st.header('Table Filters')
    search_term = st.text_input('Search by Name')
    dept_filter = st.multiselect('Filter by Department', 
                                options=sorted(df['Department'].unique()),
                                default=[])
    
    st.markdown('---')
    st.subheader('Age Percentile Filter')
    percentile = st.text_input('Show Top Percentage of Ages', 
                              value='100',
                              help='Enter a number between 1-100 to show top N% of ages')
    
    try:
        percentile = float(percentile)
        if percentile < 1 or percentile > 100:
            st.error('Please enter a number between 1 and 100')
            percentile = 100
    except ValueError:
        st.error('Please enter a valid number')
        percentile = 100

    st.markdown('---')
    st.subheader('Summary Statistics')

# Main content
col1, col2 = st.columns([4, 1])

with col1:
    # Apply filters
    filtered_df = df.copy()
    if search_term:
        filtered_df = filtered_df[filtered_df['Name'].str.contains(search_term, case=False)]
    if dept_filter:
        filtered_df = filtered_df[filtered_df['Department'].isin(dept_filter)]

    # Apply age percentile filter
    age_threshold = np.percentile(df['Age'], 100 - percentile)
    filtered_df = filtered_df[filtered_df['Age'] >= age_threshold]
    filtered_df = filtered_df.sort_values('Age', ascending=False)

    st.header("Employee Database")
    if percentile < 100:
        st.info(f"Showing employees in the top {percentile:.1f}% by age (Age ≥ {age_threshold:.0f})")
    
    st.dataframe(
        filtered_df,
        height=400,
        column_config={
            'Name': st.column_config.TextColumn('Name', width='medium'),
            'Age': st.column_config.NumberColumn('Age', width='small'),
            'Salary': st.column_config.NumberColumn('Salary', format='$%d', width='medium'),
            'Department': st.column_config.TextColumn('Department', width='medium'),
            'Years of Experience': st.column_config.NumberColumn('Years of Experience', width='small'),
            'Performance Score': st.column_config.NumberColumn('Performance Score', format='%.2f', width='medium')
        },
        hide_index=True
    )

# Update summary statistics in left sidebar
with st.sidebar:
    st.write(f"Total Employees: {len(filtered_df)}")
    st.write(f"Average Salary: ${filtered_df['Salary'].mean():,.2f}")
    st.write(f"Average Age: {filtered_df['Age'].mean():.1f}")
    st.write(f"Age Range: {filtered_df['Age'].min():.0f} - {filtered_df['Age'].max():.0f}")

# Right sidebar content using a second sidebar container
with col2:
    # Add expander to make it collapsible
    with st.expander("📚 Key Terms", expanded=True):
        st.markdown("""
        <div class="term-card">
            <strong>Performance Score</strong><br>
            • 4.5 - 5.0: Outstanding<br>
            • 4.0 - 4.4: Exceeds Expectations<br>
            • 3.5 - 3.9: Meets Expectations<br>
            • 3.0 - 3.4: Needs Improvement
        </div>
        
        <div class="term-card">
            <strong>Department</strong><br>
            • HR: Human Resources<br>
            • IT: Information Technology<br>
            • Sales: Sales and Business Development<br>
            • Marketing: Marketing and Communications
        </div>
        
        <div class="term-card">
            <strong>Years of Experience</strong><br>
            Total years of relevant work experience, including both internal and external positions.
        </div>
        
        <div class="term-card">
            <strong>Salary</strong><br>
            Annual compensation in USD, excluding bonuses and benefits.
        </div>
        """, unsafe_allow_html=True)