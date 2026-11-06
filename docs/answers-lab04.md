### Câu hỏi: Vì sao nhánh `release/*` không merge ngược vào `master`? So sánh với GitFlow?
* Trong Release Flow: Nhánh release chỉ đóng vai trò là một "đường ống ổn định" (stabilization branch) và đóng băng baseline. Nhánh release xuất phát từ `master` nên `master` vốn dĩ đã chứa toàn bộ tính năng. Bất kỳ sửa lỗi nào trên release đều được chuyển có chọn lọc sang master thông qua `cherry-pick`, giúp master luôn sạch và không bị kéo theo các commit rác chỉ dành riêng cho đóng gói phát hành.
* So với GitFlow: GitFlow duy trì 2 nhánh vô hạn (`main` và `develop`). Trong GitFlow, nhánh `release` bắt buộc phải merge ngược vào cả `main` và `develop`. Điều này khiến cấu trúc đồ thị commit của GitFlow phức tạp hơn rất nhiều ("merge hell"), khó theo dõi hơn và không phù hợp với các chu kỳ phát hành nhanh, liên tục.

### Câu hỏi: Vì sao phiên bản này nhảy lên `1.0.0` mà không phải `0.4.0`?
* Theo chuẩn **Semantic Versioning (SemVer)**:
  * Nhánh `0.y.z` là giai đoạn phát triển ban đầu (Initial Development), phần mềm chưa hoàn thiện, API chưa ổn định.
  * Khi phần mềm đã đạt được bộ tính năng hoàn chỉnh đầu tiên theo đặc tả yêu cầu, vượt qua toàn bộ các kiểm thử nghiệm thu và sẵn sàng bàn giao cho người dùng cuối (ở Lab 04), dự án chính thức xác lập phiên bản sản xuất đầu tiên là `1.0.0`.