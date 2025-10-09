
class Meeting():

    def __init__(self, meeting_id, organiser, participants, startdate, enddate, startime, endtime, meeting_type):
        self.meeting_id = meeting_id
        self.organiser = organiser
        self.participants = participants
        self.starttime = startime
        self.endtime = endtime
        self.startdate = startdate
        self.enddate = enddate
        self.meeting_type = meeting_type

    def __repr__(self):
        return f'Meeting - {self.meeting_id} Organised By - {self.organiser}, Date - {self.startdate} - {self.enddate}, Time - {self.starttime} - {self.endtime}, Type - {self.meeting_type}'