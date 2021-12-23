data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

result = sorted(data, key = abs, reverse=True)

result_with_lambda = sorted(data, key = lambda x: abs(x), reverse=True)

print(result, result_with_lambda, sep='\n')