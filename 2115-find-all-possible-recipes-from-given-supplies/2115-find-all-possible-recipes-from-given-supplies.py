#10:47 : 56 : 11:08 : 14
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        graph = dict()
        recipeIngrident = defaultdict(set)
        ans = []
        for i, recipe in enumerate(recipes):
            graph[recipe] = ingredients[i]
            recipeIngrident[recipe] = set(ingredients[i])

        def dfs(recipe, visited, supplies):
            nonlocal ans
            
            if recipe in supplies: #{yeast, flour, meat , bread}
                return True
            if recipe in visited or recipe not in graph: #{sandwich, }
                return False
            visited.add(recipe)
            
            for ing in graph[recipe]:
                if not dfs(ing, visited, supplies):
                    return False
                recipeIngrident[recipe].discard(ing)
            
            if len(recipeIngrident[recipe]) == 0:
                supplies.add(recipe)
                ans.append(recipe)
            visited.remove(recipe)
            return True

        for r in graph:
            dfs(r, set(), supplies)
        return ans




                    
