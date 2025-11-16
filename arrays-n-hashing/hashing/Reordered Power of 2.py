class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Create a helper to get the sorted digit string
        def signature(x):
            print()
            res = "".join(sorted(str(x)))
            print(f"input: {x}, res: {res}")
            return res
        
        # Precompute signatures of powers of 2
        power_signatures = {signature(2 ** i) for i in range(31)}
        power_signatures = {signature(1 << i) for i in range(31)}
        
        # Check if n's signature matches any
        return signature(n) in power_signatures
    
print(Solution().reorderedPowerOf2(2124))
