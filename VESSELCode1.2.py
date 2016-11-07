#version2
while True:
    reply=raw_input('Please enter a sentence') #enter sentence
    print reply
    cue = raw_input()
    synonymous = ['that is','i.e.','in other words']
    antynomous = ['unlike', 'but', 'instead of']
    categorical = ['or', 'less','more' 'as']
    causeeffect = ['because', 'after', 'in order', 'by', 'for']




    if any(x in cue for x in synonymous): #identifies cue type
        print 'Synonymous Cue'

    else:
        if any (x in cue for x in antynomous):
            print "Antynomous cue and Syn"
        else:
            if any (x in cue for x in categorical):
                print 'Categorical cue'
            else:
                if any (x in cue for x in causeeffect):
                    print'Cause and effect cue'
                else:
                    print 'Associative cue'
    if reply == 'stop':
        break


#multiple cues
#whole words--constrain



