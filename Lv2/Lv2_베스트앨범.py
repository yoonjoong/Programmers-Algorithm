import collections
def solution(genres, plays):
    answer = []
    album = collections.defaultdict(list)
    cnt = collections.defaultdict(int)
    song_id=0
    for genre,play in zip(genres,plays):
        album[genre].append((play,song_id))
        cnt[genre] +=play
        song_id +=1
        
    rank = sorted(cnt.keys(), key=lambda x:cnt[x],reverse=True)    
    for g in rank:
        tmp_genre = sorted(album[g],key=lambda x:x[0],reverse=True)
        if len(tmp_genre)>1:
            answer.append(tmp_genre[0][1])
            answer.append(tmp_genre[1][1])
        else:
            answer.append(tmp_genre[0][1])
    return answer