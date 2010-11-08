import re
from pprint import pprint

import datasource.user_map as userMap

class Blogger():
    
    #reads of other people's posts
    reads = {}
    
    #read/comment count
    readCount = 0
    commentCount = 0
    
    #comments on other posts
    comments = {}
    
    id = None
    
    def __init__(self, resultsList, id):
        
        self.reads = {}
        self.comments = {}
        self.id = id
        self.readCount = 0
        self.commentCount = 0
        
        for result in resultsList:
            
            #reads
            if (result['item.name'] == 'to'):
                student = re.search('(?:Talk:)?([^/]*)/', result['item.text']).group(1)
                studentId = userMap.map[student]
                if (not self.reads.has_key(studentId)): self.reads[studentId] = 0
                self.reads[studentId] += 1
                self.readCount += 1
                
            #comments
            if (result['event.type'] == 'edit'):
                studentMatchObj = re.match('(?:Talk:)([^/]*)/', result['item.text'])
                if (studentMatchObj):
                    student = studentMatchObj.group(1)
                    studentId = userMap.map[student]
                    if (not self.comments.has_key(studentId)): self.comments[studentId] = 0
                    self.comments[studentId] += 1
                    self.commentCount += 1
            