# Titanic Data Analysis

# Titanic Data Analysis

<p align="center">
    <img src="data/portada.jpg" alt="alt text">
</p>

## Introduction
The sinking of the RMS Titanic on April 15, 1912, is one of the most infamous maritime disasters in history, 
resulting in the loss of over 1,500 lives. This notebook aims to analyze the Titanic dataset to uncover insights into the 
factors that influenced passenger survival. Through data visualization and statistical analysis,
we will explore the relationships between various variables, such as age, fare, and class, to understand the 
underlying patterns and correlations within the data.

## Repository Structure

- **EDA_Visualization_Titanic.ipynb**: The main Jupyter Notebook containing the step-by-step analysis of the Titanic dataset.
- **functions.py**: A Python script with helper functions used in the analysis.
- **app.py**: A Python script to run an interactive data visualization app using Streamlit.
- **data/**: Directory containing the Titanic dataset and any other relevant data files.

## Analysis Highlights

### Data Preparation
- **Data Cleaning**: Handling missing values and correcting data types.
- **Feature Engineering**: Creating new features and converting categorical variables to numeric format using one-hot encoding.

### Exploratory Data Analysis (EDA)
- **Descriptive Statistics**: Summarizing the main characteristics of the dataset.
- **Visualization**: Using plots to explore the distribution and relationships of variables.

### Correlation Matrices
- **Numeric Conversion**: Converting categorical variables like `Sex` and `Embarked` into numeric format.
- **Correlation Analysis**: Computing and visualizing the correlation matrix to understand the relationships between different variables.

### Trios Analysis
- **Detailed Examination**: Analyzing the interactions between multiple variables to uncover intricate patterns and correlations.
- **Group Insights**: Identifying significant groups within the dataset, such as males in third class traveling alone who did not survive.

## Key Findings
- The analysis reveals critical insights into the factors that influenced survival rates, such as gender, class, and family size.
- A significant social group was identified: males in third class traveling alone who did not survive.
- The framework used in this analysis is highly customizable, allowing for flexible and versatile exploration of different aspects of the data.

## How to Use
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Juanto19/EDA_Titanic.git
    cd Titanic_backup
    ```

2. **Install Dependencies**:
    Ensure you have Python and Jupyter Notebook installed. Then, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Notebook**:
    Open the Jupyter Notebook and run the cells to reproduce the analysis:
    ```bash
    jupyter notebook EDA_Visualization_Titanic.ipynb
    ```

## Running the Streamlit App

To run the interactive data visualization app using Streamlit, follow these steps:

1. **Install Streamlit**:
    If you haven't already installed Streamlit, you can do so using pip:
    ```bash
    pip install streamlit
    ```

2. **Install Other Dependencies**:
    Ensure you have all other necessary libraries installed. You can install them using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the App**:
    Navigate to the directory containing `app.py` and run the following command in your terminal:
    ```bash
    streamlit run app.py
    ```

4. **View the App**:
    After running the command, Streamlit will start a local web server. You can view the app by opening a web browser and navigating to the URL provided in the terminal (usually `http://localhost:8501`).

By following these steps, you should be able to run the interactive Titanic data visualization app and explore the data in an interactive manner.

## Conclusion
This repository provides a thorough analysis of the Titanic dataset, offering valuable insights into the factors that influenced passenger survival. The analysis framework is designed to be easily customizable, enabling further exploration and refinement of the study.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Special thanks to the creators of the Titanic dataset and the contributors to the various Python libraries used in this analysis, including Pandas, NumPy, Matplotlib, and Seaborn.

## Contact


- **Name:** Juan Torralbo Torrado
- **Email:** jtorralbotorrado@gmail.com
- **LinkedIn:**  [https://www.linkedin.com/in/juan-torralbo-torrado/](https://www.linkedin.com/in/juan-torralbo-torrado/)
- **GitHub:** [https://github.com/Juanto19](https://github.com/Juanto19)