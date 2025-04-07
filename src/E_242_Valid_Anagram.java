/*
First Logic: Use a hashmap to store key value pairs (String & int) and use it to map out string s. Then make t into a hashmap and compare the two hashmaps.
*/
import java.util.HashMap;

class E_242_Valid_Anagram {
    public boolean isAnagram(String s, String t) {
        HashMap sMap = new HashMap(s.length());
        HashMap tMap = new HashMap(s.length());

        if(s.length() != t.length()){
            return false;
        }

        return true;
    }
}