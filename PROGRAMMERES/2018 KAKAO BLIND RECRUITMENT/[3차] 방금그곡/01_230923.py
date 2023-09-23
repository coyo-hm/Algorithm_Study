def calcTime(st, et):
    st = list(map(int, st.split(":")))
    et = list(map(int, et.split(":")))

    s = st[0] * 60 + st[1]
    e = et[0] * 60 + et[1]

    if e < s:
        e = 23 * 60 + 59

    return e - s


def replaceNote(note):
    note = note.replace("C#", "c")
    note = note.replace("D#", "d")
    note = note.replace("F#", "f")
    note = note.replace("G#", "g")
    note = note.replace("A#", "a")
    return note


def solution(m, musicinfos):
    answer = '(None)'
    m = replaceNote(m)
    for i in range(len(musicinfos)):
        mu = musicinfos[i].split(",")
        t = calcTime(mu[0], mu[1])
        n = replaceNote(mu[3])
        l = len(n)
        s = n * (t // l) + n[0: t % l]
        musicinfos[i] = [t, mu[2], s]
    musicinfos.sort(key=lambda x: -x[0])
    print(musicinfos)
    for (time, title, note) in musicinfos:
        if m in note:
            print(m)
            return title
    return answer