# KillBeam
Music

1.1 Objective The primary aim of the project was to develop an enjoyable
musical tool which supports playback and displays colorful LED lights while the
tracks play.

1.2 Features The following features characterize the Music Player using Raspberry Pi and Sense HAT : (i) Supports playback features- Play Music (ii) Display colorful lights on the LED matrix in synchronization with the beats being
captured from the track.

2 Method
2.1 System Design The development of the system ’Beats and Gleams’ can
be seen as a three step process(Figure 1).The very first step being the playing of
soundtrack in wave audio file(.wav) format. The second step follows to be the
detection of beats from the wave audio file.In this The last step of the process
was glowing the LED matrix at specific XY co-ordinate positions with one of
the three colors-red, green or yellow.

The first sub step of this step was playing audio file using Advanced Linux
Sound Architecture(ALSA) which provides audio and MIDI functionality to the Linux operating system[].Further the division of the audio wave file was made
into chunks i.e.blocks of data usually an integer power to the base 2 such as
1024,4096 etc.).Here the value of Chunk has been set to 4096.
The second step , shown step wise in Figure 2 was the calculation of beats
from the real time audio file obtained from the first step.Firstly, the raw audio data is converted in the form of an array understandable by the Numpy
package.Further this array,along with sampling rate and chunk is fed as input
into the Fast Fourier Transform function.The ”Fast Fourier Transform” (FFT)
is an important measurement method in the science of audio and acoustics measurement which converts a signal into individual spectral components and thus
provide frequency information about the audio file[2]. Once the Fast Fourier
Transform had been applied , the last element in the array was removed so as
to make it of the same size as the chunk.Further the average power of the audio
signal (a particular frame taken at a time) was computed, array was reshaped
and the final matrix was computed. In the third step, the matrix obtained from
the second step was scaled and on the basis of X and Y co-ordinates of the pixels
on the LED matrix

2.2 System Implementation The system was implemented using Python
3.The following packages were used- alsaaudio,wave,numpy,struct,sensehat.

The function numpy.fft.rfft was used to compute ”the one-dimensional n-point
discrete Fourier Transform (DFT) of a real-valued array by means of an efficient
algorithm called the Fast Fourier Transform (FFT)”[1].Here , fft(a[, n, axis,
norm])computes the one-dimensional discrete Fourier Transform and rfft(a[, n,
axis, norm]) computes the one-dimensional discrete Fourier Transform for real
input.
The function reshape(a, newshape, order=’C’)[1] gives a new shape to an array without changing its data.[1]. The function numpy.log10(x, /, out=None, *,
where=True, casting=’samekind’, order=’K’, dtype=None, subok=True[, signature, extobj]) = ¡ufunc ’log10’¿ returns the base 10 logarithm of the input
array, element-wise[1].


3 Results
The lights were glowing in one of the three colors - green ,yellow or red depending
on the beats of the music that was played.For low beats , green color LEDs were
lighting, for medium level beats , yellow color LEDS were seen to be lighting
and for high beats, red color LEDs could be spotted.

4 Conclusions
The developed system can be used as tool for entertainment particularly as
music players with display unit where fancy LED lights can be displayed. There
is the scope of extending the development of the system in a multi threaded
environment where several playback features can be implemented concurrently
along with certain audio analysis features. Moreover, the playback features
could be based on providing motion based inputs such as change of track over
the tilt of the device.
