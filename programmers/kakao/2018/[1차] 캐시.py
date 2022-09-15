def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        answer = 5 * len(cities)
    else:
        cache = []
        
        for city in cities:
            city = city.lower()
            is_contained = False
            
            for idx, c in enumerate(cache):
                if c == city:
                    is_contained = True
                    break
            
            if len(cache) >= cacheSize:
                cache.pop(idx)
            cache = [city] + cache
            answer += (1 if is_contained else 5)
            
    return answer