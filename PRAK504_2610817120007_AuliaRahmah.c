#include <stdio.h>

int reverse(int n) {
    int hasil = 0;
    while (n > 0) {
        hasil = hasil * 10 + (n % 10);
        n = n / 10;
    }
    return hasil;
}

int main() {
    int A, B;
    scanf("%d %d", &A, &B);
    A = reverse(A);
    B = reverse(B);
    int C = A + B;
    printf("%d", reverse(C));
    return 0;
}