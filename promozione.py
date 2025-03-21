class Cliente:
    def __init__(self, nome):
        self._nome = nome
        self._spesa_dal_sconto_ultimo = 0.0  # Contatore di spesa
        self._sconto_disponibile = 0.0        # Sconto disponibile
        self._totale_pagato = 0.0             # Totale effettivo pagato

    def effetuaAcquisto(self, ammontare):
        importo_originale = ammontare
        applicato = 0  # Inizializzazione
        
        # Applica il sconto disponibile (se presente)
        if self._sconto_disponibile > 0:
            applicato = min(self._sconto_disponibile, importo_originale)
            self._sconto_disponibile -= applicato
            ammontare -= applicato  # Importo effettivo pagato
        
        # Aggiorna il contatore di spesa
        self._spesa_dal_sconto_ultimo += ammontare
        
        # Genera un nuovo sconto per la transazione successiva (se necessario)
        if self._spesa_dal_sconto_ultimo >= 100:
            self._sconto_disponibile += 10  # Aggiunge 10€ di sconto
            # Resetta il contatore a 0 invece di usare modulo
            self._spesa_dal_sconto_ultimo = 0  # Reset completo
        
        # Aggiorna il totale pagato
        self._totale_pagato += ammontare

    def scontoRaggiunto(self):
        return self._sconto_disponibile > 0

def main():
    nome = input("Inserisci il nome del cliente: ")
    cliente = Cliente(nome)
    
    while True:
        cliente_input = input("Importo acquisto (o 'q' per uscire): ")
        if cliente_input.lower() == 'q':
            break
        try:
            ammontare = float(cliente_input)
            cliente.effetuaAcquisto(ammontare)
            
            print(f"\nProfilo di {cliente._nome}:")
            print(f"Totale pagato: {cliente._totale_pagato:.2f}€")
            print(f"Sconto disponibile: {cliente._sconto_disponibile:.2f}€")
            print(f"Spesa dall'ultimo sconto: {cliente._spesa_dal_sconto_ultimo:.2f}€")
        except ValueError:
            print("Errore: Inserisci un numero valido.")

    print("\nProgramma terminato.")

if __name__ == "__main__":
    main()