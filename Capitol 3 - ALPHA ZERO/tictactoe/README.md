# Tres en Ratlla

## Fitxer: TicTacToePlayers.py

Aquest fitxer conté les classes de jugadors per al joc de tres en ratlla.

- **HumanPlayer**: Un jugador humà que demana a l'usuari que introdueixi moviments.
- **RandomPlayer**: Un jugador aleatori que selecciona es mou a l'atzar.
- **GreedyPlayer**: Un jugador cobdiciós que sempre selecciona el millor moviment disponible en funció de la puntuació de cada cel·la.

## Fitxer: TicTacToeLogic.py

Aquest fitxer conté la lògica del joc de tres en ratlla.

- **Board**: La classe Board representa el tauler de joc i manté el seu estat actual, com ara les peces col·locades i les comprovacions de les condicions de victòria o empat.

## Fitxer: TicTacToeGame.py

Aquest fitxer implementa la classe de joc de tres en ratlla.

- **TicTacToeGame**: La classe TicTacToeGame representa el propi joc de tres en ratlla. Proporciona mètodes per obtenir l'estat inicial del tauler, obtenir les dimensions del tauler, obtenir el nombre d'accions possibles, passar al següent estat, obtenir moviments vàlids, comprovar si el joc ha acabat i aplicar transformacions simètriques.

## Fitxer: TicTacToeNNet.py

Aquest fitxer implementa el model de xarxa neuronal per al joc de tres en ratlla mitjançant la biblioteca Keras.

- **TicTacToeNNet**: La classe TicTacToeNNet representa el model de xarxa neuronal per al joc de tres en ratlla. Defineix l'arquitectura de la xarxa, compila el model i proporciona mètodes per predir polítiques i valors des d'un tauler.

## Fitxer: NNet.py

Aquest fitxer és un 'wrapper' del model de xarxa neuronal del joc de tres en ratlla.

- **NNetWrapper**: La classe NNetWrapper és un 'wrapper' per al model de xarxa neuronal del tres en ratlla. Proporciona mètodes per entrenar el model, fer prediccions, desar i carregar els pesos del model als punts de control.
