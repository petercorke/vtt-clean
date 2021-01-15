# VTT-clean

Remove cruft from a Microsoft Stream generated transcript file.

Turns this

```
WEBVTT

NOTE duration:"00:09:50.5320000"

NOTE language:en-us

NOTE Confidence: 0.892255544662476

6c478ecc-cbcd-4c6b-9a25-df9adba3799f
00:00:05.510 --> 00:00:08.516
Let's discuss intelligence here.
Examples of two organisms, both

NOTE Confidence: 0.892255544662476

de8e238d-692c-472c-9200-e502e9bd2825
00:00:08.516 --> 00:00:12.190
of which are intelligent but in
very different ways. We use

NOTE Confidence: 0.892255544662476

aa265655-5aef-4fb2-987f-1da913dda503
00:00:12.190 --> 00:00:15.530
Albert Einstein as an example
for all human beings, and

NOTE Confidence: 0.892255544662476
```

into this

```
WEBVTT

00:00:05.510 --> 00:00:08.516
Let's discuss intelligence here. Examples of two organisms, both

00:00:08.516 --> 00:00:12.190
of which are intelligent but in very different ways. We use

00:00:12.190 --> 00:00:15.530
Albert Einstein as an example for all human beings, and
```

* removes the `NOTE` lines
* remove duplicated blank lines
* removes the big hex strings which I think are some kind of autogenerated cue identifier or label for the following time coded text.

## Run it

```
python original.vtt > vtt_clean.vtt
```