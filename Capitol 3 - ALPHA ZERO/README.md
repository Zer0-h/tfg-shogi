# Alpha Zero General Tres En Ratlla Demo
Una versió acurtada i modificada per a la demostració del tres en ratlla tres en ratlla de https://github.com/suragnair/alpha-zero-general.

Si es vol entrenar: 

```bash
python main.py
```

Per jugar contra l'agent (amb un jugador humà):

```
python pit.py
```

El registre d'entrenament es troba a ./message.txt
A sample of training log is in ./message.txt

Un registre de les pèrdues es troba a ./log.csv

# Explicació dels Fitxers

Aquest és un breu resum dels fitxers principals del joc de tres en ratlla, així com del model de xarxa neuronal implementat per jugar al joc.

## Fitxer: Arena.py

Aquest fitxer conté la implementació de l'arena de tres en ratlla.

- **Arena**: La classe Arena representa l'arena de joc on es fan les competicions entre diferents jugadors i es realitzen les avaluacions dels models de xarxa neuronal.

## Fitxer: Coach.py

Aquest fitxer conté la implementació de l'entrenador per al joc del tres en ratlla.

- **Coach**: La classe Coach s'encarrega de l'entrenament dels models de xarxa neuronal utilitzant l'algorisme de cerca de l'arbre de decisió (MCTS).

## Fitxer: Game.py

Aquest fitxer conté la implementació del joc de tres en ratlla.

- **Game**: La classe Game representa el joc de tres en ratlla. Proporciona mètodes per obtenir l'estat inicial del tauler, les dimensions del tauler, el nombre d'accions possibles, la transició a l'estat següent, les accions vàlides, comprovar si el joc ha acabat i aplicar transformacions simètriques.

## Fitxer: main.py

Aquest fitxer és l'arxiu principal que s'executa per iniciar el joc de tres en ratlla.

- **main**: Aquesta funció principal crea una instància del joc, del model de xarxa neuronal i de l'entrenador, i executa l'entrenament del model utilitzant el coach.

## Fitxer: MCTS.py

Aquest fitxer conté la implementació de l'algorisme de cerca de l'arbre de decisió per al joc de tres en ratlla.

- **MCTS**: La classe MCTS representa l'algorisme de cerca de l'arbre de decisió utilitzat per seleccionar les millors accions en cada estat del joc.

## Fitxer: NeuralNet.py

Aquest fitxer conté la implementació de l'arquitectura de la xarxa neuronal per al joc de tres en ratlla.

- **NeuralNet**: La classe NeuralNet defineix l'arquitectura de la xarxa neuronal i proporciona mètodes per entrenar-la, fer prediccions i guardar i carregar els pesos del model.

## Fitxer: pit.py

Aquest fitxer conté un script per jugar a tres en ratlla contra la xarxa neuronal entrenada.

- **pit**: Aquest script permet als jugadors humans enfrontar-se a la xarxa neuronal entrenada i jugar partides de tres en ratlla.

## Fitxer: utils.py

Aquest fitxer conté funcions d'utilitat utilitzades en diversos llocs del projecte.

- Funcions auxiliars i constants utilitzades en diferents parts del codi del joc de tres en ratlla i de la xarxa neuronal.

Aquesta breu explicació dels fitxers principals t'ajudarà a entendre millor l'estructura i funcionalitat del joc de tres en ratlla, així com del model de xarxa neuronal utilitzat per jugar-hi.

Si tens alguna altra pregunta, estic aquí per ajudar-te!
