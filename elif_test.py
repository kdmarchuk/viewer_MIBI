import exifread

f = open('C:\\Users\\Kyle\\Box\\BIDC Main\\BIDC_Personal Folders\\Kyle\\Research\\TestData\\MIBI\\FOV1_MassCorrected_Filtered_summed_image.tiff', 'rb')

tags = exifread.process_file(f)


for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print("Key: %s, value %s" % (tag, tags[tag]))

print(tags['Image PageName'])
print(tags['Thumbnail PageName'])
print(tags['IFD 2 PageName'])
