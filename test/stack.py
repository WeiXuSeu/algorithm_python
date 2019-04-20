class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = None
        if path is None or path[0] != '/':
            return result
        index = 0
        size = len(path)
        stack = []
        stack.append(path[index])
        index += 1
        while index < size:
            slash_index = index
            while slash_index < size and path[slash_index] != '/':
                slash_index += 1
            # //
            if slash_index == index:
                index = index + 1
            # /./, /../
            elif slash_index > index:
                sub_str = path[index:slash_index]
                if sub_str == ".":
                    index = index + 3
                elif sub_str == "..":
                    index = index + 4
                    while len(stack) > 1:
                        stack.pop()
                        if stack[-1] == '/':
                            break
                else:
                    index = slash_index + 1
                    for x in sub_str:
                        stack.append(x)
                    if slash_index < size - 1:
                        stack.append('/')
        while len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        result = ""
        for x in stack:
            result += x
        return result