# Casus RailNL
#### door Beter dan de NS: "We shoot for the stars! Or at least better than the NS"


A project to create as efficient as possible routes between Dutch stations. 

<img src="/research/images/map1.png" alt="Map"/>

## Het project
Wij hebben met verschillende algoritmes geprobeerd om zo'n hoogst mogelijk scorende lijnvoering te maken tussen intercity stations in Nederland en Holland. Een complex probleem, maar ook zeer interessant. Aldus zie hier onze resultaten!

## Aan de slag (Getting Started)
### Verseisten (Prerequisites)
Deze codebase is volledig geschreven in Python3.6.4. In requirements.txt staan de alle* benodigde libraries. Deze zijn grotendeels gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```
Helaas word Basemap niet goed ondersteund door pip. De library is echter in een .whl file te vinden op de website https://www.lfd.uci.edu/~gohlke/pythonlibs/. Hier kan hij worden gedownload en geinstalleerd  worden met pip install. Mogelijk wordt er een error gegeven tijdens de installatie voor het ontbreken van Visual Studio. Deze kan echter via de link in de error message worden gedownload.

## Structuur (Structure)
De github is verdeeld in verschillende hoofdsegmenten. Ten eerste bevindt zich hier de data folder, waarin de .csv bestanden staan waaruit de stations en tracks worden gelezen. Ook bevindt zich hier de research folder, waarin wij afbeeldingen, literatuur en data verzamelde. Voornamelijke echter bevindt zich hier de code folder, waarin main.py, de algoritmes en hun hulpfuncties zich bevinden. Vanuit main.py kan ook getest worden voor meer hierover, zie het kopje Test. 
De volgende algoritmes bevinden zich hier:

##### alg.random2
##### alg.greedy_random
##### alg.recalculating_greedy
##### alg.hill_climber_random
##### alg.hill_climber_multi_greedy
##### alg.hill_climber_mutation

Twee dieperliggende algoritmes, die niet zomaar gerund kunnen worden:
##### path_finder
##### alg.greedy_search

In de map alt bevind zich nog een file met twee varianten hill climber. Dit omdat greedy en random beter reageerden op net andere hill-climbers. De versie in de alt map zijn een hill climber van greedy op de 'random manier' en vice versa.


## Test (Testing)
Alle algoritmes kunnen getest worden in de main.py met behulp van scripts uit de run folder. Van alledrie is hiervan een voorbeeld te vinden in main.py. Dit gaat als volgt:

#### Stap 1
Initieer het data object door aan te geven welke kaart gebruikt gaat worden en of alle sporen kritiek zijn.

```
map = "Nationaal"
critical = False

data = obj.Data(map, critical)
```
#### Stap 2
Kies een van de volgende drie scripts:

##### run_random
Geschikt voor het runnen van het random algoritme (alg.random2)
###### Verplicht mee te geven:
Algoritme, data
###### Optioneel:
Aantal keer runnen (standaard 10.0000)
```
run.run_random(alg.random2, data, 100)
```

##### run_greedy
Geschikt voor het runnen van de twee greedy algoritmes (alg.greedy_random en alg.recalculating_greedy). 
###### Verplicht
Algoritme, data
###### Optioneel
Aantal keer runnen (standaard 10.000, maar 1 voor recalculating_greedy)
Invalid functie (standaard helper.invalid)
Lookup table functie (standaard helper.lookup_score

De laatste twee worden gebruikt voor heuristieken binnen greedy, zie hun beschrijving voor meer detail
```
run.run_greedy(alg.greedy_random, data, 100, helper.lookup_predicting, helper.invalid_fuck_heerlen)
```

##### run_hill_climber
Geschikt voor het runnen van van de hill-climber algoritmes (alg.hill_climber_random en alg.hill_climber_multi_greedy, en hun counterparst in de alt folder.). 
###### Verplicht
Algoritme, data
###### Optioneel
Aantal keer runnen (standaard 1.000)
Aantal stappen binnen de hill_climber (standaard 10)
Reeds bestaande oplossing om op verder te bouwen
```
run.run_hill_climber(alg.hill_climber_random, data, 10, 1000, solution)
```
Voor de multi hill-climber:
Het aantal trajecten dat per gewisseld worden (standaard 2)
```
run.run_hill_climber(alg.hill_climber_multi_greedy, data, 10, 1000, solution, 4)
```
##### voor alle scripts
Bij alle scripts kunnen aan het einde worden gekozen voor het laten printen van de trajecten, een kaartje, grafiek en een histogram. Dit wordt gedaan door na alle andere argumenten voor elk onderdeel respectievelijk True of False toe te voegen. Standaard staat dit alleen op printen van de trajecten en kan het verder met rust gelaten worden.

(printen lijnen, kaartje, grafiek, histogram)

```
run.run_random(alg.random2, data, 100, True, True, True, True)
```
#### Happy Tracking

## Auteurs (Authors)
* Kasper van Tulder
* Tijs Teulings

## Dankwoord (Acknowledgments)
* De geweldige Maarten van den Sande
* minor programmeren van de UvA
* Daan 'Heur' van den Berg
* Quinten 'model programmeur' van der Post



