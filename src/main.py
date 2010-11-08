from pprint import pprint
import itertools

from lib.blogger import Blogger
from lib.group import Group

from datasource.sql_log import log as sqlLog
import datasource.user_map as userMap

from datasource.query_lib import QueryLib

def main():
    
    bloggers = buildBloggers()
    
    groups = buildGroups(bloggers)
    
    output(groups)
    
    pprint(sqlLog)
    
def buildBloggers():

    queryLib = QueryLib()
    
    users = queryLib.execute('users')
    userMap.set(users)
    
    bloggers = []
    
    for user in users:
        
        sql = '''select * from event,user, item
            where userid = fk_userid
            and userid = %i
            and item.name <> 'from'
            and item.fk_eventid = event.eventid''' % user['user.userid']
        
        bloggers.append(Blogger(queryLib.customQuery(sql, ['event', 'user', 'item']), 
                                user['user.userid']))
    
    #remove bloggers with fewer than 25 reads
    bloggers = [blogger for blogger in bloggers if blogger.readCount > 20]
    
    return bloggers
    
def buildGroups(bloggers):
    
    groups = []

    for r in range(2,6):
        groupTuples = tuple(itertools.combinations(bloggers, r))
        
        for groupTuple in groupTuples:
            group = Group(groupTuple)
            groups.append(group)
        
    return groups    
    
def output(groups):
    
    groupsByRelative = sorted(groups, key=lambda k: k.meanRelativeInteractions)
    groupsByAbsolute = sorted(groups, key=lambda k: k.meanAbsoluteInteractions)
    
    groupsByRelative.reverse()
    groupsByAbsolute.reverse()
    
    for i in range(0, 50):
        print(groupsByRelative[i].meanRelativeInteractions)
        print([userMap.mapReverse[id] for id in groupsByRelative[i].bloggerIds])

    for i in range(0, 50):
        print(groupsByAbsolute[i].meanAbsoluteInteractions)
        print([userMap.mapReverse[id] for id in groupsByAbsolute[i].bloggerIds])
    
main()