class ThroneInheritance:

    def __init__(self, kingName: str):
        self.nation = {}
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.nation:
            self.nation[parentName] = [childName]
        else:
            self.nation[parentName] += [childName]

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.ans = []
        self.dfs(self.king)
        return self.ans

    def dfs(self, cur):
        if cur not in self.dead:
            self.ans.append(cur)
        if cur in self.nation:
            for child in self.nation[cur]:
                self.dfs(child)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
