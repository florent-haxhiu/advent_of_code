#include <stdio.h>
#include <stdlib.h>

int main(void) 
{
  FILE *fp = fopen("testdata", "r");
  if (fp == NULL) 
  {
    perror("Unable to open file");
    exit(1);
  }

}
