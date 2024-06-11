
---

# **XỬ LÝ DỮ LIỆU**

### **Các vấn đề gặp phải trong quá trình xử lý dữ liệu:**

**Vấn đề 1:** 

* **Mô tả lỗi:** Khi vừa mới crawl data từ web về (raw data), em gặp lỗi không thể thực hiện được lệnh `pd.read_csv`. Sau khi kiểm tra sơ lược, em phát hiện lỗi này xuất phát từ việc dư dấu (" ") trong chuỗi data, dẫn đến cấu trúc data bị sai.

* **Giải pháp:** Sử dụng hàm `fix_csv_quotes` để thực hiện chỉnh sửa các cặp dấu (" ") sao cho hợp lý.

    * Hàm `fix_csv_quotes` được phát triển để sửa lỗi dư dấu ngoặc kép trong dữ liệu CSV. Hàm hoạt động bằng cách:
        1. Đếm số lượng dấu ngoặc kép trong mỗi dòng.
        2. Xác định các trường hợp thiếu dấu ngoặc kép bằng cách kiểm tra xem số lượng dấu ngoặc kép có chẵn hay không.
        3. Bổ sung dấu ngoặc kép thiếu vào cuối các dòng có số lượng dấu ngoặc kép lẻ.
    
    * Ví dụ: 
        - Dòng dữ liệu sai lệch: "data1", "data2", "data3""
        - Dòng dữ liệu sau khi sửa: "data1", "data2", "data3"
    
    * Sau khi đã fix xong tất cả lỗi thì xuất lại file output csv.

**Vấn đề 2:** 

* **Mô tả lỗi:** Data trong các cột của file csv chưa sạch, cụ thể là có một vài kí tự không cần thiết, kí tự đặc biệt sẽ làm ảnh hưởng không ít tới các quá trình sau này.

* **Giải pháp:** 
    * Viết hàm `clean_string` để làm sạch chuỗi bằng cách loại bỏ các biểu tượng và kí tự không cần thiết. Hàm này sẽ giữ lại các kí tự chữ (hoa và thường), số, dấu chấm, dấu phẩy, dấu |.
    * Sử dụng hàm `clean_file_csv` để áp dụng hàm `clean_string` lên một cột cụ thể trong file CSV, ở đây là cột "Description".

**Vấn đề 3:** 

* **Mô tả lỗi:** Cần trích xuất dữ liệu từ các trường 'Title' và 'Description' để điền vào các vị trí bị thiếu dữ liệu.

* **Giải pháp:** Sử dụng biểu thức chính quy (regex) để trích xuất thông tin giá, diện tích, số phòng ngủ, và số nhà vệ sinh từ các trường 'Title' và 'Description'. Cụ thể, các biểu thức chính quy được sử dụng để tìm kiếm các mẫu giá, diện tích, số phòng ngủ và số nhà vệ sinh trong chuỗi văn bản và trích xuất chúng. Sau đó, các thông tin này được lưu vào các cột mới trong DataFrame.

**Vấn đề 4:** 

* **Mô tả lỗi:** Cần xử lý chi tiết hơn, tính toán và điền giá trị thiếu.

* **Giải pháp:** Chuyển đổi cột 'Price' và 'Area' sang kiểu số và tính giá trên mỗi mét vuông. Điền giá trị thiếu dựa trên giá trị trung bình của từng quận và các quy tắc tính toán hợp lý. Cụ thể, hàm `fill_miss_vals` sẽ tính toán các giá trị thiếu cho các cột 'Price' và 'Area' dựa trên các giá trị trung bình theo từng quận. Hàm `price_per_sqm` sẽ tính toán giá trên mỗi mét vuông và thêm cột này vào DataFrame.

**Vấn đề 5:** 

* **Mô tả lỗi:** Dữ liệu bị trùng lặp quá nhiều.

* **Giải pháp:** Loại bỏ các hàng trùng lặp bằng cách kiểm tra sự tương đồng của cột 'Postdate' và 'Description'. Đầu tiên, các dòng trùng lặp hoàn toàn sẽ bị loại bỏ. Sau đó, các dòng trùng lặp một phần sẽ được so sánh dựa trên độ tương đồng của 'Postdate' và 'Description', và các dòng trùng lặp này sẽ bị loại bỏ nếu chúng có mức độ tương đồng cao.

**Vấn đề 6:** 

* **Mô tả lỗi:** Bài đăng cũ có thể gây ra sự không chính xác với khung thời gian hiện tại, nên quyết định xoá các dữ liệu cũ.

* **Giải pháp:** Xoá các bài đăng bán nhà từ năm 2022. Điều này được thực hiện bằng cách chuyển đổi cột 'Postdate' sang kiểu datetime và lọc ra các hàng có năm đăng tin là 2022.

**Vấn đề 7:** 

* **Mô tả lỗi:** Một số dữ liệu không hợp lý, cần phải loại bỏ các giá trị không hợp lý này.

* **Giải pháp:** Loại bỏ các giá trị không hợp lý bằng cách kiểm tra giá trị 'Price_per_sqm'. Các hàng có giá trị 'Price_per_sqm' không nằm trong khoảng hợp lý sẽ bị loại bỏ. Sau đó, điều chỉnh giá trị cho hợp lý hơn dựa trên khu vực. Hàm `adjust_price` sẽ điều chỉnh giá trị của cột 'Price' dựa trên khu vực và giá trên mỗi mét vuông.

**Vấn đề 8:** 

* **Mô tả lỗi:** Giá nhà không hợp lý ở một số khu vực.

* **Giải pháp:** Điều chỉnh giá trị cho hợp lý hơn. Hàm `adjust_price` được sử dụng để điều chỉnh giá trị của cột 'Price' dựa trên khu vực và giá trên mỗi mét vuông.

Sau khi hoàn tất các bước xử lý dữ liệu, chúng tôi đã lưu lại DataFrame vào file CSV:

- Tạo lại cột 'No' để dễ quan sát hơn.
- Lưu dữ liệu vào file output CSV.
- Kiểm tra các giá trị thiếu trong DataFrame để đảm bảo không còn lỗi.

---

