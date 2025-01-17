import tkinter as tk
from tkinter import messagebox
import os
import webbrowser


class Aplicatie:
    def __init__(self, root):
        self.root = root
        self.root.title("Predicție Rezultat Meci")

        # Stiluri pentru fonturi și butoane
        font_style = ("Times New Roman", 12)

        # Numele echipei 1
        self.label_echipa1 = tk.Label(root, text="Numele echipei 1:", font=font_style)
        self.label_echipa1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_echipa1 = tk.Entry(root, font=font_style)
        self.entry_echipa1.grid(row=0, column=1, padx=10, pady=10)

        # Numele echipei 2
        self.label_echipa2 = tk.Label(root, text="Numele echipei 2:", font=font_style)
        self.label_echipa2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_echipa2 = tk.Entry(root, font=font_style)
        self.entry_echipa2.grid(row=1, column=1, padx=10, pady=10)

        # Numărul de meciuri
        self.label_meciuri = tk.Label(root, text="Numărul de meciuri:", font=font_style)
        self.label_meciuri.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_meciuri = tk.Entry(root, font=font_style)
        self.entry_meciuri.grid(row=2, column=1, padx=10, pady=10)

        # Goluri echipa 1
        self.label_goluri1 = tk.Label(root, text="Goluri echipa 1 (separate prin spațiu):", font=font_style)
        self.label_goluri1.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_goluri1 = tk.Entry(root, font=font_style)
        self.entry_goluri1.grid(row=3, column=1, padx=10, pady=10)

        # Goluri echipa 2
        self.label_goluri2 = tk.Label(root, text="Goluri echipa 2 (separate prin spațiu):", font=font_style)
        self.label_goluri2.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_goluri2 = tk.Entry(root, font=font_style)
        self.entry_goluri2.grid(row=4, column=1, padx=10, pady=10)

        # Evenimente neașteptate
        self.label_evenimente = tk.Label(root, text="Au existat evenimente neașteptate? (da/nu):", font=font_style)
        self.label_evenimente.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.entry_evenimente = tk.Entry(root, font=font_style)
        self.entry_evenimente.grid(row=5, column=1, padx=10, pady=10)

        # Echipa afectată
        self.label_echipa_afectata = tk.Label(root, text="Echipa afectată (1 sau 2):", font=font_style)
        self.label_echipa_afectata.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry_echipa_afectata = tk.Entry(root, font=font_style)
        self.entry_echipa_afectata.grid(row=6, column=1, padx=10, pady=10)

        # Echipa gazdă
        self.label_echipa_gazda = tk.Label(root, text="Echipa gazdă (1 sau 2):", font=font_style)
        self.label_echipa_gazda.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.entry_echipa_gazda = tk.Entry(root, font=font_style)
        self.entry_echipa_gazda.grid(row=7, column=1, padx=10, pady=10)

        # Buton pentru deschiderea paginii web cu informații
        self.button_info = tk.Button(
            root, text="Deschide informații evenimente", bg="#ADD8E6", font=font_style, command=self.deschide_pagina_web
        )
        self.button_info.grid(row=8, column=0, padx=10, pady=20, sticky="w")

        # Buton pentru calculare rezultat (verde deschis)
        self.button_calcul = tk.Button(
            root, text="Calculează Rezultatul", bg="#90EE90", font=font_style, command=self.calculeaza_rezultatul
        )
        self.button_calcul.grid(row=8, column=1, padx=10, pady=20)

        # Buton pentru resetare (roșu deschis)
        self.button_reset = tk.Button(
            root, text="Resetează Simulatorul", bg="#FF7F7F", font=font_style, command=self.reseteaza_campurile
        )
        self.button_reset.grid(row=9, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

    def deschide_pagina_web(self):
        url = "https://www.sportsmole.co.uk/"
        webbrowser.open(url)

    def salveaza_in_istoric(self, rezultat):
        try:
            # Obține calea desktop-ului utilizatorului
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            folder_path = os.path.join(desktop_path, "Proiect MAP")

            # Creează folderul "Proiect MAP" dacă nu există
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Creează calea completă pentru fișierul "istoric.txt"
            file_path = os.path.join(folder_path, "istoric.txt")

            # Scrie rezultatul în fișierul "istoric.txt" cu encoding utf-8
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(rezultat + "\n")
        except Exception as e:
            print(f"Eroare la salvarea rezultatului în fișier: {e}")

    def calculeaza_rezultatul(self):
        try:
            # Citim datele introduse de utilizator
            nume_echipa1 = self.entry_echipa1.get()
            nume_echipa2 = self.entry_echipa2.get()
            numar_meciuri = int(self.entry_meciuri.get())
            goluri_echipa1 = list(map(int, self.entry_goluri1.get().split()))
            goluri_echipa2 = list(map(int, self.entry_goluri2.get().split()))
            evenimente = self.entry_evenimente.get().strip().lower()
            echipa_afectata = self.entry_echipa_afectata.get().strip()
            echipa_gazda = self.entry_echipa_gazda.get().strip()

            # Verificăm dacă numărul de goluri corespunde cu numărul de meciuri
            if len(goluri_echipa1) != numar_meciuri or len(goluri_echipa2) != numar_meciuri:
                messagebox.showerror("Eroare", "Numărul de goluri introduse nu corespunde cu numărul de meciuri!")
                return

            # Adăugăm un gol suplimentar echipei gazdă
            if echipa_gazda == "1":
                goluri_echipa1[-1] += 1
            elif echipa_gazda == "2":
                goluri_echipa2[-1] += 1
            else:
                messagebox.showerror("Eroare", "Echipa gazdă trebuie să fie 1 sau 2!")
                return

            # Aplicați evenimentele neașteptate
            if evenimente == "da":
                if echipa_afectata == "1":
                    goluri_echipa1[-1] = max(0, goluri_echipa1[-1] - 1)  # Reducem cu 1 gol, dar fără a scădea sub 0
                elif echipa_afectata == "2":
                    goluri_echipa2[-1] = max(0, goluri_echipa2[-1] - 1)
                else:
                    messagebox.showerror("Eroare", "Echipa afectată trebuie să fie 1 sau 2!")
                    return

            # Calculăm media de goluri pentru fiecare echipă
            media_goluri_echipa1 = sum(goluri_echipa1) / numar_meciuri
            media_goluri_echipa2 = sum(goluri_echipa2) / numar_meciuri

            # Calculăm probabilitatea de câștig
            total_medii = media_goluri_echipa1 + media_goluri_echipa2
            if total_medii > 0:  # Evităm divizarea la zero
                prob_echipa1 = (media_goluri_echipa1 / total_medii) * 100
                prob_echipa2 = (media_goluri_echipa2 / total_medii) * 100
            else:
                prob_echipa1 = prob_echipa2 = 50  # În caz de egalitate absolută

            # Prezicem rezultatul
            if media_goluri_echipa1 > media_goluri_echipa2:
                rezultat = f"Echipa câștigătoare este: {nume_echipa1} (Probabilitate: {prob_echipa1:.2f}%)"
            elif media_goluri_echipa1 < media_goluri_echipa2:
                rezultat = f"Echipa câștigătoare este: {nume_echipa2} (Probabilitate: {prob_echipa2:.2f}%)"
            else:
                rezultat = f"Rezultatul prezis este: Remiză (Probabilitate: {prob_echipa1:.2f}% - {prob_echipa2:.2f}%)"

            # Afișăm rezultatul într-o fereastră popup
            messagebox.showinfo("Rezultatul Meciului", rezultat)

            # Afișăm rezultatul în terminal
            print("Rezultatul meciului este: ")
            print(rezultat)

            # Apelăm metoda pentru salvarea rezultatului
            self.salveaza_in_istoric(rezultat)

        except ValueError:
            messagebox.showerror("Eroare", "Datele introduse nu sunt valide! Asigurați-vă că ați completat toate câmpurile corect.")

    def reseteaza_campurile(self):
        # Resetează toate câmpurile de introducere la starea inițială
        self.entry_echipa1.delete(0, tk.END)
        self.entry_echipa2.delete(0, tk.END)
        self.entry_meciuri.delete(0, tk.END)
        self.entry_goluri1.delete(0, tk.END)
        self.entry_goluri2.delete(0, tk.END)
        self.entry_evenimente.delete(0, tk.END)
        self.entry_echipa_afectata.delete(0, tk.END)
        self.entry_echipa_gazda.delete(0, tk.END)
        messagebox.showinfo("Resetare", "Simulatorul a fost resetat cu succes!")


# Inițializăm aplicația
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicatie(root)
    root.mainloop()
