#include <stdio.h>
#include <stdlib.h>
#include <math.h>


FILE *archivo;
FILE *archivo1;
double datx[42];
double daty[42];
double datx1[42];
double daty1[42];
double dat;
double dat1;



double darRadio(double x,double y, double xx, double yy);
double calcDistCuad(double x,double y, double xx, double yy);
double darRand();
//double darRandDistGauX();
//double darRandDistGauY();
double calcMax(double *arr);
double calcMin(double *arr);
void solver(double *x, double *y, char salida[]);


int main()
{
	int i,j,k;

	archivo = fopen("Canal_ionico.txt","r");
	for(i=0;i<42;i+=1){
		for(j=0;j<2;j+=1){
			fscanf(archivo,"%lf",&dat);
			if(j==0){
				datx[i] = dat;
			}

			else if(j==1){
				daty[i] = dat;
			}
		}
	}





	archivo1 = fopen("Canal_ionico1.txt","r");
	for(i=0;i<42;i+=1){
		for(j=0;j<2;j+=1){
			fscanf(archivo1,"%lf",&dat1);
			if(j==0){
				datx1[i] = dat1;
			}

			else if(j==1){
				daty1[i] = dat1;
			}
		}
	}



//Solver 1

	solver(datx,daty,"salida.txt");

//Solver 2

	solver(datx1,daty1,"salida1.txt");







	return 0;
}


double calcDistCuad(double x,double y, double xx, double yy){

	double a = x-xx;
	double b = y-yy;
	double resp = a*a+b*b;

	return resp;
}


double darRadio(double x,double y, double xx, double yy){

	double cal = 1.0;
	double resp = sqrt(calcDistCuad(x,y,xx,yy))-cal;

	return resp;
}


double darRand(double x, double y){

    	srand(time(NULL));
        double random = rand()*(x-y)/(RAND_MAX) +y;

	return random;
}

/*
double darRandDistGauX(){
	
	srand((unsigned int)time(NULL));
	double a = (double)rand()/(double)RAND_MAX;
	double aa = (double)rand()/(double)RAND_MAX;
	double randomx = sqrt(-2.0*log(a))*cos(aa*2*M_PI);

	return randomx;
	
	
}


double darRandDistGauY(){
	
	srand((unsigned int)time(NULL));
	double a = (double)rand()/(double)RAND_MAX;
	double aa = (double)rand()/(double)RAND_MAX;
	double randomy = sqrt(-2.0*log(a))*sin(aa*2*M_PI);

	return randomy;
	
	
}
*/


double calcMax(double *arr){
	
	int i,j,k;

	i=0;
	double temp = arr[0];
	while(i<42){
		if(arr[i]>temp){
			temp = arr[i];		
		}
		i +=1;
	}
	
        
        return temp;
}



double calcMin(double *arr){

	int i,j,k;
	i=0;
	double temp = arr[0];
	while(i<42){
		if(arr[i]<temp){
			temp = arr[i];		
		}
		i +=1;
	}
	
        
        return temp;
}




void solver(double *x, double *y, char salida[]){

	FILE *out = fopen(salida, "w+");
	double alpha, betha,R;
	int iteraciones = 200000;
	double *xw = malloc(iteraciones*sizeof(double));
	double *yw = malloc(iteraciones*sizeof(double));
	double *Rw = malloc(iteraciones*sizeof(double));
	double der = calcMax(x);
	double izq = calcMin(x);
	double arb = calcMax(y);
	double abj = calcMin(y);
	xw[0] = darRand(der,izq);
	yw[0] = darRand(arb,abj);
	Rw[0] = darRadio(xw[0], yw[0], x[0], y[0]);
	double xp =izq;
	double yp =abj;
	double Rp =izq;
	int i,j,k;

	k=1;
	while(k<42){
		R =darRadio(xw[0],yw[0],x[k],y[k]);
		if(R<Rw[0]){
			Rw[0] = R;
		}
		k +=1;

	}
	fprintf(out, "%f %f %f \n", xw[0], yw[0], Rw[0]);
	
	j=0;
	while(j<iteraciones){
		
/*Este pedazo del código lo tomé de la siguiente página. Por "este pedazo" me refiero a las siguientes 4 líneas y nada más. Fuente:  http://www.design.caltech.edu/erik/Misc/Gaussian.html
*/
                float a = (float)rand()/(float)RAND_MAX;
                float aa = (float)rand()/(float)RAND_MAX;
                float randomx = sqrt(-2.0*log(a))*cos(aa*2*M_PI);
                float randomy = sqrt(-2.0*log(a))*sin(aa*2*M_PI);

		//double randomx = darRandDistGauX();
		//double randomy = darRandDistGauY();
		xp = (randomx*1.0+xw[j]);
		yp = (randomy*1.0+xw[j]);

		if(izq<xp && der>xp && arb>yp && abj<yp){
			
			Rp = darRadio(xp, yp, x[0], y[0]);
			i=1;
			while(i<42){	
				R = darRadio(xp,yp,x[i], y[i]);
				if(R < Rp){					
					Rp = R;
				}
				i +=1;			
			}

			alpha = Rp/Rw[i];                                                                                            
                	if(alpha>=1.0){
                		xw[j+1]=xp;
                		yw[j+1]=yp;
                		Rw[j+1]=Rp;
                	}

                        else{
                   		betha = drand48();

                		if(betha<=alpha){		
                			xw[j+1]=xp;
                			yw[j+1]=yp;
                			Rw[j+1]=Rp;
                		}

                		else{
                			xw[j+1]=xw[j];
                			yw[j+1]=yw[j];
                			Rw[j+1]=Rw[j];
                		}	
                	}	
		}

		else{
			xw[j+1]=xw[j];
			yw[j+1]=yw[j];
			Rw[j+1]=Rw[j];
		}

		fprintf(out, "%f %f %f \n", xw[j+1], yw[j+1], Rw[j+1]);	
		j+=1;
	}

	fclose(out);	


}

