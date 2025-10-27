# Tiến trình
27/10/2025
- đang test quá trình chuyển đổi từ ảnh => latex => ảnh.
- sử dụng những file: test/test_matplotlib.py, test/test_latex_to_image.py
- thành công trong việc chuyển đổi.
- hướng đi tiếp theo: quét pdf tìm các khối, sau đó chuyển thử từng khối về latex. Nếu không chuyển được, tức là đó là văn bản và hình ảnh.
- vấn đề đang gặp: làm sao để tách pdf thành các khối?
- hướng đi tiếp theo: sử dụng thư viện pdfplumber để tách pdf thành các khối (AI đang gợi ý vậy) hoặc sử dụng công nghệ từ translater2.2.