from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


@bootstrap
def extended_gcd(a: int, b: int):
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = yield extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    yield d, x, y


def solve_linear_diophantine_equation(a, b, z):
    g, s, t = extended_gcd(a, b)

    if z % g == 0:
        x = s * (z // g)
        y = t * (z // g)
        while x == 0 or y == 0:
            x += b // g
            y -= a // g

        return x, y
    else:
        return None


# 示例
a = 7
b = 5
z = 19

solution = solve_linear_diophantine_equation(a, b, z)
if solution:
    print(f"整数解为 x = {solution[0]}, y = {solution[1]}")
else:
    print("无整数解")
