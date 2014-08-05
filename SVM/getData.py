import PIL.Image as Image
import tifwork

def getData(fileName, num):
    #get dataset
    dataset = tifwork.openTIF(fileName)

    #get details of dataset
    (cols,rows,bands,bandArray) = tifwork.detailsTIF(dataset)

    #get all bands
    bandArray = tifwork.getBand(dataset,bands,bandArray)

    #input a band

    workData = bandArray[:,:,num-1]

    #show original image and plot it
    imdata = Image.fromarray(workData)
    imdata = imdata.convert('L')
    imdata.save('original.jpg')
    #plot(workData,'Original')
    filename = 'original.jpg'
    return filename
