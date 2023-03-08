class Solution:
    def simplifyPath(self, path: str) -> str:

        path_stack = []
        arr = path.split("/")
       
        for dirs in arr:
            if dirs == "..":
               if path_stack:
                   path_stack.pop()
            elif dirs !=""  and dirs !='.':
                path_stack.append(dirs)
                
        ans = "/" + "/".join(path_stack)

        return  ans