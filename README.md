SAD ANALYTICS

This Streamlit web app provides tools for data analysis and visualization. It allows you to upload a CSV or Excel file, explore the data, and create various charts to understand the distribution and relationships within your data.

Getting Started

Clone the repository or download the files.
Install required libraries:

pip install streamlit pandas matplotlib seaborn streamlit_option_menu requests plotly.express

Run the app:

streamlit run app.py

Using the App

The app has a sidebar for navigation and two main sections: Data Analysis and Data Visualization.

Data Analysis

Upload a CSV or Excel file containing your data.
Preview the first few rows of the data.
Select columns to analyze.
View data summary statistics including data types, missing values, unique values, and standard deviation.
Sort data by a chosen column.
Data Visualization

Select the data loaded in the Data Analysis section (requires data to be uploaded first).
Choose a chart type (Bar Chart, Line Chart, Scatter Plot, Histogram, or Pie Chart).
Select the columns for the x-axis and y-axis (depending on the chart type).
The selected chart will be displayed.
Styling

The app uses custom CSS styling to enhance the user interface. The CSS styles are defined within the Python code (st.write with HTML tags) for simplicity.


This is a basic example showcasing Streamlit for data analysis and visualization. It can be further customized and extended to meet specific data exploration needs.