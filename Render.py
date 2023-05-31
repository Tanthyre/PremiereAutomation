import pymiere


pymiere.objects.app.encoder.launchEncoder()
project = pymiere.objects.app.project
sequence = pymiere.objects.app.project.sequences

# presetPath1080 = r"C:\Users\John\Documents\Adobe\Adobe Media Encoder\23.0\Presets\1080.epr"
# presetPath2257 = r"C:\Users\John\Documents\Adobe\Adobe Media Encoder\23.0\Presets\2257.epr"
# clipSequence = "Clips"
# finalVersionSequence = "Full"
# projectName = "2023_04_04_Facefuck"


# Render full video in 1080

def render1080(trackName, presetName, projectName):
    for i in range(sequence.numSequences):
        name = sequence[i].name
        if name == trackName:
            pymiere.objects.app.encoder.encodeSequence(sequence[i], "G:\\Local Edits\\" + projectName + "_1080",
                                                       presetName, 0, 0)


def render2257(trackName, presetName, projectName):
    for i in range(sequence.numSequences):
        name = sequence[i].name
        if name == trackName:
            pymiere.objects.app.encoder.encodeSequence(sequence[i], "G:\\Local Edits\\" + projectName + "_2257",
                                                       presetName, 0, 0)


def renderclips(trackName, presetName, projectName):
    for i in range(sequence.numSequences):
        name = sequence[i].name
        if name == trackName:
            for j in range(sequence[i].videoTracks[0].clips.numItems):
                sequence[i].setInPoint(sequence[i].videoTracks[0].clips[j].start)
                sequence[i].setOutPoint(sequence[i].videoTracks[0].clips[j].end)
                clipNumber = str(j + 1)
                pymiere.objects.app.encoder.encodeSequence(sequence[i],
                                                           "G:\\Local Edits\\" + projectName + " _Teaser_" +
                                                           clipNumber, presetName, 1, 0)


