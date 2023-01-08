import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    width: 640
    height: 480
    visible: true
    title: "Hello World"



    Rectangle{
    id:imageRect
    anchors.fill:parent
    color:"black"

    Image{
    id:opencvImage
    anchors.fill:parent
    property bool counter:false
    source: "image://live/image"
    fillMode: Image.PreserveAspectFit

    cache:false

    function reload(){
    counter = !counter
    source = "image://live/image?id" + counter

    }

    }

    }

Connections{
target:imageProvider

function onImageChanged(){

   opencvImage.reload()



}


}








}



