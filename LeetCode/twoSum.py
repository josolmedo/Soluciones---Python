class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        diccionario = {}
        for i in range(n):            
            diccionario[nums[i]] = i
        
        for x in range(n):
            valor = target - nums[x]            
            if valor in diccionario and diccionario[valor] != x:
                return[x, diccionario[valor]]
        
        return []

nums = [3,2,4]
target = 7
solucion = Solution()

cosa = solucion.twoSum(nums, target)
print(f"\n{cosa}\n")