# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/submissions/
# average-salary-excluding-the-minimum-and-maximum-salary.py

class Solution:
    def average(self, salary: List[int]) -> float:
        sortedSalary = list(sorted(salary))
        return (sum(sortedSalary) - (sortedSalary[0] + sortedSalary[-1])) / (len(sortedSalary) - 2)