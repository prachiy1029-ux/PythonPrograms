def common_elements(list1, list2):
    common = []

    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    return common


if __name__ == "__main__":
    list1 = list(map(int, input("Enter first list: ").split()))
    list2 = list(map(int, input("Enter second list: ").split()))

    print("Common elements:", common_elements(list1, list2))