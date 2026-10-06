class MyHashMap {
    int []arr;
    boolean []exist;
    public MyHashMap() {
        arr = new int[1_000_001];
        exist = new boolean[1_000_001];
    }
    
    public void put(int key, int value) {
        arr[key] = value;
    exist[key] = true;
    }
    
    public int get(int key) {
        if (exist[key] == false){
            return -1;
        }
        return arr[key];
    }
    
    public void remove(int key) {
        if (exist[key] == false){
            return;
        }
        exist[key]=false;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */