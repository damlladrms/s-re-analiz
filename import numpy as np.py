import numpy as np

def analyze_employee_times(times):
    """
    Çalışan sürelerini analiz eden fonksiyon.
    
    Args:
        times (list of float): Çalışan süreleri (saniye veya dakika cinsinden).
        
    Returns:
        dict: Ortalama süre, standart sapma ve %10 değer kaybıyla düzenlenmiş süreler.
    """
    if not times:
        return "Zaman verileri boş."

    # Ortalama ve standart sapma hesaplama
    mean_time = np.mean(times)
    std_dev = np.std(times)

    # %10 değer kaybını ekleyerek güncellenmiş süreleri hesapla
    adjusted_times = [time * 0.9 for time in times]

    return {
        "Ortalama Süre": mean_time,
        "Standart Sapma": std_dev,
        "Düzenlenmiş Süreler (%10 kayıp)": adjusted_times
    }

# Örnek kullanım
if __name__ == "__main__":
    # Çalışanların süreleri (örnek veriler)
    employee_times = [120, 130, 125, 140, 135]  # Örneğin saniye cinsinden süreler

    # Analizi yap
    results = analyze_employee_times(employee_times)

    # Sonuçları yazdır
    print("Ortalama Süre: {:.2f}".format(results["Ortalama Süre"]))
    print("Standart Sapma: {:.2f}".format(results["Standart Sapma"]))
    print("Düzenlenmiş Süreler (%10 kayıp):", results["Düzenlenmiş Süreler (%10 kayıp)"])
