%module example

%{
#include "example.h"
%}

extern double value;
extern int fact(int n);
extern int my_mod(int x, int y);
extern char *get_time();