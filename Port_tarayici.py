#! usr/bin python
# -*-  coding:UTF-8 -*-

import socket
from datetime import datetime
import sys
from timeit import default_timer

giris="""

 *** port tarama uygulamasına hoş geldiniz
 *** Lütfen uygun seçeneği seçiniz


"""
print(giris)


def port_tara(hedef,smask):
    baslangic_zamani = datetime.now()
    port = port_sor()
    for a in range(1,smask):
      ip=hedef[0]+"."+hedef[1]+"."+hedef[2]+"."+str(a)


      hedef_ip=socket.gethostbyname(ip)
      #hedef_ip=ip
      banner_ekle(ip)

      try:

        #baslangic_zamani = default_timer()

        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1.2)

        '''sure2=default_timer()-baslangic_zamani
         if sure2 <5:
           bs2=default_timer()'''
           #sonuc=sock.connect_ex((hedef_ip,port))
        sonuc=sock.connect_ex((hedef_ip,port))

        '''sure=default_timer()-bs2
           if sure>5:
                sock.close()
           else :
                if sonuc!=None:

                  print("Port {} açık ".format(port))
                  sock.close()
        else:'''
        if sonuc==0 :
             dosya_yaz(hedef_ip,port)
             print("Port {} açık ".format(port))
             sock.close()

      except KeyboardInterrupt:
        print("CTRL+C'ye bastınız")
        sys.exit()
      except socket.gaierror:
           print("hostname çözümlenemedi")
           sys.exit()
      except socket.error:
        print("hedef ip'ye bağlanamadı")
        sys.exit()

    bitis_zamani=datetime.now()
    toplam_sure=bitis_zamani-baslangic_zamani
    print(str(toplam_sure) +"surede tamamlandi")







def banner_ekle(ip):
    print("*"*60)
    print('Lutfen bekleyiniz. Taranan ip : ',ip)
    print("*"*60)


def port_sor():
    port_ekrani= """
    1- FTP
    2- SSH
    3- TELNET
    4- HTTP
    5-NETBIOS
    6-HTTPS
    7-WINDOWS PAYLASIM
    8-MSSQL
    9-ORACLE
    10-MYSQL

    """
    print(port_ekrani)
    pn=0
    portlar={"1":"21","2":"22","3":"23","4":"80","5":"137","6":"443","7":"445","8":"1433","9":"1521","10":"3306"}
    port_no=raw_input("lütfen servisi seciniz :\t")
    pn=int(portlar[port_no])
    return pn


def dosya_yaz(ip,port):
    with open("rapor.txt","r+") as dosya:
        okunan=dosya.read()
        dosya.seek(0)

        dosya.write(okunan + "\n" +str(ip)+":"+str(port))

ipp=raw_input("Lütfen taranacak networkü giriniz / 192.168.1.0 şeklinde \t: ")
ipp_ayrilmis=ipp.split(".")

subnet_mask=raw_input("lutfen subnet nask giriniz  .. 8/24/32 \t :")
if subnet_mask=="/24" or "24":

    smask=255
    port_tara(ipp_ayrilmis,smask)

