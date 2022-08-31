class Solution {
public:
    bool isCycle(int n, vector<bool>& taken, vector<bool>& visited,  map<int, vector<int>>& graph){
        if (taken[n]){
            return false;
        }
        if(visited[n]){
            return true;
        }
        visited[n] = true;
        for (auto prereq: graph[n]){
            if (isCycle(prereq, taken, visited, graph)){
                return true;
            }
        }
        taken[n] = true;
        visited[n] = false;
        return false;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        map<int, vector<int>> graph;
        vector<bool> visited(numCourses, false);
        vector<bool> taken(numCourses, false);
        
        for (int i= 0; i<prerequisites.size(); ++i){
            graph[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }
        
        for (int i=0; i < numCourses; ++i){
            if (isCycle(i, taken, visited, graph)){
                return false;
            }
        }
        
       return true;
        
        
        
    }
};