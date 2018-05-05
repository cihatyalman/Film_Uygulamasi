import sys
import requests
import urllib
from _datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets,QtCore,QtGui

sozluk=dict()

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setObjectName("Form")
        self.resize(920, 620)
        self.setMinimumSize(QtCore.QSize(920, 620))
        self.setMaximumSize(QtCore.QSize(920, 620))
        self.film_listesi = QtWidgets.QListWidget(self)
        self.film_listesi.setGeometry(QtCore.QRect(20, 50, 256, 531))
        self.film_listesi.setObjectName("film_listesi")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(360, 50, 551, 531))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.genel_h_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.genel_h_layout.setContentsMargins(0, 0, 0, 0)
        self.genel_h_layout.setObjectName("genel_h_layout")
        self.film_bilgi_v_layout = QtWidgets.QVBoxLayout()
        self.film_bilgi_v_layout.setObjectName("film_bilgi_v_layout")
        self.film_adi = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.film_adi.setObjectName("film_adi")
        self.film_bilgi_v_layout.addWidget(self.film_adi)
        self.film_yonetmen = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.film_yonetmen.setObjectName("film_yonetmen")
        self.film_bilgi_v_layout.addWidget(self.film_yonetmen)
        self.film_yapim = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.film_yapim.setObjectName("film_yapim")
        self.film_bilgi_v_layout.addWidget(self.film_yapim)
        self.film_puan = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.film_puan.setObjectName("film_puan")
        self.film_bilgi_v_layout.addWidget(self.film_puan)
        self.film_tur = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.film_tur.setObjectName("film_tur")
        self.film_bilgi_v_layout.addWidget(self.film_tur)
        self.film_dili = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.film_dili.setObjectName("film_dili")
        self.film_bilgi_v_layout.addWidget(self.film_dili)
        self.film_kategori = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.film_kategori.setObjectName("film_kategori")
        self.film_bilgi_v_layout.addWidget(self.film_kategori)
        self.genel_h_layout.addLayout(self.film_bilgi_v_layout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.genel_h_layout.addItem(spacerItem)
        self.film_bilgi_2_v_layout = QtWidgets.QVBoxLayout()
        self.film_bilgi_2_v_layout.setObjectName("film_bilgi_2_v_layout")
        self.film_resmi = QtWidgets.QLabel(self)
        self.film_resmi.setObjectName("film_resmi")
        self.film_bilgi_2_v_layout.addWidget(self.film_resmi)
        self.film_konu = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.film_konu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.film_konu.setObjectName("film_konu")
        self.film_konu.setFontPointSize(10)
        self.film_bilgi_2_v_layout.addWidget(self.film_konu)
        self.genel_h_layout.addLayout(self.film_bilgi_2_v_layout)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(755, 590, 161, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(280, 50, 71, 531))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(15, 10, 261, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buton_guncel = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.buton_guncel.setObjectName("buton_guncel")
        self.horizontalLayout.addWidget(self.buton_guncel)
        self.tarih = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.tarih.setEnabled(False)
        self.tarih.setObjectName("tarih")
        self.horizontalLayout.addWidget(self.tarih)
        self.tire = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.tire.setEnabled(False)
        self.tire.setObjectName("tire")
        self.tire.setText("-")
        self.horizontalLayout.addWidget(self.tire)
        self.saat = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.saat.setEnabled(False)
        self.saat.setObjectName("saat")
        self.horizontalLayout.addWidget(self.saat)
        self.buton_bilgi_goster = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.buton_bilgi_goster.setObjectName("buton_bilgi_goster")
        self.horizontalLayout.addWidget(self.buton_bilgi_goster)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.ui()     
        self.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Film Listesi"))
        self.film_adi.setText(_translate("Form", ""))
        self.film_yonetmen.setText(_translate("Form", ""))
        self.film_yapim.setText(_translate("Form", ""))
        self.film_puan.setText(_translate("Form", ""))
        self.film_tur.setText(_translate("Form", ""))
        self.film_dili.setText(_translate("Form", ""))
        self.film_kategori.setText(_translate("Form", ""))
        self.label_8.setText(_translate("Form", "Programmer Cihat Yalman"))
        self.label.setText(_translate("Form", "Film İsmi : "))
        self.label_2.setText(_translate("Form", "Yönetmen : "))
        self.label_3.setText(_translate("Form", "Yapım Yılı : "))
        self.label_4.setText(_translate("Form", "IMDB Puanı :"))
        self.label_5.setText(_translate("Form", "Tür : "))
        self.label_6.setText(_translate("Form", "Dil : "))
        self.label_7.setText(_translate("Form", "Kategori : "))
        self.buton_guncel.setText(_translate("Form", "Güncelle"))
        self.tarih.setText(_translate("Form", "13.03.2018"))
        self.buton_bilgi_goster.setText(_translate("Form", "Bigileri Göster"))

    def ui(self):
        self.film_cek()
        self.buton_guncel.clicked.connect(self.film_cek)
        self.buton_bilgi_goster.clicked.connect(self.film_bilgileri_cek)

    def film_cek(self):
        sozluk.clear()
        url = "https://www.fullhdfilmizlesene.org/"
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            gelen_veri = soup.find_all("div", {"class": "index-orta"})
            su_an=datetime.now()
            tarih=su_an.day,su_an.month,su_an.year                                      # tarih bilgisini aldık
            saat=su_an.hour,su_an.minute,su_an.second                                   # saat bilgisini aldık
            self.tarih.setText(str(tarih[0])+"."+str(tarih[1])+"."+str(tarih[2]))
            self.saat.setText(str(saat[0])+":"+str(saat[1])+":"+str(saat[2]))
            filmtablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents) - 2]
            filmtablosu = filmtablosu.find_all("li")
            self.film_listesi.clear()
            for film in filmtablosu:
                filmbas = film.find_all("a", {"class": "title"})
                filmurl = film.find_all("a", {"class": "izle-btn"})
                filmismi = filmbas[0].text                              # film isimlerini aldık
                filmlink = filmurl[0]["href"]                           # film url'lerini aldık
                sozluk[str(filmismi)]=str(filmlink)                     # sozluk'e kaydettik
                self.film_listesi.addItem(filmismi)                     # listeye yazdırdık
            self.film_listesi.setCurrentRow(0)                          # 0.indisi sec komutu verdik
            self.film_bilgileri_cek()                                   # fonk. çalıştırdık
        except(requests.exceptions.ConnectionError):
            self.film_listesi.addItem("Hata: Internet Bağlantınızı Kontrol Edin")

    def film_bilgileri_cek(self):
        try:
            secili_film=self.film_listesi.currentItem().text()          # seçili filmin ismini aldık (key için)
            url = sozluk[secili_film]                                   # isme (key) göre url aldık
            r=requests.get(url)
            soup = BeautifulSoup(r.content,"html.parser")
            gelen_veri = soup.find_all("div",{"class":"single-afis"})
            gelen_veri_2 = soup.find_all("div",{"class":"single-film-bilgileri"})
            film_ismi=(((gelen_veri[0].contents)[1]).find_all("a"))[0]["title"]
            film_resmi=gelen_veri[0].contents[5].contents[1]["data-src"]
            film_konu=gelen_veri_2[0].contents[3].contents[1].text
            #film_konu=gelen_veri_2[0].find_all("div",{"class":"film-ozeti"})[0].text
            film_detay=gelen_veri[0].find_all("div",{"class":"filmdetay"})[0].find_all("li")
            film_yonetmen=film_detay[0].find_all("span")[2].text
            film_yil=film_detay[1].find_all("a")[0].text
            film_puan=film_detay[2].find_all("span")[2].text
            film_tur=film_detay[3].find_all("a")[0].text
            film_dil=film_detay[5].find_all("a")[0].text
            film_kategori=film_detay[6].find_all("a")[0].text
        except(requests.exceptions.ConnectionError):
            self.film_adi.setText("Hata : Internet Bağlantınızı Kontrol Ediniz")

        self.film_adi.setText(film_ismi)
        self.film_yonetmen.setText(film_yonetmen)
        self.film_yapim.setText(film_yil)
        self.film_puan.setText(film_puan)
        self.film_tur.setText(film_tur)
        self.film_dili.setText(film_dil)
        self.film_kategori.setText(film_kategori)
        self.film_konu.setText(film_konu)
        data = urllib.request.urlopen(film_resmi).read()        # url'de bulunan resmi açıp okuduk
        image = QtGui.QImage()                                  # Image formatı oluşturduk
        image.loadFromData(data)                                # Image'e ekledik
        self.film_resmi.setPixmap(QtGui.QPixmap(image))         # Resmimizi Label'a yazdırdık

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
