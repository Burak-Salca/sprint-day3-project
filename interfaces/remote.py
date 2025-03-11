from abc import abstractmethod

class remoteMethods():
    @abstractmethod
    def tv_ac(self):
        pass

    @abstractmethod
    def tv_kapat(self):
        pass

    @abstractmethod
    def ses_ayari(self):
        pass

    @abstractmethod
    def kanal_ekle(self):
        pass

    @abstractmethod
    def kanal_sil(self):
        pass

    @abstractmethod
    def kanal_ara(self):
        pass

    @abstractmethod
    def favorilere_ekle(self):
        pass

    @abstractmethod
    def favorilerden_cikar(self):
        pass

    @abstractmethod
    def kanal_sayisi(self):
        pass

    @abstractmethod
    def rastgele_kanal(self):
        pass

    @abstractmethod
    def tv_bilgileri(self):
        pass

    @abstractmethod
    def kanallari_goster(self):
        pass
