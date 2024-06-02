class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split(" ")
        s=[]
        for i in title:
            if len(i)<=2:
                s.append(i.lower())
            else:
                s.append(i.title())
        return " ".join(s)