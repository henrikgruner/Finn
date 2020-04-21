## Boligmarkedet
Henter ut data fra finn.no sin eiendomsside fra de fem største byene i Norge:

Oslo, Bergen, Trondheim, Stavanger, Tromsø

### Output

#### BoligDataBy.csv
Lager en egen .csv fil for hver by med følgende attributter:

ID, Beskrivelse, Adresse, pris, kvadratmeter, pris per kvadratmeter, totalpris, fellesutgifter og meglerfirma.

#####  Eksempel
<img width="1193" alt="Screen Shot 2020-04-07 at 15 39 58" src="https://user-images.githubusercontent.com/60741787/78676249-793be100-78e6-11ea-9752-c7c53c493257.png">

#### Kvadratmeterpris.csv
Oppdateres hver gang programmer kjøres. Legger til gjennomsnittsprisene per kvadratmeter for hver av de fem største byene. 
##### Eksempel
<img width="516" alt="Screen Shot 2020-04-18 at 13 11 43" src="https://user-images.githubusercontent.com/60741787/79636184-309de680-8176-11ea-8134-31d2234efddd.png">

plotting.py gir ut et basic plot for gjennomsnittspris de siste dager ( basert på hvor ofte man har kjørt bolig.py).

<img width="616" alt="Screen Shot 2020-04-21 at 12 12 55" src="https://user-images.githubusercontent.com/60741787/79854363-a1890c80-83c9-11ea-9ef7-4993ced42164.png">
