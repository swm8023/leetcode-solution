/*
 Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:

Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

*/

/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
 #define UNODE UndirectedGraphNode
class Solution {
public:
    map<UNODE*, UNODE*>::iterator iter;
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.

        map<UNODE*, UNODE* > nodeMap;
        if (node == NULL) return node;
        UNODE *nnode = new UNODE(node->label);
        nodeMap[node] = nnode;
        dfsGraph(nodeMap, node, nnode);
        return nnode;
    }
    void dfsGraph(map<UNODE*, UNODE*> &nodeMap, UNODE *node, UNODE *nnode) {
        for (int i = 0; i < node->neighbors.size(); i++) {
            UNODE *now = node->neighbors[i];
            if ((iter = nodeMap.find(now)) != nodeMap.end()) {
                 nnode->neighbors.push_back(iter->second);
            } else {
                UNODE *nnow = new UNODE(now->label);
                nodeMap[now] = nnow;
                nnode->neighbors.push_back(nnow);
                dfsGraph(nodeMap, now, nnow);
            }
        }
    }
};
