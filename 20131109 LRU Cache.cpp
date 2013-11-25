#include <map>
using namespace std;
class Node{
public:
    int key, val;
    Node *pre, *next;
    Node(int k, int v): key(k), val(v), pre(NULL), next(NULL) {}
};
class LRUCache{
    map<int, Node*> mp;
    map<int, Node*>::iterator iter;
    int used, cap;
    Node *head, *tail;
public:
    LRUCache(int capacity) {
        mp.clear();
        used = 0, cap = capacity;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail, tail->pre = head;
    }
    ~LRUCache(){
        for (Node *n = head, *nnext; n; n = nnext) {
            nnext = n->next;
            delete n;
        }
    }

    int get(int key) {
        if ((iter = mp.find(key)) != mp.end()) {
            movetoFirst(iter->second);
            return iter->second->val;
        }else
            return -1;
    }

    void set(int key, int value) {
        if ((iter = mp.find(key)) != mp.end()) {
            iter->second->val = value;
            movetoFirst(iter->second);
        } else {
            Node *node;
            if (used == cap) {
                mp.erase(tail->pre->key);
                node = tail->pre;
                node->key = key, node->val = value;
            } else {
                node = new Node(key, value);
                used++;
            }
            mp[node->key] = node;
            movetoFirst(node);
        }
    }
    void movetoFirst(Node *node) {
        if (node->pre && node->next) {
            node->pre->next = node->next;
            node->next->pre = node->pre;
        }
        node->pre = head, node->next = head->next;
        head->next->pre = node, head->next = node;
    }

};
