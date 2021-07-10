def solution(phone_book):
    answer = True

    for i in range (len(phone_book)) :
         for j in range (len(phone_book)) :
              if (i==j) :
                  continue
              elif ( phone_book[j].find(phone_book[i]) == 0) :
                  answer = False;
                  break
         if ( answer == False ) :
             break
        
                  
    return answer

print(solution(["119", "97674223", "1195524421"]))
