# SmartGrid
SmartGrid assignment by Lisa, Tosca and Demi. 

## Uitleg van de case
Veel huizen hebben tegenwoordig zonnepanelen, windmolens of andere installaties om zelf energie mee te produceren. Vaak wordt er meer dan voor eigen consumptie nodig is geproduceerd. Het overschot zou kunnen worden terugverkocht aan de leverancier, maar de infrastructuur (het grid) is daar veelal niet op berekend. Om de pieken in consumptie en productie te kunnen managen moeten er batterijen geplaatst worden. 

De huizen hebben zonnepanelen met een maximale output, de batterijen hebben een maximale capaciteit. De maximumcapaciteit van de huizen mag die van de batterijen uiteraard niet overschrijden. De kosten zijn als volgt: de batterijen kosten 5000 per stuk. De kabels kosten 9 per grid-segment. Bij deze case is het dus de bedoeling om te kijken hoe batterijen en huizen zo efficient mogelijk met elkaar verbonden kunnen worden op het grid. Hoe efficienter de verbinding, hoe minder kabel er gebruikt hoeft te worden, hoe lager de totale kosten.

Er zijn een aantal vereisten waaraan het uiteindelijke SmartGrid moet voldoen, namelijk: 
- Batterijen mogen niet aan elkaar verbondenden zijn. Ook niet via een huis.
- Een huis mag niet aan meerdere batterijen verbonden zijn.
- Elk huis heeft een eigen unieke kabel nodig naar de batterij.
- Er mogen meerdere kabels over dezelfde gridsegmenten lopen. Het blijven echter wel unieke kabels en leveren geen kostenvermindering op.
- Huizen mogen via eenzelfde kabel aan een batterij verbonden zijn. Ze mogen dus een kabel delen.

## De algoritmen
De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.

## Gebruik 
hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen
