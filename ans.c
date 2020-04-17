#include <stdio.h>

void print(char* answers, int size) {
    for (int i = 0; i < size; i++) {
        printf("%c ", answers[i]);
    }
    printf("\n");
}

void correct_the_exam(char * answers, int size) {
    char s_answers[size];
    for (int i = 0; i < size; i++) {
        char n;
        printf("Enter student answer number %d\n", i + 1);
        scanf(" %c", &n); // input answer
        s_answers[i] = n;
    }
    int correct = 0;
    for (int i = 0; i < size; i++) {
        if (s_answers[i] == answers[i]) {
            correct += 1;
        }
    }
    printf("Number of correct answers: %d\n", correct);
    printf("Number of wrong answers: %d\n", size - correct);

    printf("Percentage: %f \n", (float)(correct * 100)/size);
}

int main(void) 
{
    int NUM = 10;
    char answers[NUM];
    for (int i = 0; i < NUM; i++) {
        char n;
        printf("Enter answer number %d\n", i + 1);
        scanf(" %c", &n); // input answer
        answers[i] = n;
    }
    int choice;
    do {
        printf("1. Correct the exam.\n");
        printf("2. Print the answers.\n");
        printf("3. Exit\n");
        scanf("%d", &choice);
        if (choice == 1) {
            correct_the_exam(answers, NUM);
        } else if (choice == 2) {
            print(answers, NUM);
        } else if (choice == 3) {
            printf("Exiting...\n");
        }
        else {
            printf("Invalid Input. Retry!");
        }
    } while (choice != 3);
}  
