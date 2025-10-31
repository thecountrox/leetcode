class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;
        queue<pair<int,int>> rooten;
        int m=grid.size(),n=grid[0].size(),days=0,cnt,tot_cnt=0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==2) rooten.push({i,j});
                if(grid[i][j]!=0) tot_cnt++;
            }
        }
        int dx[4]={0,0,-1,1};
        int dy[4]={1,-1,0,0};
        int nx,ny;
        cnt=0;
        int k;
        while(!rooten.empty()){
            k=rooten.size();
            cnt+=k;
            while(k--){
                int x=rooten.front().first;
                int y=rooten.front().second;
                rooten.pop();
                for(int i=0;i<4;i++){
                    nx=x + dx[i];
                    ny=y + dy[i];

                if ( nx>=m or ny>=n or nx<0 or ny<0 or grid[nx][ny]!=1) continue ;
                grid[nx][ny]=2;
                rooten.push({nx,ny});

                }
            }
            if(!rooten.empty()) days++;
        }
        if(tot_cnt==cnt){
            return days ;
        }
        return -1;
    }
};
