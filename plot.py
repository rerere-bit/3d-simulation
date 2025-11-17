import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker
import glob
import os

# Cari file .log terbaru di folder logs/
log_files = glob.glob("logs/*.log")

if not log_files:
    print("❌ Tidak ada file .log ditemukan di folder 'logs/'.")
else:
    latest_log = max(log_files, key=os.path.getmtime)
    print(f"📄 Membaca file log terbaru: {latest_log}")

    try:
        # Baca file log (otomatis buang spasi di sekitar header & data)
        data = pd.read_csv(latest_log, skipinitialspace=True)
        data.columns = [col.strip() for col in data.columns]

        # Pastikan kolomnya benar
        if not {"x", "y", "z"}.issubset(data.columns):
            print(f"⚠️ Kolom tidak lengkap. Kolom yang ditemukan: {list(data.columns)}")
            exit()

        # Konversi ke float
        data = data.astype(float)

        # Batasi jumlah titik biar tidak terlalu rapat
        max_points = 2000
        if len(data) > max_points:
            data = data.iloc[::len(data)//max_points]

        # Buat figure 3D
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection="3d")

        # Plot lintasan 3D
        ax.plot(data["x"], data["y"], data["z"], color='royalblue', linewidth=1.5)

        # Label dan judul
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title(f"3D Plot dari File: {os.path.basename(latest_log)}")

        # Atur ticks agar rapi
        for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
            axis.set_major_locator(ticker.MaxNLocator(nbins=6))
            axis.set_major_formatter(plt.FuncFormatter(lambda val, _: f"{val:.2f}"))

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"❌ Terjadi error saat memproses file: {e}")
