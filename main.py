"""
Aplikasi deteksi gempa terkini
modularisasi dengan fungsion
"""

def ekstraksi_data():
    """
    tanggal: 12 Desember 2024, 13:36:29 WIB
    magnitudo: 4.9
    kedalman: 10 km
    lokasi: 0.36 LS - 99.51 BT
    keterangan: Pusat gempa berada di laut 57 km barat daya Lubukbasung-Agam
    Dirasakan (Skala MMI): III-IV Padang, III-IV Agam, III-IV Padang Pariaman, III-IV Pariaman, II - III Padang Panjang, II - III Bukittinggi
    :return:
    """

    hasil = dict()
    hasil['tanggal'] = '12 desember 2024'
    hasil['waktu'] = '13:36:29 WIB'
    hasil['lokasi'] = {'ls': 0.36, 'bt': 99.51}
    hasil['pusat'] = 'Pusat gempa berada di laut 57 km barat daya Lubukbasung-Agam'
    hasil['dirasakan'] = '(Skala MMI): III-IV Padang, III-IV Agam, III-IV Padang Pariaman, III-IV Pariaman, II - III Padang Panjang, II - III Bukittinggi'

    return hasil


def ekstrasi_data(result):
    print('gempa terakhir berdasarkan bmkg')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"lokasi: ls={result['lokasi']['ls']}, bt={result['lokasi']['bt']}")
    print(f"pusat {result['pusat']}")
    print(f"dirasakan {result['dirasakan']}")


def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")


if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
