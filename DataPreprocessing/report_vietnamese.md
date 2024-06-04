

# **DATA PREPROCESSING**

### **Errors encountered during data processing:**

**Vấn đề 1:** 

* **Mô tả lỗi:** Khi vừa mới crawl data từ web về (raw data), em gặp lỗi không thể thực hiện được lệnh `pd.read_csv`. Sau khi kiểm tra sơ lược, em phát hiện lỗi này xuất phát từ việc dư dấu " " trong chuỗi data, dẫn đến cấu trúc data bị sai.

* **Giải pháp:** Sử dụng hàm `fix_csv_quotes` để thực hiện chỉnh sửa các cặp dấu (" ") sao cho hợp lý.

    * Hàm `fix_csv_quotes` được phát triển để sửa lỗi dư dấu ngoặc kép trong dữ liệu CSV. Hàm hoạt động bằng cách:

        1. Đếm số lượng dấu ngoặc kép trong mỗi dòng.

        2. Xác định các trường hợp thiếu dấu ngoặc kép bằng cách kiểm tra xem số lượng dấu ngoặc kép có chẵn hay không.

        3. Bổ sung dấu ngoặc kép thiếu vào cuối các dòng có số lượng dấu ngoặc kép lẻ.
    
    * Ví dụ: 

        Dòng dữ liệu sai lệch: "data1", "data2", "data3""

        Dòng dữ liệu sau khi sửa: "data1", "data2", "data3"
    
    * Sau khi đã fix xong tất cả lỗi thì xuất lại file output csv.


**Vấn đề 2:** 

* **Mô tả lỗi:** Data trong các cột của file csv chưa sạch, cụ thể là có một vài kí tự không cần thiết, kí tự đặc biệt sẽ làm ảnh hưởng không ít tới các quá trình sau này.

* **Giải pháp:** 

