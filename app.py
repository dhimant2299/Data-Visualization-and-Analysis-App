import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import requests
import plotly.express as px
import io
import os
import plotly.io as pio
import plotly.graph_objects as go
# Custom CSS to set background images and styles
page_element = """
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://images.pexels.com/photos/82256/pexels-photo-82256.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
  background-size: cover;
}
[data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
}

[data-testid="stSidebar"]{
  background-image: url("https://images.pexels.com/photos/7078052/pexels-photo-7078052.jpeg");
  background-size: cover;
}
</style>
"""
# Apply custom CSS
st.markdown(page_element, unsafe_allow_html=True)
image = Image.open('animated.jpeg')
st.sidebar.image(image, width=500)

with st.sidebar:
    st.write('___________________________________')
    
    
    selected = option_menu('ANALYTICS', ['Data Analysis', 'Data Visualization'],
                           icons=['📈', '📊'],
                           default_index=0,)
    st.write('___________________________________')
# Method 1: HTML and CSS (Flexible and Customizable)

footer_html = """
<div class="my-footer" style="text-align: center; padding: 10px; background-color: #f0f0f0;">
  <p>© sadcompany
        By Sarbagya, Aswin, and Dhimant</p>

</div>
"""

footer_css = """
<style>
  .my-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 10%;
  }
</style>
"""

# Method 2: Streamlit Components (Simpler for Basic Footers)

def basic_footer():
  col1, col2 = st.columns(2)
  with col1:
      st.text("© 2024 sadcompany")
  with col2:
      st.write("Contact: [link](https://www.example.com)")

# Method 1
st.write(footer_html, unsafe_allow_html=True)
st.write(footer_css, unsafe_allow_html=True)


