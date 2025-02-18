class Message :
    def __init__(self, mittente, destinatario):
        self._mittente = mittente
        self._destinatario = destinatario
        self._corpoMessaggio = []

    def append(self, riga):
        self._corpoMessaggio.append(riga)

    def toString(self):
        valore= "Mittente: \n  "+ self._mittente + "\nDestinatario:\n  "+ self._destinatario + "\nMessaggio: \n  " + "\n  ".join(self._corpoMessaggio)
        return valore
    
    
        



email1 = Message("Gigio", "Valentino")
email1.append("Ciao")
email1.append("come va")
email1.append("tanti saluti")
email1.append("Gigio")

print(email1.toString())