A simple star detection algorithm with adjustable parameters. It simply loads the image, turns it into a grayscale, applies Gaussian blur, dilates the faint stars if needed, and then draws yellow hollow circles around the detected stars.

Play with the threshold parameter to set the number of detected stars. 

Here is the RAW image that is uploaded:

![Raw Image](stars_raw.jpg)

And here is the result with the detected stars:

![Detected Stars](stars_detected.jpg)
