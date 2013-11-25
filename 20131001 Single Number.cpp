class Solution {
public:
    int singleNumber(int A[], int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int x = 0;
        while (--n >= 0) x ^= A[n];
        return x;
    }
};
