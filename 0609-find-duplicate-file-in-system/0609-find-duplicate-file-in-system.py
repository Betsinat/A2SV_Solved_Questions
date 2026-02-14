class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}
        for path in paths:
            #split each path by using space
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                name , content = file_info.split("(")
                content = content[:-1]
                full_path = directory + "/" + name
                if content not in content_map:
                  content_map[content] = []
                content_map[content].append(full_path)

        result = []
        for files in content_map.values():
            if len(files) > 1:
                result.append(files)
        return result



        

    
            
        