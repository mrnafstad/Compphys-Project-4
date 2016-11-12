#include <stdio.h>
#include <math.h>
#include "lib.h"

inline int periodic(int i, int limit, int add){
	return (i+limit+add) % limit;	
}

void Metropolis(int n_spins, long& idum, int **spin_matrix, double& E, double& M, double *w, int& accepted){

	for(int x = 0; x < n_spins; x++){
		for(int y = 0; y < n_spins; y++){

			int ix = (int) (ran1(&idum)*double(n_spins));
			int iy = (int) (ran1(&idum)*double(n_spins));
			int deltaE = 2*spin_matrix[ix][iy]*\
			(spin_matrix[ix][periodic(iy, n_spins, -1)] +\
			spin_matrix[periodic(ix, n_spins, -1)][iy] +\
			spin_matrix[ix][periodic(iy, n_spins, 1)] +\
			spin_matrix[periodic(ix, n_spins, 1)][iy]);

			if (ran1(&idum) <= w[deltaE+8]){
				spin_matrix[ix][iy] *= -1;
				M += (double) 2*spin_matrix[ix][iy];
				E += (double) deltaE;
				accepted += 1;
			}
		}
	}
}

void initialize(int n_spins, double temp, int **spin_matrix, double& E, double& M, long & idum, bool randomdistribution){
	for(int x = 0; x < n_spins; x++){
		for(int y = 0; y < n_spins; y++){
			//if (temp < 1.5)
			if (randomdistribution) { 
				if (ran1(&idum) <= 0.5) spin_matrix[x][y] = 1;
				else spin_matrix[x][y] = -1;
			}
			else {
				spin_matrix[x][y] = 1;
				M += (double) spin_matrix[x][y];
			}
		}
	}

	for(int x = 0; x < n_spins; x++){
		for(int y = 0; y < n_spins; y++){
			E -= (double) spin_matrix[x][y]*\
			(spin_matrix[periodic(x, n_spins, -1)][y] +\
			spin_matrix[x][periodic(y, n_spins, -1)]);
		}
	}	
}


void output(int n_spins, int mcs, double temp, double *average){
	double norm = 1.0/ (double) (mcs);
	double Eaverage = average[0]*norm;
	double E2average = average[1]*norm;
	double Maverage = average[2]*norm;
	double M2average = average[3]*norm;
	double Mabsaverage = average[4]*norm;
	double Suscept = (M2average - Maverage*Maverage)/temp/n_spins/n_spins;
	double Cv = (E2average - Eaverage*Eaverage)/(temp*temp)/n_spins/n_spins;

	double Evariance = (E2average - Eaverage*Eaverage)/n_spins/n_spins;
	double Mvariance = (M2average - Maverage*Maverage)/n_spins/n_spins;



	printf("Spins: %i, MC-cycles: %i, Temperature: %.2lf\n", n_spins, mcs, temp);
	printf("Expectation Values:\n");
	printf("<E> = %f\n", Eaverage);
	printf("<M> = %f\n", Maverage);
	printf("<E2> = %f\n", E2average);
	printf("<M2> = %f\n", M2average);
	printf("<|M|> = %f\n", Mabsaverage);
	printf("E_variance = %f\n", Evariance);
	printf("M_variance = %f\n", Mvariance);
	printf("Chi = %f\n", Suscept);
	printf("Cv = %f\n\n", Cv);

}

void probabilities(double E, double *Energies, int *Counters, int lengthArrays, int *no_En){
	bool En_found = false;

	for(int i = 0; i < lengthArrays; i++){
		if(E == Energies[i]){
			Counters[i] += 1;
			En_found = true;
			break;
		}
	}
	if(!En_found){
		*no_En += 1;
		Energies[*no_En] = E;
		Counters[*no_En] += 1;
	}
	
}

int main(int argc, char* argv[]){

	long idum;
	int **spin_matrix, n_spins, mcs, accepted;
	double w[17], average[5], initial_temp, final_temp, E, M, temp_step;
	bool randomdistribution = false;	


	n_spins = atoi(argv[1]);
	mcs = pow(10, atoi(argv[2]));
	initial_temp = atof(argv[3]);
	final_temp = atof(argv[4]);
	temp_step = atof(argv[5]);

	spin_matrix = (int**) matrix(n_spins, n_spins, sizeof(int));

	//Open file to write final values
	FILE *means;
	char MeanOut[25];
	snprintf(MeanOut, sizeof(MeanOut), "meanvalues_%.2lf.txt", (double) n_spins);
	means = fopen(MeanOut, "w+");


	for(double temp = initial_temp; temp <= final_temp; temp += temp_step){

		char outfile[20];
		snprintf(outfile, sizeof(outfile), "T_%.2lf.txt", temp);

		FILE *fp;
		fp = fopen(outfile, "w+");

		idum = -1;
		E = M = 0;
		accepted = 0;


		for(int de = -8; de <= 8; de++) w[de+8] = 0;
		for(int de = -8; de <= 8; de += 4) w[de+8] = exp(-de/temp);

		for(int i = 0; i < 5; i++) average[i] = 0.;

		initialize(n_spins, temp, spin_matrix, E, M, idum, randomdistribution);
		fprintf(fp, "%i %lf %lf %i \n", 0, E, M, accepted);


		//----------------------------------
		double *Energies;
		int *Counters, lengthArrays = 1000, no_En = 0;
		no_En = 0;

		Energies = new double [lengthArrays];
		Counters = new int [lengthArrays];

		for(int i = 0; i < lengthArrays; i++){
			Energies[i] = 0;
			Counters[i] = 0;
		}
		//------------------------------------



		int counter = 1;

		for(int cycles = 1; cycles <= mcs; cycles++){
			Metropolis(n_spins, idum, spin_matrix, E, M, w, accepted);
			average[0] += E; average[1] += E*E;
			average[2] += M; average[3] += M*M; average[4] += fabs(M);

			if(cycles >= 2500) probabilities(E, Energies, Counters, lengthArrays, &no_En);

			if(counter <= 10000){
				fprintf(fp, "%i %lf %lf %i\n", cycles, average[0]/cycles, average[4]/cycles, accepted);
			}
			counter += 1;
		}

		//...........................................
		FILE *pr;
		char ProbOut[25];
		snprintf(ProbOut, sizeof(ProbOut), "Prob_%.2lf.txt", temp);


		pr = fopen(ProbOut, "w+");

		for(int i = 0; i <= lengthArrays; i++){
			if(Counters[i] != 0.0){
				fprintf(pr, "%f %i\n", Energies[i], Counters[i]);
			}
		}

		fclose(pr);
		//-----------------------------------------------

		output(n_spins, mcs, temp, average);

		double norm = 1.0/ (double) (mcs);
		double Eaverage = average[0]*norm;
		double E2average = average[1]*norm;
		double Maverage = average[2]*norm;
		double M2average = average[3]*norm;
		double Mabsaverage = average[4]*norm;
		double Suscept = (M2average - Maverage*Maverage)/temp/n_spins/n_spins;
		double Cv = (E2average - Eaverage*Eaverage)/(temp*temp)/n_spins/n_spins;

		//write final values
		fprintf(means, "%f %f %f %f %f\n", temp, Eaverage, Mabsaverage, Cv, Suscept);

		delete[] Energies; delete[] Counters;

		fclose(fp);
	}

	fclose(means);

	free_matrix((void **) spin_matrix);

	return 0;
}