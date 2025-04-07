/*
Question: https://leetcode.com/problems/valid-anagram/
First Logic: Use a hashmap to store key value pairs (String & int) and use it to map out string s.
Then make t into a hashmap and compare the two hashmaps.

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

        for(int i = 0; i < s.length(); i++){
            if(sMap.containsKey(s.charAt(i))){
                sMap.replace(s.charAt(i), sMap.get(s.charAt(i))+1);
            } else {
                sMap.put(s.charAt(i), 1);
            }
        }

        for(int i = 0; i < t.length(); i++){
            if(tMap.containsKey(t.charAt(i))){
                tMap.replace(t.charAt(i), tMap.get(t.charAt(i))+1);
            } else {
                tMap.put(t.charAt(i), 1);
            }
        }

        for(int j = 0; j < sMap.size(); j++){
            for(Character e: sMap.keySet()){
                if(!tMap.containsKey(e)){
                    result = false;
                    return false;
                } else {
                    if(sMap.get(e).equals(tMap.get(e))){
                        result = true;
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

//            if(!(sMap.containsKey(s.charAt(j)) && tMap.containsKey(s.charAt(j)))){
//                result = false;
//                return false;
//            } else {
//                if(sMap.get(s.charAt(j)).equals(tMap.get(s.charAt(j)))){
//                    result = true;
//                }
//            }
        }

        return result;
    }
}