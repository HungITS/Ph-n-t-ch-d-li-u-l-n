import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc file CSV
file_path = 'dataset.csv'  # Đặt đúng đường dẫn file dataset của bạn
data = pd.read_csv(file_path)

# Phân tích dữ liệu chữ
print("### Phân tích dữ liệu chữ ###")
categorical_summary = {}
skip_columns = ['DiaChi', 'TenPhanKhu', 'DacDiem']

for column in data.select_dtypes(include=['object', 'category']):
    counts = data[column].value_counts()
    categorical_summary[column] = counts
    print(f"\nBiến: {column}")
    print(counts)

    if column in skip_columns:
        print(f"Không vẽ biểu đồ cho biến: {column}")
        continue

    # Vẽ biểu đồ và lưu file ảnh
    plt.figure(figsize=(10, 6))
    sns.countplot(y=data[column], order=counts.index, color='blue')
    plt.title(f'Biểu đồ cho biến {column}')
    plt.xlabel('Tần số')
    plt.ylabel(column)
    plt.tight_layout()
    plt.savefig(f'{column}_category_plot.png')
    plt.show()
    plt.close()
    print(f"Đã lưu biểu đồ của {column} vào file '{column}_category_plot.png'.")

# Xuất kết quả phân tích dữ liệu chữ vào file
with open('categorical_summary.txt', 'w', encoding='utf-8') as f:
    for key, value in categorical_summary.items():
        f.write(f"Biến: {key}\n{value.to_string()}\n\n")

# Phân tích dữ liệu số
print("\n### Phân tích dữ liệu số ###")
numerical_summary = {}

for column in data.select_dtypes(include=['number']):
    stats = data[column].describe()
    numerical_summary[column] = stats
    print(f"\nBiến: {column}")
    print(stats)

    # Vẽ biểu đồ và lưu file ảnh
    if not data[column].dropna().empty:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column].dropna(), kde=True, bins=30, color='blue')
        plt.title(f'Histogram của {column}')
        plt.xlabel(column)
        plt.ylabel('Tần số')
        plt.tight_layout()
        plt.savefig(f'{column}_histogram.png')
        plt.show()
        plt.close()
        print(f"Đã lưu biểu đồ của {column} vào file '{column}_histogram.png'.")

# Xuất kết quả phân tích dữ liệu số vào file
with open('numerical_summary.txt', 'w', encoding='utf-8') as f:
    for key, value in numerical_summary.items():
        f.write(f"Biến: {key}\n{value.to_string()}\n\n")

print("Phân tích dữ liệu hoàn tất.")
