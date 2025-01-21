il file p1.py svolge il punto 1 e stampa il sistema in forma di stato e le matrici A,B,C,D
il file p2.py stampa la funzione di trasferimento
il file p3_1.py crea il regolatore statico e apre il diagramma di bode di Ge
il file p3_mapping aggiunge le aree proibite dalle specifiche al diagramma di bode
il file p3_tuning crea il regolatore dinamico e apre il diagramma di bode di L
il file p4.py apre il grafico della simulazione lineare

ogni file chiama il precedente, quindi eseguire qualsiasi di questi file li esegue dall'inizio fino a quello scelto e stampa/apre il grafico solo relativi a quel punto

p3_tuning stampa anche le funzioni di trasferimento R e L
la R così ottenuta è stata copiata nel file prjB1.m alla riga 11

eseguire con matlab lo script prjB1.m mette nello stack di matlab i dati necessari per symulink
a questo punto si possono aprire i file symulink linear.slx e unlinear.slx, rispettivamente i test
sul sistema lineare e su quello non lineare
