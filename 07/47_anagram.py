
def all_anagrams(candidates):
    # if not candidates:
    #     return False
    # if len(candidates) == 1:
    #     return True
    # sorted_candidates = [sorted(candidate) for candidate in candidates]
    # first = sorted_candidates[0]
    # for candidate in sorted_candidates[1:]:
    #     if first != candidate:
    #         return False
    # return True
    return len({''.join(sorted(candidate)) for candidate in candidates}) == 1


print(all_anagrams(['ship', 'hips']))
print(all_anagrams(['ship', 'hips', 'name']))
print(all_anagrams(['ship']))
print(all_anagrams([]))
