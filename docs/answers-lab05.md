### Câu hỏi: Ưu, nhược điểm của "Upstream First" so với "Release First"?
* **Upstream First** (sửa trên `master` trước rồi cherry-pick về các nhánh `release`):
  * *Ưu điểm*: Đảm bảo không bao giờ bị quên sửa trên nhánh chính; mã nguồn mới nhất luôn luôn có bản sửa; quy trình phát triển tập trung tại một nơi.
  * *Nhược điểm*: Bản sửa lỗi trên `master` có thể sử dụng các hàm/cấu trúc mới mà nhánh release cũ không có, dẫn đến việc cherry-pick về release cũ dễ gặp xung đột hoặc lỗi tương thích ngược.
* **Release First** (sửa trên nhánh `release` cũ trước rồi cherry-pick lên `master`):
  * *Ưu điểm*: Đảm bảo bản vá tương thích 100% với môi trường tối giản của phiên bản đang chạy thực tế mà khách hàng gặp lỗi; phát hành bản vá tới tay người dùng nhanh nhất.
  * *Nhược điểm*: Nếu không có quy trình kiểm soát chặt chẽ, lập trình viên có thể quên lan truyền bản vá ngược về `master`, khiến lỗi bị tái phát trong các phiên bản tương lai (*regression*).

### Câu hỏi: Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
* **Lệnh 1**: `git cherry -v origin/master origin/release/lab05` hoặc so sánh với `origin/release/lab04`. Lệnh này liệt kê các commit chưa được tích hợp chéo.
* **Lệnh 2**: Đoạn script kiểm tra tự động chạy trên cả 3 nhánh/tag:
  ```bash
  for ref in v1.0.1 v1.1.0 master; do
      git switch --detach -q $ref
      # chạy test tìm kiếm
  done
  ```
  Nếu nhánh nào quên nhận bản vá, bài kiểm thử của nhánh đó sẽ trả về kết quả rỗng `[]` thay vì tìm thấy `1` đĩa phim, qua đó chỉ ra chính xác nhánh bị bỏ sót.

