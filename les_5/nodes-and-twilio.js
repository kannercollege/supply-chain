var myArray = context.get("videos") || [];
for (var i=0; i < myArray.length; i++) {
   if (myArray[i] == msg.payload){
    delete myArray[i]
    return msg
   }
}
myArray.push(msg.payload);
context.set("videos", myArray);