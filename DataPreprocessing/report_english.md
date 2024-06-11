

# **DATA PREPROCESSING**

### **Issues encountered during data processing:**

**Issue 1:** 

* **Error Description:** When initially crawling data from the web (raw data), I encountered an error that prevented the execution of the `pd.read_csv` command. Upon a preliminary inspection, I discovered that the error was due to extra quotation marks in the data string, which caused the data structure to be incorrect.

* **Solution:** Use the `fix_csv_quotes` function to appropriately adjust the pairs of quotation marks (" ") in the data.

    * The `fix_csv_quotes` function was developed to fix the issue of extra or missing quotation marks in the CSV data. The function works by:
        1. Counting the number of quotation marks in each line.
        2. Identifying cases of missing quotation marks by checking if the number of quotation marks is even.
        3. Adding the missing quotation mark at the end of lines with an odd number of quotation marks.
    
    * Example: 
        - Incorrect data line: "data1", "data2", "data3""
        - Corrected data line: "data1", "data2", "data3"
    
    * After fixing all errors, the output CSV file is generated.

**Issue 2:** 

* **Error Description:** The data in the columns of the CSV file is not clean; specifically, there are unnecessary characters and special characters that could significantly impact subsequent processes.

* **Solution:** 
    * Write a `clean_string` function to clean the string by removing unnecessary symbols and characters. This function will retain alphabetic characters (uppercase and lowercase), numbers, periods, commas, and vertical bars.
    * Use the `clean_file_csv` function to apply the `clean_string` function to a specific column in the CSV file, in this case, the 'Description' column.

**Issue 3:** 

* **Error Description:** It is necessary to extract data from the 'Title' and 'Description' fields to fill in the missing data positions.

* **Solution:** Use regular expressions (regex) to extract information on prices, area, number of bedrooms, and number of bathrooms from the 'Title' and 'Description' fields. Specifically, regex patterns are used to search for patterns of prices, area, number of bedrooms, and number of bathrooms in the text and extract them. This extracted information is then stored in new columns in the DataFrame.

**Issue 4:** 

* **Error Description:** More detailed processing, calculations, and filling of missing values are needed.

* **Solution:** Convert the 'Price' and 'Area' columns to numeric types and calculate the price per square meter. Fill missing values based on the average values for each district and reasonable calculation rules. Specifically, the `fill_miss_vals` function calculates missing values for the 'Price' and 'Area' columns based on the average values by district. The `price_per_sqm` function calculates the price per square meter and adds this column to the DataFrame.

**Issue 5:** 

* **Error Description:** The data contains too many duplicate rows.

* **Solution:** Remove duplicate rows by checking the similarity of the 'Postdate' and 'Description' columns. First, completely identical rows are removed. Then, partially duplicated rows are compared based on the similarity of 'Postdate' and 'Description'. These duplicate rows are removed if they have a high similarity level.

**Issue 6:** 

* **Error Description:** Old posts may cause inaccuracies with the current timeframe, so it was decided to delete outdated data.

* **Solution:** Delete house sale posts from the year 2022. This is done by converting the 'Postdate' column to datetime type and filtering out rows with a posting year of 2022.

**Issue 7:** 

* **Error Description:** Some data entries are unreasonable and need to be removed.

* **Solution:** Remove unreasonable values by checking the 'Price_per_sqm' values. Rows with 'Price_per_sqm' values outside a reasonable range are removed. Then, adjust the values to be more reasonable based on the area. The `adjust_price` function adjusts the 'Price' column values based on the area and price per square meter.

**Issue 8:** 

* **Error Description:** House prices are not reasonable in some areas.

* **Solution:** Adjust the values to be more reasonable. The `adjust_price` function is used to adjust the 'Price' column values based on the area and price per square meter.

After completing all data processing steps, we saved the DataFrame to a CSV file:

- Recreate the 'No' column for better observation.
- Save the data to the output CSV file.
- Check for missing values in the DataFrame to ensure there are no remaining errors.

---
