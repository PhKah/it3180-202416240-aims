### Câu hỏi: Vì sao phải dùng `git mv`?
* Khi dùng lệnh di chuyển thông thường của hệ điều hành (`mv`), Git ban đầu chỉ nhận diện là: tệp cũ bị xóa (`deleted`) và một tệp hoàn toàn mới được tạo ra (`untracked`).
* Sử dụng `git mv` giúp Git lập tức ghi nhận thao tác di chuyển/đổi tên trong Staging Area (`renamed`). Quan trọng nhất, điều này đảm bảo lịch sử cam kết (commit history) và truy vết thay đổi (`git log --follow`) của tệp được liên tục và không bị đứt đoạn.

### Câu hỏi: `release/lab01` có phải là một baseline không?
* **Có**. Nhánh `release/lab01` đóng băng toàn bộ trạng thái mã nguồn và tài liệu của Lab 01 tại thời điểm nộp bài. Bất kỳ thay đổi tiếp theo trên nhánh `master` sẽ không được tự tiện đưa vào `release/lab01`.

### Câu hỏi: Vì sao không commit thẳng lên `master` dù chỉ làm việc một mình?
* Đảm bảo nhánh chính luôn được bảo vệ nghiêm ngặt.
* Việc tạo nhánh và mở Pull Request giúp tự nhìn lại toàn bộ thay đổi qua tab *Files changed*, phát hiện các tệp rác hoặc thay đổi ngoài ý muốn.
* Pull Request kích hoạt các quy trình CI tự động trước khi mã nguồn được hòa vào nhánh chính.
* Tránh rủi ro làm hỏng phiên bản ổn định khi đang thử nghiệm.