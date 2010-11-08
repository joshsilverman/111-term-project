class Group:
    
    bloggers = []
    
    bloggerIds = []
    
    meanRelativeReads = 0
    meanRelativeComments = 0
    meanRelativeInteraction = 0

    meanAbsoluteReads = 0
    meanAbsoluteComments = 0
    meanAbsoluteInteractions = 0
    
    commonTopicsPerBlogger = 0
    
    def __init__(self, bloggers):
        
        self.bloggers = bloggers
        self.bloggerIds = []
        self.meanRelativeInteraction = 0.0
        self.meanAbsoluteInteractions = 0.0
        self.commonTopicsPerBlogger = 0.0
        
        #blogger ids
        for blogger in bloggers: 
            self.bloggerIds.append(blogger.id)

        
        #mean absolute interactions
        readCount = 0
        commentCount = 0
        for blogger in bloggers:
            for bloggerId in self.bloggerIds:
                if (blogger.reads.has_key(bloggerId)):
                    readCount += blogger.reads[bloggerId]
                if (blogger.comments.has_key(bloggerId)):
                    commentCount += blogger.comments[bloggerId]
        self.meanAbsoluteReads = readCount/pow(len(bloggers), 2)
        self.meanAbsoluteComments = commentCount/pow(len(bloggers), 2)
        self.meanAbsoluteInteractions = (self.meanAbsoluteReads + self.meanAbsoluteComments)/2
        
        #mean relative interactions
        readRelCount = 0
        commentRelCount = 0
        for blogger in bloggers:
            for bloggerId in self.bloggerIds:
                if (blogger.reads.has_key(bloggerId)):
                    readRelCount += float(blogger.reads[bloggerId])/float(blogger.readCount)
                if (blogger.comments.has_key(bloggerId)):
                    commentRelCount += blogger.comments[bloggerId]/float(blogger.commentCount)
        self.meanRelativeReads = readRelCount/pow(len(bloggers), 2)
        self.meanRelativeComments = commentRelCount/pow(len(bloggers), 2)
        self.meanRelativeInteractions = (self.meanRelativeReads + self.meanRelativeComments)/2
        