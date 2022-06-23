class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        item_dict = {"type":0, "color": 1, "name" : 2 }
        position = item_dict[ruleKey]
         
        for i in items:
            if i[position] == ruleValue:
                count +=1
        return count
    
    
    
    """
    class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in items:
            if ruleKey == "type":
                if i[0] == ruleValue:
                    count += 1
            elif ruleKey == "color":
                if i[1] == ruleValue:
                    count += 1
            elif ruleKey == "name":
                if i[2] == ruleValue:
                    count += 1
        return count
    """