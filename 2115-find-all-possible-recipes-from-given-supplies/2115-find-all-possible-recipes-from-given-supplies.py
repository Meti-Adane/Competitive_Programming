#10:47 : 56 : 11:08 : 14
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        graph = defaultdict(set)
        ans = []
        for i, recipe in enumerate(recipes):
            graph[recipe] = set(ingredients[i])
      
        def dfs(recipe, visited, supplies):
            nonlocal ans
            if recipe in supplies: 
                return True
            if recipe in visited or recipe not in graph: 
                return False
            
            visited.add(recipe)
            used = set()
            for ing in graph[recipe]:
                if not dfs(ing, visited, supplies):
                    return False
                used.add(ing)
            graph[recipe] ^= used
            
            if not graph[recipe]:
                supplies.add(recipe)
                ans.append(recipe)
            visited.remove(recipe)
            return True

        for r in graph:
            dfs(r, set(), supplies)
        return ans




                    