selected_option = None
if selected == 'Data Analysis' :
    st.markdown("______________________________________")
    
    # Define the HTML with a center-aligned heading
    center_aligned_title = f"<h1 style='text-align: center;'>SAD ANALYTICS </h1>"

    # Display the styled title using markdown with unsafe_allow_html
    st.markdown(center_aligned_title, unsafe_allow_html=True)
    
    
    # Define the HTML with a center-aligned heading
    center_aligned_header = f"<h2 style='text-align: center;'>APPLICATION FOR DATA ANALYSIS 📈 AND VISUALIZATION 📊</h2>"

    # Display the styled header using markdown with unsafe_allow_html
    st.markdown(center_aligned_header, unsafe_allow_html=True)
    st.markdown("______________________________________")
    


    def load_data(file):

            file_extension = file.name.split(".")[-1]
            if file_extension == "csv":
                data = pd.read_csv(file)
            elif file_extension in ["xls", "xlsx"]:
                data = pd.read_excel(file)
            else:
                st.warning("Unsupported file format. Please upload a CSV or Excel file.")
                return None
            return data
        
    file = None
    data = None

    if 'data' not in st.session_state:  # Check if data is not already loaded
            st.markdown("<h4 style=' padding: 10px; border-radius: 10px; font-family: Serif; color: black; text-align: center;'> Upload a Dataset for</h4>", unsafe_allow_html=True)
            image = Image.open('analysis.png')
            st.image(image, width=700)
            file = st.file_uploader("CSV or EXCEL", type=["csv", "excel"])
            if file is not None:
                col1, col2, col3 = st.columns([2, 1, 2])
                if col2.button("Load Data"):  # Button to trigger data loading
                    data = load_data(file)  # Call the load_data function
                    if data is not None:
                        st.session_state['data'] = data  # Store loaded data in session state
                    
        
    if 'data' in st.session_state:  # Check if data is loaded
            data = st.session_state['data']  # Retrieve data from session state
            
            st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5; font-family: Serif; color: black; text-align: center;'> Dataset Preview </h4>", unsafe_allow_html=True)

    def group_data(data, aggregation):
            def select_group_column(df):
                group_columns = st.sidebar.multiselect("Select Columns", df.columns, key="group_cols")
                return group_columns

    def select_columns(df):
            st.write("### Select Columns")
            all_columns = df.columns.tolist()
            options_key = "_".join(all_columns)
            selected_columns = st.multiselect("Select columns", options=all_columns)
        
            if selected_columns:
                sub_df = df[selected_columns]
                st.write("### Sub DataFrame")
                st.write(sub_df.head())
            else:
                st.warning("Please select a column.")

    def analyze_data(data):
        
            show_file_header(data)
            st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5;font-family: Serif; color: black; text-align: center;'>Select Columns : </h4>", unsafe_allow_html=True)
            all_columns = data.columns.tolist()
            options_key = "_".join(all_columns)
            selected_columns = st.multiselect("", options=all_columns)
        
            if selected_columns:
                sub_df = data[selected_columns]
                st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5;font-family: Serif; color: black; text-align: center;'> Dataset Preview : </h4>", unsafe_allow_html=True)
                st.table(sub_df.head())

                    
                def show_data_shape(data):
                    st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5; font-family: Serif; color: black; text-align: center '> Rows and Columns: </h4>", unsafe_allow_html=True)
                    shape_data = {
                    "Rows": [data.shape[0]],
                    "Columns": [data.shape[1]]
                    }
                    st.table(pd.DataFrame(shape_data))
                show_data_shape(sub_df)

                st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5; font-family: Serif; color: black; text-align: center;'>Descriptions: </h4>", unsafe_allow_html=True)
                st.table(sub_df.describe())


                show_columns_info(sub_df)
                show_missing_and_unique_values(sub_df)
                show_standard_deviation(sub_df)
                sorted_data = sort_data(sub_df)
                show_sorted_data(sorted_data)
                
            else:
                st.warning("Select Columns.")


    def show_file_header(data):
            
            st.table(data.head())

    def sort_data(data):
        # Sort the data by a selected column
            st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5;font-family: Serif; color: black;text-align: center;'>Sort by :</h4>", unsafe_allow_html=True)
            sort_column = st.selectbox("", data.columns)
            sorted_df = data.sort_values(by=sort_column)
            return sorted_df


    def show_sorted_data(sorted_df):
            st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5;font-family: Serif; color: black; text-align: center;'> Sorted Data :</h4>", unsafe_allow_html=True)
            #with st.expander("Click to view all data"):
            st.write(sorted_df)  # Display the entire DataFrame

    def show_columns_info(data):
            
            st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5;font-family: Serif; color: black; text-align: center;'>Column DataTypes : </h4>", unsafe_allow_html=True)
            column_info_df = pd.DataFrame({
            'Column Names': data.columns,
            'Data Types': data.dtypes
            })
            st.table(column_info_df)

    

    def show_missing_and_unique_values(data):
            st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5;font-family: Serif; color: black; text-align: center;'>Missing and Unique Values :</h4>", unsafe_allow_html=True)
            missing_values = data.isnull().sum()
            unique_values = data.nunique()
        
        # Create a DataFrame to combine the missing and unique values
            info_df = pd.DataFrame({
                'Column Names': data.columns,
                'Missing Values': missing_values,
                'Unique Values': unique_values
            })
            info_df = info_df.rename(columns={
                'Column Names': 'Column Name',
                'Missing Values': 'Missing Values Count',
                'Unique Values': 'Unique Values Count'
            })
            st.table(info_df)


    def show_standard_deviation(data):
            st.markdown("<h4 style=' padding: 10px; border-radius: 10px;  background-color:#D0D0B5;font-family: Serif; color: black; text-align: center;'>Standard Deviation : </h4>", unsafe_allow_html=True)
            std_deviation = data.std(numeric_only=True)
        
        # Create a DataFrame to show the standard deviation
            std_dev_df = pd.DataFrame({
                'Column Names': std_deviation.index,
                'Standard Deviation': std_deviation.values
            })
        
        # Rename the columns in the std_dev_df DataFrame
            std_dev_df = std_dev_df.rename(columns={
                'Column Names': 'Column Name',
                'Standard Deviation': 'Standard Deviation'
            })
        
            st.table(std_dev_df)

    if data is not None:
            analyze_data(data)
        
    def clear_data():
            # Clear data from session state
            if "data" in st.session_state:
                del st.session_state["data"]
        

    col1, col2, col3 = st.columns([2, 1, 2])

