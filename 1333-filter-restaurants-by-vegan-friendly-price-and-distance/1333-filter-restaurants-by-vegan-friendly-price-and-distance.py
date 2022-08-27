class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        restaurants.sort( key=lambda x:[x[1],x[0]],reverse=True)
        
        for ids, rating, isVegan, price, dst in restaurants:
            if (price <= maxPrice and dst <= maxDistance):
                if veganFriendly and not isVegan:
                    continue
                ans.append(ids)
   
        return ans