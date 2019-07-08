#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <malloc.h>
//#include <sys/wait.h>
//#include <unistd.h>
#include <math.h>

void main(int argc, char *argv[])
{

    printf ("booting up...\n");

    printf ("enter command\nfor list of commands enter 'help'\n");

    while (1)
    {
        char cmd[100], opr[10], arg1[10], arg2[10];
        const char delim[2] = " ";
        char *token;
        printf(">");
        fgets(cmd,100,stdin);
        token = strtok(cmd, delim);
        int i=0;

        while( token != NULL ) 
        {
            if(i==0) 
            {
                strcpy(opr, token);
            } 
            else if(i==1) 
            {
                strcpy(arg1, token);
            }
            else if(i==2) 
            {
                strcpy(arg2, token);
            }
            i++;
            token = strtok(NULL, delim);
        }

        if(strcmp(opr , "help")==0)
        {
            printf("add = adds of two numbers\nsub = subtracts the second number from the first\nmul = multiplies two numbers together\ndiv = divides the first number by the second\npow = raise the first number to the power of the second\n");
        }
        else if(strcmp(opr , "add")==0)
        {
            float a;
            a = atoi(arg1) + atoi(arg2);
            printf("%f\n", a);
        }
        else if(strcmp(opr , "sub")==0)
        {
            float a;
            a = atoi(arg1) - atoi(arg2);
            printf("%f\n", a);
        }
        else if(strcmp(opr , "div")==0)
        {
            float a;
            a = (float) atoi(arg1)/atoi(arg2);
            printf("%.2f\n", a);
        }
        else if(strcmp(opr , "mul")==0)
        {
            float a;
            a = atoi(arg1)*atoi(arg2);
            printf("%f\n", a);
        }
        else if(strcmp(opr , "pow")==0)
        {
            float a;
        
            printf("%d, %d \n", (int) atoi(arg1), (int) atoi(arg2));
            a = pow(atoi(arg1), atoi(arg2));
            printf("%f\n", a);
        }
    }
}
