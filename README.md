# SmartGrid
SmartGrid assignment by Lisa, Tosca and Demi. 

## Uitleg van de case
Veel huizen hebben tegenwoordig zonnepanelen, windmolens of andere installaties om zelf energie mee te produceren. Vaak wordt er meer dan voor eigen consumptie nodig is geproduceerd. Het overschot zou kunnen worden terugverkocht aan de leverancier, maar de infrastructuur (het grid) is daar veelal niet op berekend. Om de pieken in consumptie en productie te kunnen managen moeten er batterijen geplaatst worden. 

Bij deze case zijn er drie wijken/districten, ofwel 'grids', en op deze grids bevinden zich huizen en batterijen. De huizen hebben zonnepanelen met een maximale output, de batterijen hebben een maximale capaciteit. De maximumcapaciteit van de huizen mag die van de batterijen uiteraard niet overschrijden. De kosten zijn als volgt: de batterijen kosten 5000 per stuk. De kabels kosten 9 per grid-segment. Bij deze case is het dus de bedoeling om te kijken hoe batterijen en huizen zo efficient mogelijk met elkaar verbonden kunnen worden op het grid. Hoe efficienter de verbinding, hoe minder kabel er gebruikt hoeft te worden, hoe lager de totale kosten.

Er zijn een aantal vereisten waaraan het uiteindelijke SmartGrid moet voldoen, namelijk: 
- Batterijen mogen niet aan elkaar verbondenden zijn. Ook niet via een huis.
- Een huis mag niet aan meerdere batterijen verbonden zijn.
- Elk huis heeft een eigen unieke kabel nodig naar de batterij.
- Er mogen meerdere kabels over dezelfde gridsegmenten lopen. Het blijven echter wel unieke kabels en leveren geen kostenvermindering op.
- Huizen mogen via eenzelfde kabel aan een batterij verbonden zijn. Ze mogen dus een kabel delen.

Dit laatste vereiste is erg belangrijk voor de totale kostenvermindering. In eerste instantie hadden wij een output waarin er een kabel per huis werd verbonden, maar later hebben wij geimplementeerd dat kabels ook opgesplitst kunnen worden.

## De algoritmes
#### Random algoritme (baseline)
In dit geval worden de resultaten geproduceerd door middel van een algoritme die random verbinding legt tussen huizen en batterijen. Door te itereren over de huizen van het district (wijk) wordt er per huis een verbinding gelegd met een random batterij uit de lijst. In deze situatie is er geen rekening gehouden met de maximale capaciteit van de batterij en de positie van de verbindingen. 

Er wordt in dit algoritme gebruik gemaakt van twee functies: random_assignment en random_assignment_repeat. Bij de random assigment functie wordt er een verbinding gemaakt van de x-coordinaat van het huis naar de x-coordinaat van de batterij, en vervolgens van de y-coordinaat van het huis naar de y-coordinaat van de batterij. De connecties worden opgeslagen in een dictionary. Er wordt met een if-statement gekeken of de maximale capaciteit van de batterij niet overschreden wordt.

De repeat functie zorgt er voor dat de random assignment functie opnieuw blijft runnen totdat alle huizen verbonden zijn.

#### Hillclimber algoritme 
De resultaten worden in dit geval tot stand gebracht met behulp van het Hillclimber algoritme. Dit houdt in dat eerst, middels het in de baseline opgestelde random algoritme, een begintoestand wordt gecreëerd. Deze wordt vervolgens gemanipuleerd middels het Hillclimber algoritme. Hier vindt optimalisatie plaats van de resultaten door het verwisselen van batterijen tussen twee huizen. Het verwisselen van batterijen vindt niet random plaats; de batterij wordt verwisseld met de batterij waar het volgende huis aan is verbonden. Vervolgens wordt nagegaan of deze resultaten optimaler zijn dan de resultaten in de random situatie. Een situatie wordt gezien als optimaler wanneer de totale lengte van alle kabels afneemt. Deze afname resulteert eveneens in een lagere hoeveelheid totale kosten. Een swap tussen de batterijen van twee huizen is enkel mogelijk wanneer deze swap resulteert in een afname van de lengte van de totale kabel én de maximale capaciteit van de betreffende batterij niet wordt overschreden. Op het moment dat de batterijen van elk huis in de lijst zijn geswapt, indien mogelijk, stopt het algoritme.

#### Stimulated annealing
Als tweede algoritme hebben wij gekozen voor een simulated annealing algoritme. Hierbij gebruiken wij eveneens als het Hillclimber algoritme, het baseline random algoritme om een beginsituatie van de wijk te creëren. Deze wordt vervolgens gemanipuleerd middels simulated annealing. 

Bij het simulated annealing algoritme wordt er, in tegenstelling tot het hillclimber algoritme, rekening gehouden met eventuele lokale minima en maxima waarin resultaten zich bevinden. Met simulated annealing kunnen er dus globale minima en maxima gevonden worden. Dit houdt in dat het algoritme soms voor een ‘slechtere’ oplossing kiest om er voor te zorgen dat de oplossing niet in een lokale maximum of minimum vastzit.  Voor het vaststellen en kiezen van een ‘slechtere keuze’ wordt er in dit algoritme gebruik gemaakt van een initiële temperatuur(T0),  uiteindelijke temperatuur(T) en een alpha waarde. Vervolgens wordt de huidige temperatuur gelijk gesteld aan de initiële temperatuur, en loopt het algoritme zolang de huidige temperatuur nog groter is dan de gewenste uiteindelijke temperatuur.

Wij hebben de volgende waardes gebruikt voor de temperatuur en alpha: 
- initial temp = 1000.0
- final temp = 1.0
- alpha = 0.01.

## Gebruik 
Deze code kan gerund worden door aanroepen van:
  
  `python main.py [district_x] [algorithm.py]`
  
- Bij district_x kan het getal 1, 2 of 3 kan zijn. Deze getallen duiden de betreffende wijk aan. Wanneer district_1 als argument wordt meegegeven, genereert het algoritme dus een oplossing voor wijk 1.

- Bij algorithm.py kan er gekozen worden uit randomise.py, hillclimber.py en simulatedannealing.py.

## Structuur
De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kunt vinden:

- /code: bevat alle code van dit project
  - /code/algorithms: bevat de code voor de verschillende algoritmes
  - /code/classes: bevat de benodigde classes voor deze case
  - /code/visualisation: bevat de code voor de visualisatie, in ons geval een plot 
- /data: bevat de verschillende databestanden die nodig zijn om de grid te vullen en te visualiseren
