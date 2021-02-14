# Affine_Transformations_Implementation
 Script and jupyter notebook presentation of an implementation on affine transformations, using numpy and PIL.

## Description

In Euclidean geometry, an affine transformation, or an affinity (from the Latin, affinis, "connected with"), is a geometric transformation that preserves lines and parallelism (but not necessarily distances and angles).

More generally, an affine transformation is an automorphism of an affine space (Euclidean spaces are specific affine spaces), that is, a function which maps an affine space onto itself while preserving both the dimension of any affine subspaces (meaning that it sends points to points, lines to lines, planes to planes, and so on) and the ratios of the lengths of parallel line segments. Consequently, sets of parallel affine subspaces remain parallel after an affine transformation. An affine transformation does not necessarily preserve angles between lines or distances between points, though it does preserve ratios of distances between points lying on a straight line.

## Instructions

The script can be run with the command "python AffineTransformations.py <inputImageName> <a1> <a2> <a3> <a4> <a5> <a6>", where inputImageName needs to be the path of the image you wish to process (highly recommend the image in this repository because I've come across problems with other pictures) and a1, a2, a3, a4, a5, a6 are the first 6 numbers of the 3x3 Affine Transformation matrix (the last row is always [0 0 1]). For example, python AffineTransformations.py brain0030slice150_101x101.png 0 1 0 -1 0 0 will rotate the picture bt 90 degrees and show the result.

For more information about how the 6 parameters can be used to scale/rotate etc the image, you can check out this guide: https://www.mathworks.com/discovery/affine-transformation.html. You can also check out the jupyter notebook presentation in order to understand the process and check out the examples I included.
