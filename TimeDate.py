'''Question:-
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to
view this new post on their news feed. Users can also see exactly when the post was published,
i.e, how many hours, minutes or seconds ago.
Since sometimes posts are published and viewed in different time zones, this can be confusing.
You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
Day dd Mon yyyy hh:mm:ss +xxxx
Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Sample Input 0
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample Output 0
25200
88200
'''
import datetime

format_string = "%a %d %b %Y %H:%M:%S %z"
Time = int(input())

for test in range(Time):
    t1 = str(input())
    t2 = str(input())

    parsed_t1 = datetime.datetime.strptime(t1, format_string)
    parsed_t2 = datetime.datetime.strptime(t2, format_string)

    diff = parsed_t2 - parsed_t1

    print (int(abs(diff.total_seconds())))
