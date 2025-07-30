def backward_traversal(s: str) -> str:
    sb = []
    for i in range(len(s) - 1, -1, -1):
        sb.append(s[i])
    return ''.join(sb)


def two_pointer(s: str) -> str:
    s_list = list(s)
    left, right = 0, len(s) - 1
    while left <= right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    return ''.join(s_list)


def stack_method(s: str) -> str:
    stack = []
    for ch in s:
        stack.append(ch)

    sb = []
    while stack:
        sb.append(stack.pop())
    return ''.join(sb)


if __name__ == "__main__":
    print(backward_traversal("International"))  # lanoitanretnI
    print(two_pointer("International"))  # lanoitanretnI
    print(stack_method("International"))  # lanoitanretnI
