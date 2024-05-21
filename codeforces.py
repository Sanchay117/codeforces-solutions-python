from collections import defaultdict


def count_beautiful_pairs(triplets):
    # Hash tables for different positions
    hash_pos1 = defaultdict(list)
    hash_pos2 = defaultdict(list)
    hash_pos3 = defaultdict(list)

    # Populate hash tables
    for index, triplet in enumerate(triplets):
        hash_pos1[(triplet[1], triplet[2])].append(index)
        hash_pos2[(triplet[0], triplet[2])].append(index)
        hash_pos3[(triplet[0], triplet[1])].append(index)

    count = 0

    # Check for beautiful pairs
    for index, triplet in enumerate(triplets):
        # Check pairs differing at position 1 (fix 2 and 3)
        for other_index in hash_pos1[(triplet[1], triplet[2])]:
            if other_index != index:
                count += 1

        # Check pairs differing at position 2 (fix 1 and 3)
        for other_index in hash_pos2[(triplet[0], triplet[2])]:
            if other_index != index:
                count += 1

        # Check pairs differing at position 3 (fix 1 and 2)
        for other_index in hash_pos3[(triplet[0], triplet[1])]:
            if other_index != index:
                count += 1

    # Each pair is counted twice (once for each order), so divide by 2
    return count // 2


# Example usage
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    triplets = []

    for j in range(n - 2):
        triplets.append([arr[j], arr[j + 1], arr[j + 2]])

    print(triplets)
    print(count_beautiful_pairs(triplets))
