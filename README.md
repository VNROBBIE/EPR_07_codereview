Graphen – Mehrzieloptimierung

---------------------------------------------------------------------------
# Projektübersicht

In diesem Projekt arbeiten wir mit einem Graphen, dessen Kanten zwei Werte besitzen:

- Kosten (cost): Aufwand, um von einem Knoten zum nächsten zu gelangen  
- Ablenkungswert (fun): Wie attraktiv oder interessant dieser Weg für die Katze ist.

Die Aufgabe besteht darin, für einen gegebenen Start- und Zielknoten den „besten“ Weg zu finden.
Dabei sollen:
- die Kosten möglichst gering
- und der Ablenkungswert möglichst hoch sein


Das Projekt ist in mehrere Module aufgeteilt, die unterschiedliche Lösungsansätze implementieren.

---------------------------------------------------------------------------

## Graph-Struktur


Der Graph wird als Dictionary dargestellt und bei den Rekursive und Greedy Algorithmen benutzt.

CAT_EDGES = {
    ("A", "B") : (3, 2),
    ("A", "C") : (1, 0), etc...
    }

- Jeder Schlüssel ist eine Kante (start, ziel)

- Jeder Wert ist ein Tupel (cost, fun)

- Jeder Knoten darf nur einmal besucht werden (keine Zyklen)

-----------------

TEST_PATHS = [("A", "C", "D", "B", "E"), ("A", "B", "D", "F")

Diese Liste von Tupeln entspricht vorgegebenen Wege die von den 3 Optimierungsfunktionen als Argument genommen werden
---------------------------------------------------------------------------


### Multiobjective Optimization

Dieses Modul enthält Funktionen zur Bewertung und Optimierung von Wegen:

- path_value(paths_list, edges_dict)

Berechnet für jeden gegebenen Pfad die Gesamtkosten und den gesamten Ablenkungswert.

Eingabe:

Liste von Pfaden (Tupel mit Knoten)
Dictionary mit Kantenwerten

Ausgabe:

Liste von Tupeln (total_cost, total_fun)



- pareto_optimal(paths_list, edges_dict)

Bestimmt die Pareto-optimalen Pfade.
Ein Pfad ist pareto-optimal, wenn kein anderer Pfad in beiden Zielen besser ist.

Eingabe:

Liste von Pfaden (Tupel mit Knoten)
Dictionary mit Kantenwerten

Ausgabe:

Menge von pareto-optimalen Pfaden



- epsilon_constraint(paths_list, edges_dict, main_goal, sec_goal_value)

Diese Funktion implementiert die ε-Constraint-Methode zur Mehrzieloptimierung.

Dabei wird ein Ziel als Hauptziel festgelegt (entweder Kosten minimieren oder Ablenkungswert maximieren),
während das zweite Ziel als Nebenbedingung dient.

Zuerst werden alle Pfade entfernt, die die Nebenbedingung nicht erfüllen
(z.B. zu wenig Ablenkung oder zu hohe Kosten).
Anschließend wird unter den verbleibenden Pfaden derjenige ausgewählt,
der das Hauptziel optimal erfüllt.

Eingabe:

paths_list: Liste von möglichen Pfaden (Tupel mit Knoten)

edges_dict: Dictionary mit Kanten und deren Kosten- und Ablenkungswerten

main_goal: Hauptziel der Optimierung ("cost" oder "fun")

sec_goal_value: Grenzwert für das sekundäre Ziel (Mindest-Fun oder maximale Kosten)

Ausgabe:

Eine Menge (set) von optimalen Pfaden, die die Nebenbedingung erfüllen und das Hauptziel optimal optimieren
Die Funktion gibt eine Menge von optimalen Pfaden zurück,
da es mehrere gleich gute Lösungen geben kann.


---------------------------------------------------------------------------



#### Modul: Rekursiver Algorithmus


Hilfsfunktion:
-optimize_weighted(cost, fun, weight_cost, weight_fun)

Diese Hilfsfunktion kombiniert Kosten und Ablenkungswert zu einem einzelnen Bewertungswert
mithilfe einer gewichteten Summe.

Sie wird vom rekursiven Algorithmus verwendet, um verschiedene Pfade miteinander zu vergleichen.
Ein kleinerer Wert bedeutet einen besseren Pfad.

Eingabe:

cost: Gesamtkosten eines Pfades

fun: Gesamt-Ablenkungswert eines Pfades

weight_cost: Gewichtungsfaktor für die Kosten

weight_fun: Gewichtungsfaktor für den Ablenkungswert

Ausgabe:

Ein numerischer Score, wobei kleinere Werte bessere Pfade darstellen

------------------------------------

Rekursive Hauptfunktion:
- recursive_best_path(current, goal, edges_dict, optimize_func, ...)

Diese Funktion sucht rekursiv den optimalen Pfad in einem Graphen
zwischen einem Startknoten und einem Zielknoten.

Dabei werden alle möglichen Pfade ohne erneutes Besuchen von Knoten untersucht.
Zur Bewertung der Pfade wird eine übergebene Optimierungsfunktion(Hilfsfuktion)verwendet.

Eingabe:

current: Aktueller Knoten (Startknoten beim ersten Aufruf)

goal: Zielknoten

edges_dict: Dictionary mit Kanten und deren (cost, fun)-Werten

optimize_func: Funktion zur Bewertung eines Pfades basierend auf Kosten und Ablenkungswert

path (optional): Aktueller Pfad (Liste von Knoten)

acc_cost (optional): Bisher aufgelaufene Kosten

acc_fun (optional): Bisher aufgelaufener Ablenkungswert

visited (optional): Menge bereits besuchter Knoten

Ausgabe:

Ein Tupel (best_path, total_cost, total_fun), falls ein Pfad gefunden wird

None, falls kein Pfad vom Start- zum Zielknoten existiert
---------------------------------------------------------------------------
##### Greedy-Algorithmus (noch zu implementieren)

Geplant ist ein Greedy-Ansatz, bei dem die Katze an jedem Knoten lokal die „beste“ nächste Kante auswählt
(z. B. mit dem höchsten Ablenkungswert oder bestem gewichteten Score).










---------------------------------------------------------------------------
###### Zeitmessung

In einem separaten Modul wird die Laufzeit der Algorithmen gemessen.

Dafür wird das Modul timeit verwendet.

Die Laufzeiten von: rekursivem Algorithmus und Greedy-Algorithmus

werden verglichen, indem die Funktionen mehrfach ausgeführt werden(10.000 mals jeweils)
