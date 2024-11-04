import heapq

def solution(book_time):
    book_time.sort(key=lambda x: x[0])
    heap = []
    first_book = book_time[0][1].split(':')
    first_book = int(first_book[0])*60 + int(first_book[1])
    
    heapq.heappush(heap, first_book+10)
    for i in range(1, len(book_time)):
        start = book_time[i][0].split(':')
        start = int(start[0])*60 + int(start[1])
        
        end = book_time[i][1].split(':')
        end = int(end[0])*60 + int(end[1])

        
        min_book = heap[0]
        if min_book <= start :
            heapq.heappop(heap)
        heapq.heappush(heap, end+10)


    return len(heap)