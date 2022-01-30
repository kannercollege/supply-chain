let values = Object.values(msg.payload["items"]);

if (values.length == 0){
    msg.payload= "no title found";
} else{
     msg.payload = msg.payload["items"][0]["title"]
}
return msg;