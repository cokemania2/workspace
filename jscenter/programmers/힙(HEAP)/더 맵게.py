import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    for i in range (len(scoville)) :
        heapq.heappush(heap, scoville[i])
    while(heap[0] < K) :
        print(heap)
        if (len(heap) == 1 and heap[0] < K) :
            return -1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b*2)
        answer = answer + 1

    return answer

print(solution([1, 2, 3, 9, 10, 12],7))
