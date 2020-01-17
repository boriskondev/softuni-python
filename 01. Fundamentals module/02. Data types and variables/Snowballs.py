snowballs = int(input())

best_value = 0
best_ball = ()

for snowball in range(0, snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > best_value:
        best_value = snowball_value
        best_ball = (snowball_snow, snowball_time, snowball_value, snowball_quality)

print(f"{best_ball[0]} : {best_ball[1]} = {best_ball[2]} ({best_ball[3]})")