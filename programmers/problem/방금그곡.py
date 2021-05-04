# 문제
# https://programmers.co.kr/learn/courses/30/lessons/17683

# IDEA
# #이 붙어있는 음과 안 붙어 있는 음은 엄연히 다르게 취급하므로
# #이 붙어있는 음을 하나의 문자로 대치
# 시작 시간과 끝 시간의 차를 반환해 주는 함수 생성
# 찾는 음이 노래 멜로디 안에 포함되어 있으면 해당 제목과 재생시간을 딕셔너리에 저장
# 매치되는 노래가 없을 경우 '(None)' 형태의 string 출력
# 매치되는 노래가 다수인 경우, 가장 재생시간이 긴 노래를 뽑고
# 그래도 다수일 경우, 노래 제목 순서로 출력

def change(melody):
    if 'A#' in melody : melody = melody.replace('A#', 'a')
    if 'C#' in melody : melody = melody.replace('C#', 'c')
    if 'D#' in melody : melody = melody.replace('D#', 'd')
    if 'F#' in melody : melody = melody.replace('F#', 'f')
    if 'G#' in melody : melody = melody.replace('G#', 'g')
    return melody

def get_playtime(start, end):
    start = start.split(':')
    end = end.split(':')
    hour = (int(end[0]) - int(start[0])) * 60
    minute = int(end[1]) - int(start[1])
    return hour + minute

def solution(m, musicinfos):
    m = change(m)
    answer = dict()
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        start, end, name, melody = info[0], info[1], info[2], info[3]
        playtime = get_playtime(start, end)
        melody = change(melody)
        music_melody = ''
        idx = 0
        length = playtime
        while length != 0:
            music_melody += melody[idx%len(melody)]
            idx += 1
            length -= 1

        if m in music_melody:
            answer[name] = playtime

    if not answer: return '(None)'
    else:
        answer = [name for name, playtime in answer.items() if playtime == max(answer.values())]
        answer.sort()
        return answer[0]