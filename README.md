# Ship Bell Time Converter

This program converts any time of day into Ship's Bell Time!

## Background

Ship's Bell Time is a system of time-keeping that has been used aboard marine vessels since as early as the 1400s and is still in-use today! This system divides the day (24hrs) into 7 "watches". 

|    WATCH    |  START  |  END   |
--------------|---------|--------| 
| First       |  20:00  |  00:00 |
| Middle      |  00:00  |  04:00 |
| Morning     |  04:00  |  08:00 |
| Forenoon    |  08:00  |  12:00 |
| Afternoon   |  12:00  |  16:00 |
| First Dog   |  16:00  |  18:00 |
| Second Dog  |  18:00  |  20:00 |

The progress of each watch is announced every 30 minutes by ringing the ship bell. For example, consider a 4 hour watch. After the first 30 minutes, the bell is rung once for "First Bell". After the next 30 minutes the bell is rung twice for "Two Bells". After 30 more minutes it's rung thrice "Three Bells", and so on. After all 4 hours have passed (8 30min increments) the bell is rung for "Eight Bells" indicating the end of the current watch and the beginning of the next. 

## Instructions

Here's how to use this program to check the watch status for a given time!


```python
# Start by initializing the Schedule() with the target time.
# Pass the target time as a string like (ie. '23:45', '00:28', '15:13', etc.)
s = Schedule('20:11')
# ...or leave it blank and it'll default to current time!
s = Schedule()

# Use the Schedule() you created to check status of the watch...
current_watch = s.current_watch.name
next_watch = s.next_watch.name
last_watch = s.last_watch.name

# ...or status of the bell!
next_bell = s.next_bell.count
last_bell = s.last_bell.count
minutes_to_next_bell = s.min_to_next_bell
minutes_since_last_bell = s.min_since_last_bell
```

## Example

Print out current Ship Bell Time in human readable text.

```python
# Initialize Schedule(). Default to current time.
s = Schedule()

# Access schedule information.
current_watch    = s.current_watch.name
min_to_next_bell = s.min_to_next_bell
next_bell_count  = s.next_bell.count

# Print out time as human readable string.
print(f"It's currently {current_watch} watch. {min_to_next_bell} minutes to {next_bell_count} bells.")

# OUTPUT: "It's currently First Dog watch. 3 minutes to 4 bells."
```
