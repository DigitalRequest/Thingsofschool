#include <stdio.h>

int main()
{
    int row, col; // Number of rows and columns in matrix

    // User-Input for num of columns and rows
    printf("Please enter how much rows the matrix have: ");
    scanf("%d", &row);
    printf("Please enter how much colomns the matrix have: ");
    scanf("%d", &col);

    int matrix[col][row];     // Matrix provided by user
    int transposed[row][col]; // The transposed matrix provided by user

    // Loop for user-input of matrix
    for (int i = 0; i < col; i++)
    {
        for (int j = 0; j < row; j++)
        {
            printf("Please enter the element in %dx%d: ", i, j);
            scanf("%d", &matrix[i][j]);
        }
    }

    // Data Processing - Create the transposed matrix of user-input matrix
    for (int i = 0; i < col; i++)
    {
        for (int j = 0; j < row; j++)
        {
            transposed[j][i] = matrix[i][j];
        }
    }

    // Output - Show original matrix to user
    printf("Your matrix is:\n");
    for (int i = 0; i < col; i++)
    {
        for (int j = 0; j < row + 1; j++)
        {
            if (j < row)
            {
                printf("%d ", matrix[i][j]);
            }
            else
            {
                printf("\n");
            }
        }
    }

    // Output - Show the transposed matrix that the user-inputted
    printf("The transposed matrix is:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col + 1; j++)
        {
            if (j < col)
            {
                printf("%d ", transposed[i][j]);
            }
            else
            {
                printf("\n");
            }
        }
    }

    return 0;
}