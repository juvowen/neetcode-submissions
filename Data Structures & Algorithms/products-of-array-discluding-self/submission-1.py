class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #we add a number to the stack, then everything esle will be multiplied then we add it to the temp list
        zero_count = 0
        total_product = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num

        result = []

        for num in nums:
            if zero_count > 1:
                result.append(0)

            elif zero_count == 1:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)

            else:
                result.append(total_product // num)
        return result