# Display the button in the center column
    if col2.button('Clear Data'):
        clear_data()
elif selected == 'Data Visualization':
     
    # Main function
    def main(): 
        data = None

        # Check if data is already loaded in session state
        if 'data' in st.session_state:
            data = st.session_state['data']  # Retrieve data from session state

        # Check if data is loaded
        if data is not None:

            st.markdown("<h1 style=' padding: 10px; border-radius: 10px;  background-color: #D0D0B5; font-family: Serif; color: black; text-align: center;'>Data Visualization</h1>", unsafe_allow_html=True)
                

            # Function to plot bar chart
            def plot_bar_chart(data, x_column, y_column):
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.barplot(data=data, x=x_column, y=y_column, ax=ax)
                ax.set_title(f"Bar Chart: {y_column} vs {x_column}")
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                st.pyplot(fig)

            # Function to plot line chart
            def plot_line_chart(data, x_column, y_column):
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.lineplot(data=data, x=x_column, y=y_column, ax=ax)
                ax.set_title(f"Line Chart: {y_column} vs {x_column}")
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                st.pyplot(fig)

            # Function to plot scatter plot
            def plot_scatter_plot(data, x_column, y_column):
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.scatterplot(data=data, x=x_column, y=y_column, ax=ax)
                ax.set_title(f"Scatter Plot: {y_column} vs {x_column}")
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                st.pyplot(fig)       
                
            chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot","Histogram", "Pie Chart", "Box Plot"], key="chart_type")

            if chart_type == "Bar Chart" or chart_type == "Line Chart":
                x_column = st.selectbox("Select X Column", data.columns, key="x_column_bar")
                y_column = st.selectbox("Select Y Column", data.columns, key= "y_column_bar")
            elif chart_type == "Line Chart":
                x_column = st.selectbox("Select X Column (Numeric)", data.select_dtypes(include=['int', 'float']).columns, key="x_column_line")
                y_column = st.selectbox("Select Y Column (Numeric)", data.select_dtypes(include=['int', 'float']).columns, key="y_column_line")
            elif chart_type == "Scatter Plot":
                x_column = st.selectbox("Select X Column (Numeric)", data.select_dtypes(include=['int', 'float']).columns, key="x_column_scatter")
                y_column = st.selectbox("Select Y Column (Numeric)", data.select_dtypes(include=['int', 'float']).columns, key="y_column_scatter")
            elif chart_type == "Histogram":
                x_column = st.selectbox("Select Column for Histogram", data.columns, key="x_column_histogram")
            elif chart_type == "Pie Chart":
                x_column = st.selectbox("Select Column for Pie Chart", data.columns, key="x_column_pie")
            
            elif chart_type == "Box Plot":
                x_column = st.selectbox("Select X Column for Box Plot", data.columns, key="x_column_box")

                
                
            fig = None

            if chart_type == "Bar Chart":
                fig = px.bar(data, x=x_column, y=y_column, title=f"Bar Chart: {y_column} vs {x_column}")

            elif chart_type == "Line Chart":
                fig = px.line(data, x=x_column, y=y_column, title=f"Line Chart: {y_column} vs {x_column}" , width=800, height=600)
                
            elif chart_type == "Scatter Plot":
                fig = px.scatter(data, x=x_column, y=y_column, title=f"Sactter Chart: {y_column} vs {x_column}" , width=800, height=600)
            elif chart_type == "Histogram":
                fig = px.histogram(data, x=x_column, title=f"Histogram: {x_column}")
            elif chart_type == "Pie Chart":
                fig = px.pie(data, names=x_column, title=f"Pie Chart: {x_column}")
            elif chart_type == "Box Plot":
                fig = px.box(data, x=x_column, title=f"Box Plot: {x_column}")

            
            if fig:
                st.plotly_chart(fig)

    
                    



        else:
            st.header("DATA VISUALIZATION")
            st.markdown("____________________________________________________")
            st.subheader("Load data in Data Analysis to visualize the data.")
            image = Image.open('sadnodata.jpeg')
            st.image(image, width=600)



    if __name__ == "__main__":
        main()