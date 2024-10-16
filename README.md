# Titanic Data Analysis

## Overview

This repository contains a comprehensive analysis of the Titanic dataset, focusing on uncovering insights, factors, and tendencies that influenced the survival outcomes of the passengers. The analysis is conducted using various data visualization and statistical techniques, providing a detailed examination of the relationships between different variables.

## Repository Structure

- **EDA_Visualization_Titanic.ipynb**: The main Jupyter Notebook containing the step-by-step analysis of the Titanic dataset.
- **functions.py**: A Python script with helper functions used in the analysis.
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

## Conclusion
This repository provides a thorough analysis of the Titanic dataset, offering valuable insights into the factors that influenced passenger survival. The analysis framework is designed to be easily customizable, enabling further exploration and refinement of the study.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Special thanks to the creators of the Titanic dataset and the contributors to the various Python libraries used in this analysis, including Pandas, NumPy, Matplotlib, and Seaborn.

---

Feel free to customize this README further to fit your specific needs and repository details.