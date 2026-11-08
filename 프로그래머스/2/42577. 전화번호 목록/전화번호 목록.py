def solution(phone_book):

    phone_book = set(phone_book)
    for phone in phone_book:            #O(N)
        for j in range(1, len(phone)):  #O(L)
            if phone[:j] in phone_book: #O(j)
                return False
                
    return True