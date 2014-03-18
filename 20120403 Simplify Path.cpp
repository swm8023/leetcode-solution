/*
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
*/
class Solution {
public:
    string simplifyPath(string path) {
        //cout << "here" << endl;
        vector<string> resVec;
        string ans = "";
        int pos = 0, rpos;
        while ((rpos = path.find("/", pos+1)) != string::npos) {
            resVec.push_back(path.substr(pos, rpos-pos));
            cal(resVec);
            pos = rpos;
        }
        resVec.push_back(path.substr(pos));
        cal(resVec);
        if (resVec.size() == 0) resVec.push_back("/");
        for (auto &s: resVec) ans.append(s);
        return ans;
    }
    void cal(vector<string> &vec) {
        string s = vec[vec.size() - 1];
        if (s == "/" || s == "/.") {
            vec.pop_back();
        } else if (s == "/..") {
            vec.pop_back();
            if (vec.size()) vec.pop_back();
        }
    }
};