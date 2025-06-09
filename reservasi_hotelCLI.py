import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox
)
from abc import ABC, abstractmethod

# Kelas abstrak Kamar
class Kamar(ABC):
    def __init__(self, nama_pelanggan, jumlah_malam):
        self._nama = nama_pelanggan
        self._malam = jumlah_malam

    def get_nama(self):
        return self._nama

    def get_malam(self):
        return self._malam

    @abstractmethod
    def hitung_total(self):
        pass

# Kamar Standard
class KamarStandard(Kamar):
    def hitung_total(self):
        return 300000 * self.get_malam()

# Kamar VIP
class KamarVIP(Kamar):
    def hitung_total(self):
        tarif = 700000 * self.get_malam()
        if self.get_malam() > 3:
            tarif *= 0.85  # Diskon 15%
        return tarif

# GUI untuk Reservasi Hotel
class ReservasiHotel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reservasi Hotel")
        self.init_ui()

    def init_ui(self):
        # Label dan input nama
        self.label_nama = QLabel("Nama Pelanggan:")
        self.input_nama = QLineEdit()

        # Label dan input jumlah malam
        self.label_malam = QLabel("Jumlah Malam:")
        self.input_malam = QLineEdit()

        # Pilihan tipe kamar
        self.label_kamar = QLabel("Tipe Kamar:")
        self.combo_kamar = QComboBox()
        self.combo_kamar.addItems(["Standard", "VIP"])

        # Tombol hitung
        self.btn_hitung = QPushButton("Hitung Total")
        self.btn_hitung.clicked.connect(self.hitung_total)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_nama)
        layout.addWidget(self.input_nama)
        layout.addWidget(self.label_malam)
        layout.addWidget(self.input_malam)
        layout.addWidget(self.label_kamar)
        layout.addWidget(self.combo_kamar)
        layout.addWidget(self.btn_hitung)

        self.setLayout(layout)

    def hitung_total(self):
        nama = self.input_nama.text()
        try:
            malam = int(self.input_malam.text())
            if malam <= 0:
                raise ValueError

            tipe = self.combo_kamar.currentText()
            if tipe == "Standard":
                kamar = KamarStandard(nama, malam)
            else:
                kamar = KamarVIP(nama, malam)

            total = kamar.hitung_total()
            QMessageBox.information(self, "Total Biaya", f"Total biaya untuk {nama} adalah Rp {total:,.0f}")
        except ValueError:
            QMessageBox.warning(self, "Input Salah", "Masukkan jumlah malam yang valid!")

# Main aplikasi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservasiHotel()
    window.show()
    sys.exit(app.exec_())
