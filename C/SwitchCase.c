#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define pi 3.1415926535898

int main()
{
    printf("Hello! This program will do one of the following tasks for you.\n");
    printf("1. Calculate the Area of a Circle, when 0<radius<50 is given.\n");
    printf("2. Calculate the Quadratic Equation Roots, a*x^2+b*x+c = 0, when a, b, and c are given.\n");
    printf("3. Return whether the given input integer an Odd or Even number.\n");
    printf("4. Sort 3 numbers (minimum to maximum).\n");

    int CaseNumber;
    float Radius,Area;                  // used in Case 1

    int a,b,c,out1,out2,out3;
    float x1,x2,Discriminant;     // used in Cases 2, 4

    int Integer;                        // used in Case 3


    printf("Enter a case number (1, 2, 3, 4): ");
    scanf("%i", &CaseNumber);

    switch(CaseNumber)
    {
        case 1:
            printf("You have entered 1. Calculate the Area of a Circle.\n");
            printf("Enter the radius, where 0<radius<50.\n");
            printf("Radius : ");
            scanf("%f",&Radius);
            if(Radius>0 && Radius<50)
            {
                Area = pi*Radius*Radius;
                printf("The Area of the circle with radius %f is %f.\n", Radius, Area);
            }
            else
            {
                printf("You did not enter a suitable value for the radius.\n");
            }
            break;

        case 2:
            printf("You have entered 2. Calculate the roots of the Quadratic Equation, a*x^2+b*x+c = 0.\n");
            printf( "a : ");
            scanf("%d",&a);
            printf( "b : ");
            scanf("%d",&b);
            printf( "c : ");
            scanf("%d",&c);
            Discriminant = b*b-4*a*c;
            if  (Discriminant < 0)
            {
                printf("\n The Quadratic Equation %d x^2 + %d x + %d = 0 has no real roots.", a, b, c);
            }
            else if   (Discriminant == 0)
            {
                x1 = -b/2/a;
                printf("\n The Quadratic Equation %d x^2 + %d x + %d = 0 has repeated real roots x1 = x2 = %.2f.", a, b, c, x1);
            }
            else if   (Discriminant > 0)
            {
                x1 = -b/2/a-sqrt(b*b-4*a*c)/2/a;
                x2 = -b/2/a+sqrt(b*b-4*a*c)/2/a;
                printf("\n The Quadratic Equation %d x^2 + %d x + %d = 0 has distinct real roots x1 = %.2f, x2 = %.2f.", a, b, c, x1, x2);
            }
            break;

        case 3:
            printf("You have entered 3. Return whether the given input integer an Odd or Even number.\n");
            printf("Enter an integer.\n");
            printf("Integer : ");
            scanf("%d",&Integer);
            if (Integer%2 == 0)
            {
                printf("%d is Even.\n", Integer);
            }
            else
            {
                printf("%d is Odd.\n", Integer);
            }
            break;

        case 4:
            printf("You have entered 4. Sort 3 numbers (minimum to maximum).\n");
            printf("Enter 3 real numbers, a, b, and c.\n");
            printf("a : ");
            scanf("%d",&a);
            printf("b : ");
            scanf("%d",&b);
            printf("c : ");
            scanf("%d",&c);
            if ((a <= b) && (b <= c))
            {
                out1 = a;
                out2 = b;
                out3 = c;
            }
            else if ((a <= c) && (c <= b))
            {
                out1 = a;
                out2 = c;
                out3 = b;
            }
            else if ((b <= a) && (a <= c))
            {
                out1 = b;
                out2 = a;
                out3 = c;
            }
            else if ((b <= c) && (c <= a))
            {
                out1 = b;
                out2 = c;
                out3 = a;
            }
            else if ((c <= a) && (a <= b))
            {
                out1 = c;
                out2 = a;
                out3 = b;
            }
            else if ((c <= b) && (b <= a))
            {
                out1 = c;
                out2 = b;
                out3 = a;
            }
            printf("%d, %d, %d in increasing order is %d, %d, %d", a, b, c, out1, out2, out3);
            break;

        /* CaseNumber doesn't match any case constant 1, 2, 3, 4 */
        default:
            printf("Error! Case number is incorrect.");
            break;
    }
    return 0;
}
