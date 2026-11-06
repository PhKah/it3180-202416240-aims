### Câu hỏi: Merge Base là gì?
* **Merge Base** giữa hai nhánh (hoặc hai commit) $A$ và $B$ là **tổ tiên chung gần nhất (Best Common Ancestor)** của cả hai nhánh đó trong đồ thị lịch sử cam kết (DAG - Directed Acyclic Graph).
* Git sử dụng thuật toán Three-Way Merge: so sánh trạng thái của nhánh $A$, nhánh $B$ với chính điểm $Merge\ Base$ để xác định dòng nào đã được thay đổi ở bên nào, từ đó tự động hợp nhất hoặc báo Conflict nếu cả hai cùng sửa đổi một vị trí so với Merge Base.

### Câu hỏi: Vì sao trên `master` hoặc `release/*` phải dùng `revert` thay vì `reset`?
* `git reset` dời con trỏ nhánh và xóa bỏ các commit khỏi lịch sử nhánh. Nếu commit đó đã được đẩy lên remote (nhánh chia sẻ), việc dùng reset đòi hỏi phải force push (`git push --force`), điều này phá vỡ lịch sử làm việc của toàn bộ các thành viên khác.
* `git revert` không hề xóa lịch sử mà tạo ra một **commit mới** có nội dung đảo ngược lại thay đổi trước đó. Điều này bảo toàn 100% tính toàn vẹn của lịch sử SCM, cho phép truy vết lý do vì sao tính năng bị hủy bỏ và tuyệt đối an toàn khi cộng tác nhóm.
