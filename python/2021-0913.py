# 字节面试题目,稀疏矩阵乘法
def multibyViolence(A: list, B: list):
    dim = len(B)
    result = [[0 for _ in range(dim)] for _ in range(dim)]
    mymulti = lambda x, y: sum([x[index] * y[index] for index in range(dim)])
    for i in range(dim):
        for j in range(dim):
            temp = [B[_][j] for _ in range(dim)]
            result[i][j] += mymulti(A[i][:], temp)
    return result


def multiBy(A: list, B: list):
    dim = len(B)
    result = [[0 for _ in range(dim)] for _ in range(dim)]
    myadd = lambda x, y: [x[index] + y[index] for index in range(dim)]
    for i, j, v in A:
        result[i] = myadd(result[i], v * B[j])
    return result


if __name__ == '__main__':
    dim = 3
    import random

    random.seed(1)
    A = [[1 if random.random() > 0.5 else 0 for _ in range(dim)] for _ in range(dim)]  # 稀疏矩阵 二维数组表示
    B = [[random.randint(0, 10) for _ in range(dim)] for _ in range(dim)]
    print("A-{} B-{}".format(A, B))
    result = multibyViolence(A, B)
    print(result, end="\n\n")

    A_ = [(i, j, A[i][j]) for i in range(dim) for j in range(dim) if A[i][j]]  # 稀疏矩阵 (r,c,v)元组表示
    B = [[random.randint(0, 10) for _ in range(dim)] for _ in range(dim)]
    print(A_, B)
    result = multibyViolence(A, B)
    print(result)
