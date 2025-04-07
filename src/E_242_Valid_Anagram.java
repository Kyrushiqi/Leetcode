/*
Question: https://leetcode.com/problems/valid-anagram/
Submission: https://leetcode.com/problems/valid-anagram/submissions/1599264711/

First Logic:
Create 2 hashmaps to store key value pairs (Character & int) of String s and String t.
Compare the two hashmaps by keys and values.
*/
import java.util.HashMap;

class E_242_Valid_Anagram {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sMap = new HashMap<>(s.length());
        HashMap<Character, Integer> tMap = new HashMap<>(s.length());
        boolean result = false;

        if(s.length() != t.length()){
            return false;
        }

        // Put String s into a Hashmap
        for(int i = 0; i < s.length(); i++){
            if(sMap.containsKey(s.charAt(i))){
                sMap.replace(s.charAt(i), sMap.get(s.charAt(i))+1);
            } else {
                sMap.put(s.charAt(i), 1);
            }
        }
        // Put String t into a Hashmap
        for(int i = 0; i < t.length(); i++){
            if(tMap.containsKey(t.charAt(i))){
                tMap.replace(t.charAt(i), tMap.get(t.charAt(i))+1);
            } else {
                tMap.put(t.charAt(i), 1);
            }
        }

        // Compare the two HashMaps by Key and Value
        for(int j = 0; j < sMap.size(); j++){
            for(Character e: sMap.keySet()){
                if(!tMap.containsKey(e)){ // Does tMap contain the same Keys as sMap?
                    return false;
                } else {
                    if(sMap.get(e).equals(tMap.get(e))){ // Does sMap's values equal tMap's values?
                        result = true;
                    } else {
                        return false;
                    }
                }
            }

            /* s = KLqr..., t = qKrL...
            sMap        tMap
            K | 2       q | 3
            L | 4       K | 10
            q | 3       r | 24
            r | 32      L | 4
            */
        }

        return result;
    }
}