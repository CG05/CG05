#include <stdio.h>
int main_print_scan(void)
{
  char name[256];
  printf("NAME? : ");
  scanf("%s", name, sizeof(name));

  int age;
  printf("AGE? : ");
  scanf("%d", &age);

  float weight;
  printf("WEIGHT? : ");
  scanf("%f", &weight);

  double tall;
  printf("TALL? : ");
  scanf("%lf", &tall);

  char what[256];
  printf("WHAT CRIME? : ");
  scanf("%s", what, sizeof(what));

  printf("\n\nINFO OF CRIMINA\n");
  printf("NAME : %s\n", name);
  printf("AGE : %d\n", age);
  printf("WEIGHT : %f.1\n", weight);
  printf("TALL : %.2lf\n", tall);
  printf("WHAT CRIME : %s\n", what);

  return 0;
}