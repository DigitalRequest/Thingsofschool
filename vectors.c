#include <stdio.h>

int main()
{
    int size; // Size of the vectors

    // User input for vectors size
    printf("Please enter the size of both vectors: ");
    scanf("%d", &size);

    int a[size], b[size], c[size]; // Vector for store numbers

    // User input - vector a
    for (int i = 0; i < size; i++)
    {
        printf("Please enter the %d element of vector a: ", i + 1);
        scanf("%d", &a[i]);
    }

    printf("\nNow the same with vector b:\n\n");

    // User input - vector b
    for (int i = 0; i < size; i++)
    {
        printf("Please enter the %d element of vector b: ", i + 1);
        scanf("%d", &b[i]);
    }

    printf("\nStarting the sum of vectors: ...\n\n");

    // Data processing, creating vector c by sum of vector a and vector b
    for (int i = 0; i < size; i++)
    {
        c[i] = a[i] + b[i];
    }

    // Output, Show all elements of all vectors
    printf("Summing finished, now showing all the vectors:\n");
    printf("Elements in vector a are: ");
    for (int i = 0; i < size; i++)
    {
        if (i < size - 1)
        {
            printf("%d, ", a[i]);
        }
        else
        {
            printf("%d.\n", a[i]);
        }
    }
    printf("Elements in vector b are: ");
    for (int i = 0; i < size; i++)
    {
        if (i < size - 1)
        {
            printf("%d, ", b[i]);
        }
        else
        {
            printf("%d.\n", b[i]);
        }
    }
    printf("Elements in vector c are: ");
    for (int i = 0; i < size; i++)
    {
        if (i < size - 1)
        {
            printf("%d, ", c[i]);
        }
        else
        {
            printf("%d.\n", c[i]);
        }
    }

    return 0;
}