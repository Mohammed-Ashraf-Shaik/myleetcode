class Solution {
    public int tribonacci(int n) {
        if(n==0)
        return 0;
        else if(n==1){
        return 1;
    }
    else{
        int fn=0,sn=1,tn=1;
        for(int i=0;i<n;i++){
           int ftn=fn+sn+tn;
            fn=sn;
            sn=tn;
            tn=ftn;
        }
        return fn;
    }
    }
}