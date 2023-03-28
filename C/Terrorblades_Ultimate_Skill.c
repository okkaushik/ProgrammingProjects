#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//Terrablade's Ultimate Skill by 62070504030//

//define variables//
//Terrorblade's position//
float xT,yT;
//Enemy's position//
float xE,yE;
//define distance between two champions//
float d;
//define both champion's health//
float THP,EHP;


float distance(float d)
{
    d = sqrt((xE-xT)*(xE-xT)+(yE-yT)*(yE-yT));
    return d;
}


void swap(int a,int b)
{
    int temp;
    temp = THP;
    THP = EHP;
    EHP = temp;
    a = THP;
    b = EHP;
    return 0;
}


int main()
{
    printf("Terrorblade's Ultimate Skill!");

    //Enter Terrorblade's position//
    printf("\nEnter Terrorblade's current x-position:");
    scanf("%f",&xT);
    printf("Enter Terrorblade's current y-position:");
    scanf("%f",&yT);
    printf("Terrorblade's position (%f,%f)\n",xT,yT);

    //Enter Enemy's position//
    printf("\nEnter Enemy's current x-position:");
    scanf("%f",&xE);
    printf("Enter Enemy's current y-position:");
    scanf("%f",&yE);
    printf("Enemy's position (%f,%f)\n",xE,yE);

    //Show distance//
    d = distance(d);
    printf("\nDistance between the two champions are: %f\n",d);

    //Range condition//
    if(d<425){
    //Enter Terrorblade's HP//
    printf("\nEnter Terrorblade's current HP:");
    scanf("%f",&THP);
    printf("Enter Enemy's current HP:");
    scanf("%f",&EHP);
    swap(THP,EHP);

    printf("\nSunder is casted\n");

    //Display champions' HP after Sunder is casted//
    printf("\nTerrorblade's HP is now %f",THP);
    printf("\nEnemy's HP is now %f\n",EHP);
    } else {printf("\nCan't Sunder, too far!!!\n");}

return 0;
}


