import subprocess

def get_formats(url):
    output = subprocess.check_output(["yt-dlp", "-F", url]).decode()
    formats = {}
    audio_formats = []
    video_formats = []
    lines = output.split('\n')
    for line in lines:
        if not line:
            continue
        fields = line.split()

        if len(fields) < 15:
            continue

        while '|' in fields:   
            fields.remove('|')
        while '~' in fields:   
            fields.remove('~')

        if 'video' in fields and 'only' in fields:
            fields.remove('video')
            fields.remove('only')
            del fields[8]
            del fields[6]
            if ',' in fields[-2]:
                fields[-2] = fields[-2][:-1]
            temp = fields[2]
            del fields[2]
            fields.insert(-2, temp)

            Fields = {}
            labels = [ 'ID', 'File Format', 'FPS', 'File Size', 'Bit rate', 'VCodec', 'Resolution', 'Quality' ]
            for i in range(8):
                Fields[labels[i]] = fields[i]
            video_formats.append(Fields)
            
        if 'audio' in fields and 'only' in fields:
            while 'audio' in fields and 'only' in fields:
                fields.remove('audio')
                fields.remove('only')
            del fields[7:11]
            del fields[5]
            
            Fields = {}
            labels = [ 'ID', 'File Format', 'Channels', 'File Size', 'Bit rate', 'ACodec' ]
            for i in range(6):
                Fields[labels[i]] = fields[i]
            audio_formats.append(Fields)

        if 'dash' in fields[-1]:
            del fields[-1]

        formats['audio'] = audio_formats
        formats['video'] = video_formats

    return(formats)

if __name__ == '__main__':
    url = input()    
    print(get_formats(url))
