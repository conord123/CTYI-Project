#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <sys/wait.h>
#include <unistd.h>

void main(int argc, char *argv[])
{

    printf ("booting up...\n");

    printf ("enter command\n for list of commands enter 'help'\n>");

    while (1)
    {
        char opr[20], cmd[10], arg1[10], arg2[10];
        printf(">");
        gets(opr);
        char token = strtok(opr, " ");

        while( token != NULL ) 
        {
            int i=0;

            if(i==0) 
            {
                strcpy(cmd, token);
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
            token = strtok(NULL, " ");
        }
        if(strcmp(opr , "add")==0)
        {
            int a;
            a = atoi(argv[1]) + atoi(argv[2]);
            printf("%d", a);
        }
    }
    
}