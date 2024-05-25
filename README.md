# Proiect_Final

# Mini Magazin Online

Mini Magazin Online este o aplicație web simplă, creată pentru a demonstra funcționalitățile de bază ale unui magazin online.
Aplicația permite utilizatorilor:
* să vizualizeze o listă de produse și servicii
* să consulte detaliile fiecărui produs
* să contacteze magazinul prin intermediul unei pagini de contact.

Funcționalități
Lista de Produse:
Utilizatorii pot vizualiza o listă de produse disponibile în magazin.
Fiecare produs este afișat cu o imagine, un nume, o descriere scurtă și un preț.

Detalii Produs:
Utilizatorii pot face clic pe un produs din listă pentru a vedea detaliile complete ale acestuia.
Aceasta include o descriere detaliată, prețul și o imagine mai mare.

Lista de Servicii:
O pagină dedicată prezentării serviciilor oferite de magazin.
Fiecare serviciu este descris în detaliu, evidențiind beneficiile pentru utilizatori.

Pagina de Contact:
Utilizatorii pot completa un formular de contact pentru a trimite mesaje magazinului.
Formularul include câmpuri pentru nume, email și mesaj.


2. Screenshot Mini Magazin Online
# Mini Magazin Online

![Screenshot al aplicației](images/screenshot%20mini%20magazin%20online.PNG)

Aceasta este o aplicație web simplă pentru un mini magazin online, dezvoltată folosind Flask.

3. Tehnologii & Tool-uri utilizate

Pentru realizarea acestui proiect, am folosit următoarele tehnologii și tool-uri:

* Python: Limbajul de programare principal pentru dezvoltarea aplicației.

* Flask: Un framework web pentru Python, folosit pentru dezvoltarea aplicației web.

* HTML și CSS: Folosite pentru structurarea și stilizarea paginilor web.

* Jinja2: Un motor de șabloane pentru Python, integrat cu Flask pentru generarea dinamică a paginilor web.

* Git și GitHub: Git a fost folosit pentru controlul versiunilor proiectului, iar GitHub a fost folosit pentru găzduirea și colaborarea la cod.

* PyCharm: Un mediu de dezvoltare integrat (IDE) pentru Python, utilizat pentru scrierea și testarea codului.

* Terminalul sau linia de comandă: Folosit pentru gestionarea pachetelor Python, controlul versiunilor cu Git și rularea comenzilor de sistem.

* SQLite: Un sistem de gestionare a bazelor de date relaționale, utilizat pentru stocarea și gestionarea datelor în cadrul aplicației.

Acestea sunt principalele tehnologii și tool-uri utilizate în realizarea proiectului.


4. Instrucțiuni de instalare și rulare a proiectului

Urmează pașii de mai jos pentru a instala și rula proiectul:

# Instalarea și Configurarea

-->>Clonare repository-ului: Clonează repository-ul proiectului de pe GitHub pe computerul tău folosind comanda:
git clone https://github.com/Rradu10/Proiect_Final.git

-->>Navigare în director: Intră în directorul proiectului:
cd Proiect_Final

-->>Creare și activare virtual environment (opțional):
Este recomandat să creezi un mediu virtual pentru a izola dependențele proiectului. 
Poți folosi venv sau virtualenv. Iată cum poți crea și activa un mediu virtual folosind venv:
python -m venv venv
.\venv\Scripts\activate   

-->>Instalare dependențelor: Instalează dependențele proiectului folosind pip:
pip install -r requirements.txt

-->>Configurare bazei de date: 
Poate fi necesar să configurezi calea către baza de date SQLite în fișierul config.py, în funcție de cum este definită în proiect.

### Rularea Aplicatiei

# Pornește serverul Flask: Rulează următoarea comandă pentru a porni serverul de dezvoltare Flask:
flask run

# Accesează aplicația în browser: Deschide browserul și navighează la adresa http://127.0.0.1:5000/ pentru a vizualiza aplicația.