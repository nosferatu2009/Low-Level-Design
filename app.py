from MeetingScheduler import MeetingScheduler
from Meeting import Meeting
from datetime import date, time
from MeetingType import MeetingType

def main():

    meeting1 = Meeting(1,"Alice", ["A", "B", "C"], date(2025,9,21), date(2025,9,21), time(14,30,0), time(15,0,0), MeetingType.SINGLE_INSTANCE)
    meeting2 = Meeting(2,"Bob", ["A", "B", "C"],   date(2025,9,21), date(2025,9,30), time(15,30,0), time(15,45,0), MeetingType.DAILY)
    meeting3 = Meeting(3,"Alice", ["A", "B", "C"], date(2025,9,21), date(2025,10,2),time(13,30,0), time(15,0,0), MeetingType.WEEKLY)
    meeting4 = Meeting(4,"Alice", ["A", "B", "C"], date(2025,10,21), date(2025,10,30),time(13,30,0), time(14,0,0), MeetingType.DAILY)


    meetingScheduler = MeetingScheduler()
    meetingScheduler.schedule_meeting(meeting = meeting1)
    meetingScheduler.schedule_meeting(meeting = meeting2)
    meetingScheduler.schedule_meeting(meeting = meeting3)
    meetingScheduler.schedule_meeting(meeting = meeting4)

    meetings = meetingScheduler.fetch_meetings("Alice", period="week")


if __name__ == "__main__" :
    main()