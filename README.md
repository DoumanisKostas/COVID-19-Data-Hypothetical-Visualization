# README for COVID-19 Data Visualization

## Overview
This project visualizes COVID-19 confirmed cases for different countries over time using hypothetical data. It generates two bar plots showing the number of confirmed cases for six countries: Greece, Italy, Spain, Germany, France, and China.

**Note:** The data used in this project is hypothetical and randomly generated for demonstration purposes. For real-world analysis, you should replace the data generation part with actual data from reliable sources.

## Data
- **Date Range**: December 1, 2019, to December 31, 2022
- **Countries**: Greece, Italy, Spain, Germany, France, China
- **Data Columns**:
  - `date`: Date of the record
  - `country`: Country of the record
  - `confirmed`: Number of confirmed COVID-19 cases
  - `deaths`: Number of deaths due to COVID-19
  - `recovered`: Number of recovered COVID-19 cases

## Code Description
1. **Data Creation**:
   - The code generates hypothetical data for confirmed cases, deaths, and recoveries for the specified countries over the given date range.

2. **Data Aggregation**:
   - The data is aggregated on a monthly basis to provide a clearer view of the trends over time.

3. **Visualization**:
   - Two bar plots are created using Matplotlib and Seaborn:
     - **First Plot**: Shows confirmed cases for Greece, Italy, and Spain.
     - **Second Plot**: Shows confirmed cases for Germany, France, and China.
   - Both plots are displayed in a single figure with two subplots.

4. **Plot Customization**:
   - The x-axis labels (dates) are rotated by 45 degrees to enhance readability.
   - Different colors are used for each country to improve visual differentiation.

## Requirements
- **Python Libraries**:
  - pandas
  - numpy
  - matplotlib
  - seaborn

## How to Run
1. Ensure you have Python installed.
2. Install the required libraries if you haven't already:
   ```bash
   pip install pandas numpy matplotlib seaborn
