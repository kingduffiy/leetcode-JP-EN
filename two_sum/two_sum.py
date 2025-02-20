class Solution(object):
    def twoSum(self, nums, target):
        # 数字とそのインデックスを保存するための辞書を作成 | Create a dictionary to store the numbers and their indices
        num_to_index = {}

        # 配列をループして処理 | Iterate through the array
        for i, num in enumerate(nums):
            # 補数を計算 | Calculate the complement
            complement = target - num

            # 補数が辞書に存在するか確認 | Check if the complement exists in the dictionary
            if complement in num_to_index:
                # 存在する場合、そのインデックスと現在のインデックスを返す | If it exists, return the indices
                return [num_to_index[complement], i]
            
            # 存在しない場合、現在の数字とそのインデックスを辞書に保存 | Otherwise, store the current number and its index in the dictionary
            num_to_index[num] = i


# 使用例 | Example usage:
nums = [2,7,11,15]
target = 9
print(Solution) # 出力 | Output: [0, 1]