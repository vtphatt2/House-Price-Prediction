

# **DATA PREPROCESSING**

### **Errors encountered during data processing:**

Các dòng data bị lỗi: 564, 1308, 1404, 1435, 1594, 1660, 1701, 1713, 1731, 1824,
1. * **Mô tả lỗi:** Khi vừa mới crawl data từ web về (raw data), em gặp lỗi không thể thực hiện được lệnh `pd.read_csv`. Sau khi kiểm tra sơ lược, em phát hiện lỗi này xuất phát từ việc dư dấu " " trong chuỗi data, dẫn đến cấu trúc data bị sai.
    * **Giải pháp:** Sửa trực tiếp bằng cách xoá các cặp dấu " " dư thừa. Đây là một biện pháp tạm thời trước khi tìm ra được phương pháp tối ưu hơn. 