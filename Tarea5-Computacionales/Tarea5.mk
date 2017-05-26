Resultados_hw5.pdf : *.jpg *.png Resultados_hw5.tex
	pdflatex Resultados_hw5.tex

%.jpg : *.txt circuitoRC.py
	python circuitoRC.py 

%.png : *.txt plots_canal_ionico.py circuitoRC.py 
	python plots_canal_ionico.py
	
%.txt : a.out
	./a.out

a.out : canal_ionico.c 
	gcc -lm canal_ionico.c 
