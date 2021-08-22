# https://www.acmicpc.net/problem/17211
# 좋은날 싫은날.py

N, feel = map(int,input().split())
gg, gb, bg, bb = map(float,input().split())
fg = 0
fb = 0
if feel == 1:
    fg = bg
    fb = bb
else :
    fg = gg
    fb = gb
for i in range(N-1):
    fg_t = fg
    fb_t = fb
    fg = fg_t * gg + fb_t * bg
    fb = fb_t * bb + fg_t * gb
print(round(fg * 1000))
print(round(fb * 1000))