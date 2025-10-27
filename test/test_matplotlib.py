import matplotlib.pyplot as plt
import os

# Công thức LaTeX muốn render
formula = r"S=\int_{x}\left\{\frac{1}{2}\sum_{a}\partial^{\mu}\chi_{a}\partial_{\mu}\chi_{a}+V(\rho)\right\}"

try:
    # Tạo thư mục output nếu chưa tồn tại
    os.makedirs("test/output", exist_ok=True)
    # Tạo canvas
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.text(0.05, 0.5, f"${formula}$", fontsize=22, va='center')
    
    # Ẩn trục
    ax.axis('off')
    
    # Lưu ra file PNG độ phân giải cao
    plt.savefig("test/output/formula.png", dpi=300, bbox_inches='tight', pad_inches=0.2)
    plt.close()
    print("Đã tạo file formula.png thành công!")
except Exception as e:
    print(f"Lỗi khi render công thức LaTeX: {e}")
    print(f"Công thức: {formula}")
