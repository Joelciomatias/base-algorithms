def numSub(s: str) -> int:
    # MOD = 10**9 + 7
    # count = 0
    # ans = 0

    # for c in s:
    #     if c == '1':
    #         count += 1
    #     else:
    #         ans = (ans + count * (count + 1) // 2) % MOD
    #         count = 0

    # # se terminar com bloco de 1's
    # if count > 0:
    #     ans = (ans + count * (count + 1) // 2) % MOD

    # return ans % MOD

    MOD = 10**9 + 7
    count = 0
    ans = 0

    for c in s:
        if c == '1':
            count += 1
        else:
            ans = (ans + count * (count + 1) // 2)
            count = 0

    # se terminar com bloco de 1's
    if count > 0:
        ans = (ans + count * (count + 1) // 2) 

    return ans % MOD


print(numSub('0110111'))