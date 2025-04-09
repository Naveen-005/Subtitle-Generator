import whisper

model = whisper.load_model("small")
result = model.transcribe("english.mp3",word_timestamps=True)
#print(result["text"])
#print(result["segments"])
fp = open("subtitle.srt", "w")

for line in result["segments"]:

    srt=""
    seq=str(line['id']+1)
    hr=int(line['start']/3600)
    min=int((line['start']/60)-hr*60)
    sec=int(line['start']-hr*3600-min*60)
    ms=int((line['start']*100)%100)
    #print(srt)
    srt+=(str(seq)+'\n'+('%02d' % hr)+':'+('%02d' % min)+':'+('%02d' % sec)+','+('%03d' % ms)+' --> ')
    #print(srt)
    hr=int(line['end']/3600)
    min=int((line['end']/60)-hr*60)
    sec=int(line['end']-hr*3600-min*60)
    ms=int((line['end']*100)%100)
    srt+=(('%02d' % hr)+':'+('%02d' % min)+':'+('%02d' % sec)+','+('%03d' % ms)+'\n')
    #print(srt)
    srt+=(line['text']+'\n\n')
    #print(srt,"\n\n")
    fp.write(srt)
    #print(line)
    
fp.close()