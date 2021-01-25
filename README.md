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

## De algoritmen
#### Random algoritme (baseline)
In dit geval worden de resultaten geproduceerd door middel van een algoritme die random verbinding legt tussen huizen en batterijen. Door te itereren over de huizen van het district (wijk) wordt er per huis een verbinding gelegd met een random batterij uit de lijst. 

#### Hillclimber algoritme 
De resultaten worden in dit geval tot stand gebracht met behulp van het Hillclimber algoritme. Dit houdt in dat eerst, middels het in de baseline opgestelde random algoritme, een begintoestand wordt gecreëerd. Deze wordt vervolgens gemanipuleerd middels het Hillclimber algoritme. Hier vindt optimalisatie plaats van de resultaten door het verwisselen van batterijen tussen twee huizen. Het verwisselen van batterijen vindt niet random plaats; de batterij wordt verwisseld met de batterij waar het volgende huis aan is verbonden. Vervolgens wordt nagegaan of deze resultaten optimaler zijn dan de resultaten in de random situatie. Een situatie wordt gezien als optimaler wanneer de totale lengte van alle kabels afneemt. Deze afname resulteert eveneens in een lagere hoeveelheid totale kosten. Een swap tussen de batterijen van twee huizen is enkel mogelijk wanneer deze swap resulteert in een afname van de lengte van de totale kabel én de maximale capaciteit van de betreffende batterij niet wordt overschreden. Op het moment dat de batterijen van elk huis in de lijst zijn geswapt, indien mogelijk, stopt het algoritme

#### Stimulated annealing


## Gebruik 
hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen
