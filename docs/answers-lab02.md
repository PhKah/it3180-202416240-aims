### Câu hỏi: Vì sao phải đồng bộ `master` trước khi gửi Pull Request?
* Trong quá trình phát triển nhánh tính năng, nhánh `master` có thể đã nhận thêm nhiều commit mới từ các thành viên khác.
* Nếu không đồng bộ `master` về nhánh tính năng (`git merge origin/master`), dev sẽ không thể biết mã của mình có tương thích hoặc gây xung đột với mã mới nhất hay không.
* Đồng bộ trước giúp phát hiện và giải quyết xung đột cục bộ ngay trên máy lập trình viên, đảm bảo Pull Request khi mở ra ở trạng thái an toàn, chạy qua toàn bộ test tích hợp và sẵn sàng merge sạch sẽ (*clean merge*).

### Câu hỏi: Khi nào không được dùng `rebase`?
* Không bao giờ rebase một nhánh đã chia sẻ công khai hoặc nhánh có nhiều người cùng làm việc (như `master`, `main`, `dev`, `release/*`).
* `rebase` sẽ viết lại lịch sử bằng cách tạo ra các mã băm commit (SHA) hoàn toàn mới. Nếu người khác đang làm việc dựa trên các commit cũ, việc rebase và force push sẽ gây xáo trộn nghiêm trọng lịch sử commit và dẫn đến lỗi phân kỳ dữ liệu phức tạp.

### Câu hỏi: Nhánh `feature/*` khác nhánh `topic/*` ra sao?
* `feature/*`: Dành riêng cho việc xây dựng một chức năng hoặc đặc tính mới của phần mềm (ví dụ: thêm tính năng in giỏ hàng `feature/cart-print`, tìm kiếm `feature/search-by-title`). Các nhánh này thường có phạm vi ảnh hưởng tới mã nguồn logic nghiệp vụ và cần kiểm thử chặt chẽ.
* `topic/*`: Dành cho các công việc có tính chất chủ đề cụ thể, ngắn hạn, thường không phải là tính năng người dùng cuối (ví dụ: thêm cấu hình PR template `topic/pr-template`, cập nhật sơ đồ use case `topic/use-case-diagram`, thiết lập CI `topic/ci-unit-tests`).