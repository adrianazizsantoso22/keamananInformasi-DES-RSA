def main_menu():
    """Fungsi ini menampilkan menu utama untuk memilih opsi yang tersedia.
    
    Returns:
        str: Pilihan pengguna sebagai string.
    """
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Sign Message")
    print("4. Verify Signature")
    choice = input("Choose an option: ")
    return choice
