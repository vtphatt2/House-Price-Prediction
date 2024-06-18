# **DATA PREPROCESSING AND FEATURE ENGINEERING**

### **Issues Encountered During Data Processing:**

**Issue 1:** 

* **Description:** When initially crawling data from the web (raw data), I encountered an error that prevented the execution of the `pd.read_csv` command. Upon a preliminary inspection, I discovered that the error was due to extra quotation marks in the data string, which caused the data structure to be incorrect.

* **Solution:** Use the `fix_csv_quotes` function to appropriately adjust the pairs of quotation marks (" ") in the data.

    * The `fix_csv_quotes` function was developed to fix the extra quotation marks in the CSV data. The function works by:
        1. Counting the number of quotation marks in each line.
        2. Identifying cases of missing quotation marks by checking if the number of quotation marks is even.
        3. Adding missing quotation marks to the end of lines with an odd number of quotation marks.
    
    * Example: 
        - Incorrect data line: "data1", "data2", "data3""
        - Corrected data line: "data1", "data2", "data3"
    
    * After fixing all errors, export the corrected file as an output CSV.

**Issue 2:** 

* **Description:** The data in the CSV file columns is not clean; specifically, there are unnecessary characters and special characters that could significantly impact subsequent processes.

* **Solution:** 
    * Write the `clean_string` function to clean the string by removing unnecessary symbols and characters. This function retains alphabetic characters (uppercase and lowercase), numbers, periods, commas, and |.
    * Use the `clean_file_csv` function to apply the `clean_string` function to a specific column in the CSV file, in this case, the 'Description' column.

**Issue 3:** 

* **Description:** Data needs to be extracted from the 'Title' and 'Description' fields to fill in missing data.

* **Solution:** Use regular expressions (regex) to extract information on price, area, number of bedrooms, and number of bathrooms from the 'Title' and 'Description' fields. Specifically, regex expressions are used to find patterns for price, area, number of bedrooms, and number of bathrooms in the text and extract them. This information is then stored in new columns in the DataFrame.

**Issue 4:** 

* **Description:** Detailed processing, calculations, and filling of missing values are needed.

* **Solution:** Convert the 'Price' and 'Area' columns to numeric types and calculate the price per square meter. Fill missing values based on the average value of each district and reasonable calculation rules. Specifically, the `fill_miss_vals` function calculates missing values for the 'Price' and 'Area' columns based on the average values per district. The `price_per_sqm` function calculates the price per square meter and adds this column to the DataFrame.

**Issue 5:** 

* **Description:** There are too many duplicate rows in the data.

* **Solution:** Remove duplicate rows by checking the similarity of the 'Postdate' and 'Description' columns. Initially, fully duplicate rows are removed. Then, partially duplicate rows are compared based on the similarity of 'Postdate' and 'Description', and these duplicate rows are removed if they have a high level of similarity.

**Issue 6:** 

* **Description:** Old posts can cause inaccuracies with the current timeframe, so we decided to delete outdated data.

* **Solution:** Delete house sale posts from 2022. This is done by converting the 'Postdate' column to the datetime format and filtering out rows with a post date in 2022.

**Issue 7:** 

* **Description:** Some data entries are unreasonable and need to be removed.

* **Solution:** Remove unreasonable values by checking the 'Price_per_sqm' value. Rows with 'Price_per_sqm' values outside the reasonable range are removed. Then, adjust the price for more reasonable values based on the area. The `adjust_price` function adjusts the 'Price' column values based on the area and price per square meter.

**Issue 8:** 

* **Description:** House prices are unreasonable in some areas.

* **Solution:** Adjust the prices for more reasonable values. The `adjust_price` function adjusts the 'Price' column values based on the area and price per square meter.

**Issue 9:** 

* **Description:** Missing values need to be predicted for the Floors, Bedrooms, and WCs columns.

* **Solution:** Train K-Nearest Neighbors (KNN) models to predict missing values for these columns based on the features: Area, Price per square meter, District (encoded), and Month. This process includes the following steps:
    * Select the necessary features.
    * Split the data into training and testing sets.
    * Train the KNN model for each column: Floors, Bedrooms, and WCs.
    * Predict and fill in the missing values for the corresponding columns in the DataFrame.

### **Final Results:**

After completing the data processing steps, we saved the DataFrame to a CSV file:

- Recreate the 'No' column for easier observation.
- Save the data to the output CSV file.
- Check for missing values in the DataFrame to ensure no errors remain.

---

## **EXPLORATORY DATA ANALYSIS (EDA) AND DATA PREPARATION**