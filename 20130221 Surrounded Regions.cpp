/*
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region .

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
*/
class Solution {
public:
    void solve(vector<vector<char> > &board) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        queue<pair<int, int> > q;
        int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
        if (board.size() == 0) return ;
        int lenh = board.size(), lenw = board[0].size();
        for (int i = 0; i < lenh; i++)
            for (int j = 0; j < lenw; j++)
                if ((i == 0 || j == 0 || i == lenh - 1 || j == lenw - 1)
                        && board[i][j] == 'O') {
                    board[i][j] = 'Y';
                    q.push(make_pair(i, j));
                }
        while (!q.empty()) {
            pair<int, int> p = q.front(); q.pop();
            for (int i = 0; i < 4; i++) {
                int ni = p.first + dx[i], nj = p.second + dy[i];
                if (ni >= 0 && ni < lenh && nj >= 0 && nj < lenw
                    && board[ni][nj] == 'O') {
                    board[ni][nj] = 'Y';
                    q.push(make_pair(ni, nj));
                }
            }
        }
        for (int i = 0; i < lenh; i++)
            for (int j = 0; j < lenw; j++)
                board[i][j] = (board[i][j] == 'Y' ? 'O' : 'X');
    }
};
