#
# Scans directory for stereo audio files (currently only works with .m4a), outputs
# left channel as a mono file (normalized).
#
# Motivation: jazz piano players want to isolate the left channel of the 100s of
# Jamey Aebersold backing tracks out there, because the left channel contains the
# bass + drums track (the right channel contains the piano + drums track). 
#

import os
from pydub import AudioSegment

def match_target_amplitude(sound, target_dBFS):
# function that does the normalizing, courtesy https://github.com/jiaaro/pydub/issues/90
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Begin

# Get the filenames

tracks = os.listdir('.')

# Loop through the filenames

for track in tracks:

    # Split filename into name + extension then check if it is a .m4a

    splitname = os.path.splitext(track) 

    if splitname[1] == ".m4a":
        print ".m4a file found: " + splitname[0] + splitname[1]

        # Import
    
        song = AudioSegment.from_file(track,"m4a")

        # Check if stereo (to avoid crash when trying to split a mono track)

        if  song.channels == 2:

            # If yes, split it up 

            splitsong = song.split_to_mono()

            # Retrieve the left channel
     
            left = splitsong[0]

            # Normalize
  
            normalized_left = match_target_amplitude(left, -20.0)

            # Construct the new filename
    
            newtrackname = splitname[0] + "_L.m4a"

            # Export as m4a/mp4 (temp)

            normalized_left.export(newtrackname, format="mp4")
            print newtrackname + " successfully extracted and written"

        else:
            print splitname[0] + splitname[1] + " is not stereo, track ignored"
        #endif
    #endif
#endfor
