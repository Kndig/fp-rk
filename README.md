### Aufgaben zum Lambda-Kalkül

1. (?abc.cba)zz(?wv.w) = (?zzc.czz)(?wv.w) = ?zwv.vwz = vwz

2. (?x.(?y.xyy))(?a.a)b = ?b.tbb

3. (?y.y)(?x.xx)(?z.zq) = (?x.xt)(?z.zq) = zq

7. ?x.xxx = xxx berechenbar

8. berechenbar

9. divergent

10. divergent


### Y Combinator

1. Yg = ?f.((?x.f(xx))(?x.f(xx)))g = ?f.(?x.f(?x.f(xx)?x.f(xx)))g = ?f.(?g.f(?g.f(gg)?g.f(gg))) = unendlich g

2. Vermehrung der Anzahl im Quadrat

3. Es entstehen unendlich viele Funktionen, diese sind divergent.

4. a Alle Zahlen von 1 bis 100 werden addiert; es handelt sich um einen rekursiven Algorithmus. `n + n-1`

4. b 2a: ersetzen eines imperativen Ausdrucks durch einen Lambaausdruck 2b: Rekursion wird durch weiteren Lambaausdruck ersetzt (darum foo von foo) 6. Y-Combinator wurde eingefügt, foo ausgeklammert. Da foo als f definiert ist, wird es so lange ausgeführt, bis `n == 0` ist.

4. c Die Formel wird auf sich selbst angewendet, so dass eine "doppelte" Schlaufe entsteht. Dadurch entsteht ein Y-Combinator.
