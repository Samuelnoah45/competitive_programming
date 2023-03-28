var compress = function(chars) {
    let start = 0, end = 0;
    while (end < chars.length) {
        if (chars[end] == chars[end+1]) end++;
        else {
            let len = end-start+1; // number of letters
            if (len == 1) {
                start++, end++;
                continue;
            }
            
            chars.splice(start+1, len-1, ...len.toString().split(""));
            end -= len - 1 - len.toString().length; 
            // move backwards as much as the number of letters 
            // except for one letter char and length chars
            
            start = end; // bring start pointer to end pointer
            start++, end++; // move both pointers to new letter
        }
    }
    return chars.length;
    // One Pass
    // Two Pointer
    // Time Complexity: O(n)
    // Space Complexity: O(1)
};