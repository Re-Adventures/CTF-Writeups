#include <time.h>
#include <stdio.h>
#include <stdlib.h>
int main(void){
  srand(0);
  // printf("[");
  for(int i=0; i<23469; ++i){
    printf("%i,", rand()%4);
  }
  // printf("]\n");
  return 0;
}


