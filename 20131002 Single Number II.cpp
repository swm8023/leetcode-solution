class Solution {
public:
    int singleNumber(int A[], int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int x[3] = {0};
        while (--n >= 0) {
            x[2] = x[1] & A[n];
            x[1] |= x[0] & A[n];
            x[0] |= A[n];
            x[0] &= ~x[2], x[1] &= ~x[2];
        }
        return x[0];
    }
};
