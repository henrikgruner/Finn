# Finn
Prosjekt for å lære webscraping. Henter boligdata fra finn for å finne diverse nøkkeltall i boligmarkedet.
### Boligdata
Henter ut alle boliger til salgs fra de fem største byene, i tillegg legger scriptet til de gjennomsnittslige prisene for en kvadratmeter  for hver by i en egen .csv fil. Her kan prisene spores over tid. 

### UtleieData
Henter ut alle utleieobjekter fra de fem største byene. 

### Resultater
Eksempel på resultatene og hvilke attributter som hentes kan sees i hver respektive folders readme. Resultatene legges ikke ut her, og programmet kan ikke benyttes til kommersielle formål. Minner om denne fra Finn.no

"Innholdet er beskyttet etter åndsverkloven. Regelmessig, systematisk eller kontinuerlig innhenting, lagring, indeksering, distribusjon og all annen form for bruk av data fra FINN.no til andre enn rent personlige formål tillates ikke uten eksplisitt, skriftlig tillatelse fra FINN.no."


#### Packages 
Prosjektet bruker python3.7 og følgende pakker på installeres:

```
pip install BeautifulSoup
pip install urllib
pip install pandas
```

