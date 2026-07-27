# 🎓 Student Management System

Hệ thống Quản lý Sinh viên được xây dựng bằng **Python**, áp dụng lập trình hướng đối tượng (OOP), lưu trữ dữ liệu bằng **JSON**, ghi nhật ký hoạt động (Logging) và xuất báo cáo **Excel**.

---

# 📋 Mục lục

- Giới thiệu
- Chức năng
- Cấu trúc dự án
- Yêu cầu hệ thống
- Cài đặt
- Cách chạy chương trình
- Hướng dẫn sử dụng
- Công nghệ sử dụng
- Hình ảnh minh họa
- Hướng phát triển
- Tác giả

---

# 📖 Giới thiệu

Student Management System giúp quản lý thông tin sinh viên thông qua giao diện dòng lệnh (CLI).

Chương trình hỗ trợ:

- Quản lý sinh viên
- Tìm kiếm
- Cập nhật
- Xóa
- Thống kê
- Sắp xếp GPA
- Xuất dữ liệu Excel
- Lưu dữ liệu JSON

---

# 🚀 Chức năng

## 1. Thêm sinh viên

- Kiểm tra mã sinh viên trùng
- Kiểm tra tên hợp lệ
- Kiểm tra tuổi
- Kiểm tra ngành học
- Kiểm tra điểm (0-10)
- Lưu dữ liệu tự động

---

## 2. Hiển thị danh sách

Hiển thị toàn bộ sinh viên.

Bao gồm:

- Mã sinh viên
- Họ tên
- Tuổi
- Ngành
- Điểm Toán
- Điểm Văn
- Điểm Anh
- GPA
- Xếp loại

---

## 3. Tìm kiếm theo mã sinh viên

Cho phép tìm kiếm nhanh theo mã sinh viên.

---

## 4. Cập nhật sinh viên

Cho phép cập nhật:

- Họ tên
- Tuổi
- Ngành
- Điểm

Có kiểm tra dữ liệu trước khi lưu.

---

## 5. Xóa sinh viên

Hiển thị thông tin sinh viên trước khi xóa.

Có xác nhận:

```
Y/N
```

---

## 6. Tìm theo tên

Tìm kiếm gần đúng.

Ví dụ:

```
Nguyễn
```

---

## 7. Tìm theo ngành

Ví dụ

```
CNTT
```

---

## 8. Thống kê

Hiển thị số lượng sinh viên:

- Giỏi
- Khá
- Trung bình
- Yếu

---

## 9. Sắp xếp GPA

Sắp xếp GPA giảm dần.

---

## 10. Xuất Excel

Xuất danh sách sinh viên ra file Excel.

Ví dụ:

```
reports/students.xlsx
```

---

# 📁 Cấu trúc dự án

```
StudentManagement/
│
├── data/
│   └── students.json
│
├── logs/
│   └── app.log
│
├── models/
│   └── student.py
│
├── reports/
│   └── students.xlsx
│
├── services/
│   ├── student_service.py
│   ├── file_service.py
│   ├── report_service.py
│   └── logger_config.py
│
├── utils/
│   └── validator.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

# 💻 Yêu cầu hệ thống

- Python 3.10 trở lên

Khuyến nghị:

- Python 3.11
- VS Code

---

# ⚙️ Cài đặt

## Clone project

```bash
git clone https://github.com/yourusername/StudentManagement.git
```

Hoặc tải file ZIP và giải nén.

---

## Cài thư viện

```bash
pip install -r requirements.txt
```

Nếu chưa có file `requirements.txt`, cài:

```bash
pip install openpyxl
```

---

# ▶️ Chạy chương trình

Từ thư mục dự án:

```bash
python main.py
```

Hoặc:

```bash
python3 main.py
```

---

# 📌 Menu chương trình

```
==============================
HỆ THỐNG QUẢN LÝ SINH VIÊN
==============================

1. Thêm sinh viên
2. Hiển thị danh sách
3. Tìm kiếm sinh viên
4. Cập nhật sinh viên
5. Xóa sinh viên
6. Lưu dữ liệu
7. Đọc dữ liệu
8. Tìm theo tên
9. Tìm theo ngành
10. Thống kê
11. Sắp xếp GPA
12. Xuất Excel
0. Thoát
```

---

# 📚 Dữ liệu

Dữ liệu được lưu trong:

```
data/students.json
```

Ví dụ:

```json
{
    "student_id":"SV001",
    "name":"Nguyễn Văn A",
    "age":20,
    "major":"CNTT",
    "math":8,
    "literature":7,
    "english":9
}
```

---

# 📊 Báo cáo Excel

Sau khi xuất dữ liệu sẽ tạo:

```
reports/students.xlsx
```

---

# 📝 Nhật ký hoạt động

Chương trình ghi log vào:

```
logs/app.log
```

Ví dụ:

```
Thêm sinh viên
Cập nhật sinh viên
Xóa sinh viên
```

---

# 🛠 Công nghệ sử dụng

- Python 3
- OOP
- JSON
- Logging
- OpenPyXL
- File Handling

---

# 📈 Hướng phát triển

Trong tương lai có thể bổ sung:

- SQLite / MySQL
- Đăng nhập
- Phân quyền
- Giao diện Tkinter
- Flask/FastAPI
- REST API
- PDF Report
- CSV Export
- Dashboard
- Biểu đồ thống kê

---

# 👨‍💻 Tác giả

**Nguyen Hieu**

Student Management System

Python OOP Project

2026

---

# ⭐ Đánh giá

Dự án áp dụng:

- Lập trình hướng đối tượng (OOP)
- Kiểm tra dữ liệu đầu vào
- CRUD
- JSON
- Logging
- Excel Reporting

Phù hợp cho:

- Đồ án Python cơ bản
- Thực hành OOP
- Quản lý dữ liệu bằng File JSON
