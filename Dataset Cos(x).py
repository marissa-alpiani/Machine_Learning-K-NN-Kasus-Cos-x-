import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan dataset dari fungsi cos x
def generate_cos_dataset(start, end, num_points):
    x_values = np.linspace(start, end, num_points)
    y_values = np.cos(x_values)
    return x_values, y_values

# Simpan dataset ke dalam file txt dengan keterangan koordinat
def save_dataset_to_txt(x_values, y_values, filename):
    with open(filename, 'w') as file:
        file.write("x\tcos(x)\n")  # Menambahkan header dengan keterangan kolom
        for x, y in zip(x_values, y_values):
            file.write(f"{x}\t{y}\n")

# Parameter untuk fungsi cos x
start = 0
end = 2 * np.pi
num_points = 30

# Generate dataset
x_values, y_values = generate_cos_dataset(start, end, num_points)

# Simpan dataset ke dalam file txt
filename = 'cos_dataset.txt'
save_dataset_to_txt(x_values, y_values, filename)

# Tampilkan nilai x dan cos(x) ke konsol dengan label di atas
print(f"{'x':<10} {'cos(x)':<10}")
for x, y in zip(x_values, y_values):
    print(f"{x:<10.4f} {y:<10.4f}")

print(f"\nDataset dengan keterangan koordinat telah disimpan dalam file {filename}.")
