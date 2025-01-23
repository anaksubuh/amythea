import os

def generate_photo_list(folder_path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            folder_name = os.path.basename(root)
            if files:  # Hanya tulis nama folder jika ada file di dalamnya
                namafolder = (f"{{{folder_name}}}\n")
                file.write(
f'''
<section class="section__container portfolio__container" id="portfolio">
    <h2 class="section__header">{namafolder}</h2>
    <p class="section__description">
    DESKRIPSI
    </p>
    <div class="portfolio__grid">
'''
                )
                for photo in files:
                    if photo.lower().endswith(('jpg', 'jpeg', 'png', 'heic', 'bmp', 'gif')):
                        namafoto = (f"{photo}")
                        file.write(
f'''
    <div class="portfolio__card">
        <img src="{namafolder}\{namafoto}" alt="portfolio" />
    </div>
'''
                        )

                file.write(
f'''
    </div>
    </div>
</section>
<section class="section__container portfolio__container" id="portfolio">
                '''
                )


# Path folder utama tempat foto disimpan
folder_path = "E:\\amythea\\assets"  # Ganti dengan path folder kamu

# Nama file output untuk menyimpan hasil
output_file = "namafoto.txt"

generate_photo_list(folder_path, output_file)

print(f"Daftar foto berhasil disimpan di {output_file}!")
