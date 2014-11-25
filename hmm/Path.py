'''
Created on Nov 4, 2014

@author: joro
'''
import numpy
import sys


class Path(object):
    '''
    classdocs
    '''
    
    

    def __init__(self, chiBackPointers, psiBackPointer):
        '''
        Constructor
        '''
        # DEBUG: 
        self.durations = []
        # ending time for each state
        self.endingTimes = []
        
        if chiBackPointers != None and psiBackPointer != None:
            self.pathRaw = self._backtrackForcedDur(chiBackPointers, psiBackPointer)
    
    def setPatRaw(self, pathRaw):
        self.pathRaw = pathRaw
        
    def _backtrackForcedDur(self, chiBackPointers, psiBackPointer):
        '''
        starts at last state and assumes states increase by one
        '''
        length, numStates = numpy.shape(chiBackPointers)
        rawPath = numpy.empty( (length), dtype=int )
        
        # termination: start at end state
        t = length-1
        currState = numStates - 1
        duration = chiBackPointers[t,currState]

        
        # path backtrakcing. allows to 0 to be starting state, but not to go below 0 state
        while (t>duration and currState > 0):
            if duration <= 0:
                print "Backtracking error: duration for state {} is {}. Should be > 0".format(currState, duration)
                break
            
            rawPath[t-duration+1:t+1] = currState
            
            # DEBUG: 
            self.durations.append(duration)
            self.endingTimes.append(t)

            
            ######update
            # pointer of coming state
            currState = psiBackPointer[t, currState]
            
            t = t - duration
            # sanity check. 
            if currState < 0:
                sys.exit("state {} at time {} < 0".format(currState,t))
            
            duration = chiBackPointers[t,currState]
        rawPath[0:t+1] = currState
        
        # DEBUG: 
        self.durations.append(t)
        self.endingTimes.append(t)
        
        self.durations.reverse() 
        self.endingTimes.reverse()    
   
        return rawPath
    
    def _path2stateIndices(self):
        '''
         indices in pathRaw where a new state starts. 
         the array index is the consequtive state count from sequence  
        '''
        self.indicesStateStarts = []
        currState = -1
        for i, p in enumerate(self.pathRaw):
            if not p == currState:
              self.indicesStateStarts.append(i)
              currState = p
              
    def printDurations(self):
        '''
        DEBUG: print durations
        ''' 
        print self.durations
    
             
        