def binary_search(lookup_value, array, insert_position=False):
    def binary_search_impl(arr, offset=0):
        size = len(arr)
        if size <= 1:
            return offset + (0 if size == 0 or arr[0] <= lookup_value else 1)
        else:
            mid_index = size // 2
            mid = arr[mid_index]
            if lookup_value == mid:
                return offset + mid_index
            return offset + (binary_search_impl(arr[:mid_index]) if mid > lookup_value else
                             binary_search_impl(arr[mid_index + 1:], mid_index + 1))

    loc = binary_search_impl(array, 0)
    return loc if insert_position or (loc < len(array) and array[loc]) == lookup_value else -1


if __name__ == '__main__':
    pass
