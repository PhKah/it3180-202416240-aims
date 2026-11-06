# Changelog

Tất cả các thay đổi đáng chú ý của dự án AIMS-mini sẽ được ghi nhận tại đây.
Định dạng tuân thủ [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
và dự án tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-11-07
### Added
- Phương thức in chi tiết giỏ hàng (`Cart.print_cart()`).
- Tìm kiếm đĩa theo tiêu đề (`search_by_title()`).
- Tính toán tiền giỏ hàng khi áp dụng chiết khấu (`total_cost_with_discount()`).
- Tài liệu ca sử dụng tại `docs/use-case.md`.
- Khung kiểm thử tự động với `unittest`.
## [1.0.1] - 2026-11-07

### Fixed
- Sửa lỗi tìm kiếm đĩa không phân biệt hoa thường (`search_by_title`).
- Sửa lỗi giỏ hàng nhận đĩa thứ 21 vượt giới hạn 20 đĩa (#7).
- Sửa công thức tính chiết khấu theo phần trăm và kiểm tra ngoại lệ `ValueError`.

