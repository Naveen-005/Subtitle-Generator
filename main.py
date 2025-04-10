import whisper

def convert_time_stamp(time):
    hr=int(time/3600)
    min=int((time/60)-hr*60)
    sec=int(time-hr*3600-min*60)
    ms=int((time*100)%100)

    return(('%02d' % hr)+':'+('%02d' % min)+':'+('%02d' % sec)+','+('%03d' % ms))

def generate_subtitles(input_audio,output_path,Model="small"):

    model = whisper.load_model(Model)
    result = model.transcribe(input_audio,word_timestamps=True)

    fp = open(output_path, "w")
    seq=0

    for line in result["segments"]:

        srt=""
        seq+=1

        time=convert_time_stamp(line['start'])
        srt+=(str(seq)+'\n'+time+' --> ')

        time=convert_time_stamp(line['end'])
        srt+=(time+'\n')
        srt+=(line['text']+'\n\n')
        
        fp.write(srt)
        
    fp.close()

generate_subtitles(input_audio="tmp/english.mp3",output_path="tmp/subtitl2.srt")


'''


Todo:

Break large sentences into small segments
UI for easy use

'''

