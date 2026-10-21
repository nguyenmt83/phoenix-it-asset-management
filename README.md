# HỆ THỐNG QUẢN LÝ THIẾT BỊ CNTT - PHOENIX GOLF RESORT
**IT Asset Management - Cloud Pro Edition v3.5**

---

## 📌 1. NGUỒN GỐC & LỊCH SỬ DỰ ÁN
* **Đơn vị phát triển/vận hành:** Bộ phận Công nghệ Thông tin - Công ty TNHH Phoenix Golf Resort (Lương Sơn, Hòa Bình).
* **Nguồn gốc tìm kiếm:** Được truy vết chính xác từ lịch sử phiên làm việc của Google Gemini / Antigravity (Conversation ID: `8c1d47a6-80b7-4a43-91fb-ce0420606539` - *Rà Soát Ứng Dụng Và CSDL*), định vị vị trí lưu trữ gốc tại `D:\PHOENIX\Ha_Tang_Mang_Va_Server\Ung Dung Quan Ly Thiet Bi CNTT` và đồng bộ đầy đủ về thư mục làm việc hiện tại: `D:\PHOENIX\Quản ly Thiet Bi`.

---

## 📂 2. CẤU TRÚC THƯ MỤC DỰ ÁN

```text
D:\PHOENIX\Quản ly Thiet Bi\
│
├── index.html                                 # Giao diện ứng dụng chính (Single Page App - Cloud Pro)
├── START_APP.bat                              # File kích hoạt chạy nhanh ứng dụng trên trình duyệt
│
├── .html\
│   └── ng_d_ng_qu_n_l_thi_t_b_cntt.html       # Bản gốc file ứng dụng HTML
│
├── Backup_database\                           # Toàn bộ bản sao lưu cơ sở dữ liệu định kỳ JSON
│   ├── Database_Backup_PHOENIX_20260817_1249.json
│   ├── Database_Backup_PHOENIX_20260817_1706.json
│   ├── Database_Backup_PHOENIX_20260818_1608.json
│   ├── Database_Backup_PHOENIX_20260819_0800.json
│   ├── Database_Backup_PHOENIX_20260820_0800.json
│   ├── Database_Backup_PHOENIX_20260821_0954.json
│   ├── Database_Backup_PHOENIX_20260822_1648.json
│   ├── Database_Backup_PHOENIX_20260823_0800.json
│   ├── Database_Backup_PHOENIX_20260824_0800.json
│   ├── Database_Backup_PHOENIX_20260914_1435.json
│   ├── Database_Backup_PHOENIX_20260915_1559.json
│   └── Database_Backup_PHOENIX_20260920_1619.json  # Bản sao lưu mới nhất (20/09/2026)
│
├── Database\                                  # Dữ liệu khởi tạo & schema ban đầu
│   ├── Backup_Data_PHOENIX_2026-08-15.json
│   └── Backup_Data_PHOENIX_2026-08-15 (17h00).json
│
├── Tai lieu\
│   └── Hướng Dẫn Quản Lý Thiết Bị CNTT.pdf    # Tài liệu hướng dẫn sử dụng phần mềm
│
├── BaoCao_TaiSan_CNTT_PHOENIX_1786784037630.pdf # Báo cáo tài sản xuất mẫu
├── BaoCao_TaiSan_CNTT_PHOENIX_1786785875176.pdf # Báo cáo tài sản xuất mẫu
└── BG-20260815-555.pdf                        # Biên bản bàn giao thiết bị mẫu
```

---

## ⚡ 3. HƯỚNG DẪN KHỞI CHẠY & SỬ DỤNG
1. **Khởi chạy ứng dụng:**
   - Cách 1: Nhấp đúp chuột vào file `START_APP.bat`.
   - Cách 2: Mở trực tiếp file [index.html](file:///D:/PHOENIX/Qu%E1%BA%A3n%20ly%20Thiet%20Bi/index.html) bằng bất kỳ trình duyệt web nào (Google Chrome, Microsoft Edge, Firefox, Cốc Cốc).
2. **Cơ chế hoạt động:**
   - **Frontend:** HTML5, Tailwind CSS, FontAwesome Icons, Chart.js, SheetJS, jsPDF.
   - **Database Live:** Kết nối trực tuyến với Google Firebase Firestore (đồng bộ dữ liệu đám mây thời gian thực).
   - **Chức năng:** Quản lý danh mục thiết bị, phân loại khu vực/phòng ban, theo dõi trạng thái bảo hành/bảo trì, in biên bản bàn giao, xuất báo cáo Excel & PDF chuẩn hóa cho Phoenix Golf Resort.
