import heapq
h = []
heapq.heappush(h, (5, 'AA'))
heapq.heappush(h, (7, 'BB'))
heapq.heappush(h, (11, 'CC'))
heapq.heappush(h, (9, 'DD'))
heapq.heappush(h, (1, 'EE'))
heapq.heappush(h, (3, 'FF'))
heapq.heappop(h)
heapq.heappop(h)
heapq.heappop(h)
heapq.heappop(h)
print(h)