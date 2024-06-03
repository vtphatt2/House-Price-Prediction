
# **DATA PREPROCESSING**

### **Errors encountered during data processing:**

1. * **Error Description:** When I first crawled the data from the web (raw data), I encountered an error where the `pd.read_csv` command could not be executed. Upon a preliminary review, I determined that this error was due to extra quotation marks (" ") in the data strings, leading to an incorrect data structure.

    * **Solution:** Temporarily fix this by removing the extra quotation marks (" "). This is a temporary measure until a more optimal method is found.