import whisper

def generate_subtitles(input_audio,output_path,Model="small"):

    model = whisper.load_model(Model)
    result = model.transcribe(input_audio,word_timestamps=True)
    #print(result["text"])
    #print(result["segments"])
    fp = open(output_path, "w")

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

generate_subtitles(input_audio="tmp/english.mp3",output_path="tmp/subtitl2.srt")


'''


Todo:

Break large sentences into small segments
UI for easy use

'''

