/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point> &points) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int size = points.size();
        int ans = 0, horz, same;
        map<double, int> mp;
        map<double, int>::iterator it;
        for (int i = 0; i < size; i++) {
            mp.clear(); horz = same = 0;
            for (int j = 0; j < points.size(); j++) {
                if (points[j].x == points[i].x && points[j].y == points[i].y) same++;
                else if (points[j].x == points[i].x) horz ++;
                else mp[(points[j].y-points[i].y)*1.0/(points[j].x-points[i].x)]++;
            }
            if (horz + same > ans) ans = horz + same;
            for (it = mp.begin(); it != mp.end(); it++)
                if (it->second + same > ans) ans = it->second + same;
        }
        return ans;
    }
};
