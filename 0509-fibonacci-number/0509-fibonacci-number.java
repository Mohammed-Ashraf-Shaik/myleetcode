class Solution {
    public int fib(int n) {
        if(n==0){
        return 0;
        }
        else if(n==1){
            return 1;
            }
            int fn=0;
            int sn=1;
            for(int i=0;i<n;i++){
            int tn=fn+sn;
            fn=sn;
            sn=tn;
            }
        return fn;
    }
    }