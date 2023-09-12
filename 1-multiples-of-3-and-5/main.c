/*
Question:

If we list all the natural numbers below that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Solution:

The multiplies of 3 or 5 have a repeating pattern every 7 numbers, as shown below:

3, 5, 6, 9, 10, 12, 15, 3+15, 5+15, ..., 15+15, 3+15*2, ...

The multiples below 1000 have 66 complete such groups plus 1 incomplete group (993, 995, 996, 999), so the sum is:

66*(3+5+6+9+10+12+15) + 15*7*(1+2+...+65) + (993+995+996+999)
   ------------------        ------------   -----------------
           a                      b                 c
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int a = 3 + 5 + 6 + 9 + 10 + 12 + 15;
    int b = 65 * 66 / 2;
    int c = 993 + 995 + 996 + 999;
    int sum = 66 * a + 15 * 7 * b + c;
    printf("%d\n", sum);
    return 0;
}
