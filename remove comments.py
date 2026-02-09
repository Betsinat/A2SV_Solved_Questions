class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        result = []
        in_block = False
        buffer = []
        for line in source:
            i = 0
            while i < len(line):
                
                if in_block:
                    if i + 1 < len(line) and line[i] =="*" and line[i+1]=="/":
                        in_block = False
                        i+=2
                    else:
                            i+=1
                else:
                   
                    if i + 1 < len(line) and line[i] == "/" and line[i+1]=="*":
                        in_block = True
                        i+=2
                
                    elif i + 1 < len(line) and line[i] == "/" and line[i+1] == "/":
                        break
                    else:
                        buffer.append(line[i])
                        i += 1
            if not in_block and buffer:
                result.append("".join(buffer))
                buffer = []
        return result
        
