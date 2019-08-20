
//Find the Kth Row in Pascal Triangle.


public ArrayList<Integer> getRow(int A) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int c = 1;
        result.add(1);
        for(int i =1; i<=A;i++){
            result.add((c*(A-i+1))/i);
            c = (c*(A-i+1))/i;
        }
        
        return result;
    }
