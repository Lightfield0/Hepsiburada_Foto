# Hepsiburada Ürün Fotoğrafları Çekici

Bu proje, Hepsiburada'daki ürünlerin fotoğraflarını çekmek için bir Selenium web scraper'dır. 

## Nasıl Çalışır

- Chrome'u otomasyon için yapılandırır ve undetected modda başlatır. 
- Hepsiburada'dan ilgili kategorideki ürün linklerini toplar.
- Her ürün linkine girer ve yorumlar sekmesini açar.
- Ürün fotoğraflarının URL'lerini çeker.
- Problemli URL'ler için redirect parametresini parse eder ve orijinal URL'ye ulaşmaya çalışır.
- Çekilen tüm fotoğraf URL'lerini ekrana yazdırır.

## Gereklilikler

- Python 3
- Selenium
- BeautifulSoup
- Undetected Chromedriver

## Kurulum

- `pip install selenium bs4` ile gerekli kütüphaneleri yükleyin.
- `chromedriver.exe` dosyasını projeye ekleyin.

## Kullanım

`python main.py` ile çalıştırın.

## Geliştirici Notları

- Fotoğraf URL'lerini bir CSV dosyasına da yazdırabilirsiniz.
- Farklı ürün kategorileri için URL'yi değiştirebilirsiniz.
- Tespitten kaçınmak için bekleme sürelerini arttırın, scroll ve bekleme ekleyin.

## Lisans

MIT
