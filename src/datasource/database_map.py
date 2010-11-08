
map = {'user': {'fields': ['userid', 'name', 'admin']},
       'event': {'fields': ['eventid', 'timestamp', 'type', 'fk_userid']},
       'item': {'fields': ['itemid', 'type', 'name', 'text', 'action', 'revision', 'checksum', 'currerev', 'preview', 'rev', 'fk_eventid']},
       'project': {'fields': ['pid', 'key', 'value']},
       'tag': {'fields': ['tagid', 'name']},
       'tagobject': {'fields': ['tagobjectid', 'name', 'fk_tagid']},
       'wikipage': {'fields': ['wikipageid', 'name', 'conent', 'rev']}}